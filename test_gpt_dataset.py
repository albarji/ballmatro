"""Main tool to test a GPT model against a Ballmatro dataset."""

import argparse
import json

from gpt.gpt import gpt_attempt_ballmatro_dataset
from datasets import load_dataset


def main(dataset: str, model: str, output: str = None):
    """Main function to test a GPT model against a Ballmatro dataset."""
    # Download the dataset from the Hugging Face Hub
    ds = load_dataset("albarji/ballmatro", dataset)
    if "test" not in ds:
        raise ValueError(f"Dataset {dataset} does not contain a 'test' partition.")

    # Run the GPT model on the test set
    results = gpt_attempt_ballmatro_dataset(ds["test"], model)

    # Format the results in a readable way
    results = results.asdict()
    # Save the results
    with open(output, "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a GPT model against a Ballmatro dataset")
    parser.add_argument("dataset", type=str, help="Name of the dataset to test against. Must be the name of a partition of the BaLLMatro dataset in the Hugging Face Hub.")
    parser.add_argument("model", type=str, help="Name of the GPT model to use for testing.")
    parser.add_argument("output", type=str, help="File to save the benchmark results to (JSON format).")
    args = parser.parse_args()
    main(args.dataset, args.model, args.output)
