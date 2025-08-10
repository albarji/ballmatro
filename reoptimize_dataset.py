"""Tool to compute again the optimal plays for a given dataset"""

import argparse
from ballmatro.generators import add_optimal_plays, to_hf_dataset
from datasets import load_dataset

from ballmatro.card import parse_card_list


def main(dataset: str):
    """Run the optimizer over a dataset of results to find the optimal plays, and recompute statistics"""
    ds = load_dataset("albarji/ballmatro", dataset)

    train = optimize_dataset(ds["train"])
    test = optimize_dataset(ds["test"])

    for dataset_orig, dataset_new in [[ds["train"], train], [ds["test"], test]]:
        for data_orig, data_new in zip(dataset_orig, dataset_new):
            if data_orig != data_new:
                print(f"Optimal play changed:\n\t{data_orig}\n\t{data_new}")

    train.to_parquet("train.parquet")
    test.to_parquet("test.parquet")


def optimize_dataset(dataset: list[dict]) -> list[dict]:
    """Find the optimal plays for a given Hugging Face dataset fold"""
    generator = add_optimal_plays([parse_card_list(data["input"]) for data in dataset])
    return to_hf_dataset(generator)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the optimizer over a dataset to recompute the optimal plays")
    parser.add_argument("dataset", type=str, help="Hugging Face name of the dataset fold to process.")
    args = parser.parse_args()
    main(args.dataset)
