"""Functions to try to solve a Ballmatro dataset using a GPT model."""

import logging
import os
import re

from ballmatro.score import ScoreDataset

from openai import OpenAI
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from trl import SFTConfig, SFTTrainer


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
LOGGER = logging.getLogger(__name__)

README_PATH = "README.md"

THINKING_MODELS_FINISHERS = {
    "Qwen/Qwen3": "</think>",
    "openai/gpt-oss": "assistantfinal"
}

ALTERNATIVE_CHAT_TEMPLATES = {
    "Qwen/Qwen3": "gpt/chat_templates/qwen3",
}

def gpt_attempt_ballmatro_dataset(dataset: list[dict], model: str = "gpt-4o") -> list[str]:
    """Use a GPT model to attempt to solve a Ballmatro dataset.

    Returns a list of responses from the model for each item in the dataset.
    """
    openai = OpenAI()
    system_prompt = build_system_prompt()
    responses = []
    for i, data in enumerate(dataset):
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": data["input"]}
            ]
        )
        content = response.choices[0].message.content
        LOGGER.info(f"({i+1}/{len(dataset)}): {data['input']} -> {content}")
        # Append the response content to the list
        responses.append(content)
    return ScoreDataset(dataset, responses)

def hf_attempt_ballmatro_dataset(dataset: list[dict], model_name: str, max_new_tokens: int = 16384) -> list[str]:
    """Use a Hugging Face model to attempt to solve a Ballmatro dataset.

    Returns a list of responses from the model for each item in the dataset.
    """
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # Automatically loads the model into the GPU, if one is available
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Load alternative chat template if it exists
    for registered_template_prefix in ALTERNATIVE_CHAT_TEMPLATES.keys():
        if model_name.startswith(registered_template_prefix):
            LOGGER.info(f"Using alternative chat template for model {model_name}")
            with open(ALTERNATIVE_CHAT_TEMPLATES[registered_template_prefix], "r") as f:
                tokenizer.template = f.read()

    generation_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_tokens,
    )

    system_prompt = build_system_prompt()
    responses = []
    for i, data in enumerate(dataset):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": data["input"]}
        ]
        result = generation_pipeline(messages)[0]["generated_text"][-1]["content"]
        # If thinking model but chain of thought is unfinished, continue generation forcing final response
        if _is_thinking_model(model_name) and not _thinking_finished(result):
            try:
                LOGGER.warning(f"Model {model_name} did not finish thinking. Forcing generation to end.")
                messages.append({"role": "assistant", "content": result + "\n" + _thinking_model_finisher(model_name)})
                result = generation_pipeline(messages)[0]["generated_text"][-1]["content"]
            except Exception as e:
                LOGGER.error(f"Error occurred while forcing generation to end: {e}")
                result = ""
        if _is_thinking_model(model_name):
            result = _remove_chain_of_thought(result)
        LOGGER.info(f"({i+1}/{len(dataset)}): {data['input']} -> {result}")
        # Append the response content to the list
        responses.append(result)
    return ScoreDataset(dataset, responses)

def _is_thinking_model(model_name: str) -> bool:
    """Tries to identify by its name if a Hugging Face model is a thinking model. Returns False for unknown models"""
    return any(model_name.startswith(prefix) for prefix in THINKING_MODELS_FINISHERS.keys())

def _thinking_model_finisher(model_name: str) -> str:
    """Return the string that marks the end of a chain of thought for the given model.

    Return empty string if the model is not a known thinking model"""
    for key, value in THINKING_MODELS_FINISHERS.items():
        if model_name.startswith(key):
            return value
    return ""

def _thinking_finished(model_output: str) -> bool:
    """Check if the thinking process has finished based on the model output."""
    return any(finisher in model_output for finisher in THINKING_MODELS_FINISHERS.values())

def _remove_chain_of_thought(result: str) -> str:
    """Removes the chaing of thought part from the output, returning only the final LLM response"""
    # Remove <think></think> section from the result, if present (Qwen 3 models)
    result = re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL).strip()
    # Remove everything up to </think> mark from the result, if present (Qwen 3 Thinking models)
    result = re.sub(r"^.*?</think>", "", result, flags=re.DOTALL).strip()
    # Remove analysis-assistantfinal section from the result, if present (gpt-oss models)
    result = re.sub(r"^analysis.*?assistantfinal", "", result, flags=re.DOTALL).strip()
    return result

def build_system_prompt() -> str:
    """Build the system prompt for the GPT model, making use of the README file."""
    # Read contents of the README file
    with open(README_PATH, "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()
    # Extract the section for the rules
    sections = markdown_to_sections(readme_content)
    if "The rules of BaLLMatro" not in sections:
        raise ValueError("README file does not contain the rules section.")
    # Use the rules section to build the system prompt
    return sections["The rules of BaLLMatro"]

def markdown_to_sections(markdown: str) -> dict[str, str]:
    """Convert a markdown string into a dictionary from section titles to content."""
    sections = {}
    current_title = None
    current_content = []
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("## "):
            if current_title:
                sections[current_title] = "\n".join(current_content)
            current_title = line[3:]
            current_content = []
        elif current_title:
            current_content.append(line)
    if current_title:
        sections[current_title] = "\n".join(current_content)
    return sections

def hf_stf_ballmatro_dataset(dataset: list[dict], model_name: str, output_model_path: str, **training_kwargs) -> AutoModelForCausalLM:
    """Trains a Hugging Face model on a BaLLMatro dataset using Supervised Fine Tuning.

    All parameters in **training_kwargs are passed to the TRL SFTConfig.

    Returns the trained model.
    """
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # Automatically loads the model into the GPU, if one is available
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Adapt data to standard SFTTrainer format
    formatted_train = dataset.map(
        lambda example: {
            "messages": [
                {"role": "user", "content": example["input"]},  # User message contains the problem input
                {"role": "assistant", "content": example["output"]}  # Assistant message containts the ideal output
            ]
        }
    )

    training_args = SFTConfig(
        max_length=256,  # Maximum length (in tokens) of tokenized LLM inputs
        logging_steps=25,  # Log training results every 25 steps
        save_strategy="no",
        **training_kwargs
    )

    trainer = SFTTrainer(
        model,  # Base model to fine-tune
        train_dataset=formatted_train,  # Training dataset
        args=training_args,  # Previously prepared SFTConfig object
    )
    trainer.train()

    model.save_pretrained(output_model_path)
    tokenizer.save_pretrained(output_model_path)

    return model
