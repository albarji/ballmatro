"""Main tool to train an LLM against a Ballmatro dataset."""

import argparse

from gpt.gpt import hf_stf_ballmatro_dataset, hf_grpo_ballmatro_dataset
from datasets import load_dataset

TRAINING_ALGORITHMS = {
    "sft": hf_stf_ballmatro_dataset,
    "grpo": hf_grpo_ballmatro_dataset
}

def main(dataset: str, model: str, output: str = None, algorithm: str = None, **training_kwargs):
    """Main function to test an LLM against a Ballmatro dataset."""

    # Download the dataset from the Hugging Face Hub
    ds = load_dataset("albarji/ballmatro", dataset)
    if "train" not in ds:
        raise ValueError(f"Dataset {dataset} does not contain a 'train' partition.")

    TRAINING_ALGORITHMS[algorithm](ds["train"], model, output, **training_kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Hugging Face model against a Ballmatro dataset")
    parser.add_argument("dataset", type=str, help="Name of the dataset to train against. Must be the name of a partition of the BaLLMatro dataset in the Hugging Face Hub.")
    parser.add_argument("model", type=str, help="Name of the Hugging Face model to use for training.")
    parser.add_argument("algorithm", type=str, help="Training algorithm to use.", choices=list(TRAINING_ALGORITHMS.keys()))
    parser.add_argument("output", type=str, help="Folder to save the trained model to.")
    parser.add_argument("--per_device_train_batch_size", type=int, help="Batch size to use for training.", default=8)
    args = parser.parse_args()
    main(args.dataset, args.model, args.output, algorithm=args.algorithm, per_device_train_batch_size=args.per_device_train_batch_size)
