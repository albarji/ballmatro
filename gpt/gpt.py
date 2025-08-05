"""Functions to try to solve a Ballmatro dataset using a GPT model."""

import logging
import os

from ballmatro.score import ScoreDataset

from openai import OpenAI
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
LOGGER = logging.getLogger(__name__)

README_PATH = "README.md"

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

def hf_attempt_ballmatro_dataset(dataset: list[dict], model_name: str) -> list[str]:
    """Use a Hugging Face model to attempt to solve a Ballmatro dataset.

    Returns a list of responses from the model for each item in the dataset.
    """
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # Automatically loads the model into the GPU, if one is available
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    generation_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    system_prompt = build_system_prompt()
    responses = []
    for i, data in enumerate(dataset):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": data["input"]}
        ]
        result = generation_pipeline(messages)[0]["generated_text"][-1]["content"]
        LOGGER.info(f"({i+1}/{len(dataset)}): {data['input']} -> {result}")
        # Append the response content to the list
        responses.append(result)
    return ScoreDataset(dataset, responses)

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
