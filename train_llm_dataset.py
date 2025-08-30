"""Main tool to train an LLM against a Ballmatro dataset."""

import argparse
import json

from gpt.gpt import hf_stf_ballmatro_dataset, hf_grpo_ballmatro_dataset
from datasets import load_dataset

TRAINING_ALGORITHMS = {
    "sft": hf_stf_ballmatro_dataset,
    "grpo": hf_grpo_ballmatro_dataset
}

def main(dataset: str, model: str, output: str = None, algorithm: str = None, config_file: str = None, lora_config_file: str = None):
    """Main function to test an LLM against a Ballmatro dataset."""

    # Load configuration files
    try:
        with open(config_file, "r") as f:
            training_kwargs = json.load(f)
    except Exception as e:
        print(f"Error loading config file {config_file}: {e}")
    if lora_config_file is not None:
        try:
            with open(lora_config_file, "r") as f:
                lora_kwargs = json.load(f)
        except Exception as e:
            print(f"Error loading LoRA config file {lora_config_file}: {e}")

    # Download the dataset from the Hugging Face Hub
    ds = load_dataset("albarji/ballmatro", dataset)
    if "train" not in ds:
        raise ValueError(f"Dataset {dataset} does not contain a 'train' partition.")

    TRAINING_ALGORITHMS[algorithm](ds["train"], model, output, training_kwargs=training_kwargs, lora_kwargs=lora_kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Hugging Face model against a Ballmatro dataset")
    parser.add_argument("dataset", type=str, help="Name of the dataset to train against. Must be the name of a partition of the BaLLMatro dataset in the Hugging Face Hub.")
    parser.add_argument("model", type=str, help="Name of the Hugging Face model to use for training.")
    parser.add_argument("algorithm", type=str, help="Training algorithm to use.", choices=list(TRAINING_ALGORITHMS.keys()))
    parser.add_argument("config_file", type=str, help="Path to the JSON configuration file with training arguments.")
    parser.add_argument("output", type=str, help="Folder to save the trained model to.")
    parser.add_argument("--lora_config", type=str, default=None, help="Path to the LoRA configuration file (optional).")
    args = parser.parse_args()
    main(args.dataset, args.model, args.output, algorithm=args.algorithm, config_file=args.config_file, lora_config_file=args.lora_config)
