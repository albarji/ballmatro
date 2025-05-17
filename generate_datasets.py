"""Main function to generate datasets of Ballmatro hands and plays"""
import argparse

from ballmatro.generators import exhaustive_generator, to_hf_dataset

def main(hand_size: int, rng: int):
    """Main function to generate datasets of Ballmatro hands and plays"""
    # Generate the dataset
    dataset = to_hf_dataset(exhaustive_generator(hand_size))

    # Split dataset evenly into train and test sets
    dataset = dataset.train_test_split(test_size=0.5, seed=rng)

    # Save the dataset to compressed CSV files
    dataset["train"].to_parquet(f"exhaustive_size{hand_size}_train.parquet")
    dataset["test"].to_parquet(f"exhaustive_size{hand_size}_test.parquet")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate datasets of Ballmatro hands and plays")
    parser.add_argument("size", type=int, help="Size of the available cards")
    parser.add_argument("--rng", type=int, help="Random seed for reproducibility", default=42)
    args = parser.parse_args()
    main(args.size, args.rng)
