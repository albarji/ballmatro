"""Main function to generate datasets of Ballmatro hands and plays"""
import argparse

from ballmatro.generators import GENERATION_ALGORITHMS, to_hf_dataset

def main(algorithm: str, hand_size: int, n: int, rng: int):
    """Main function to generate datasets of Ballmatro hands and plays"""
    # Check inputs
    if algorithm not in GENERATION_ALGORITHMS:
        raise ValueError(f"Unknown algorithm: {algorithm}. Available algorithms: {list(GENERATION_ALGORITHMS.keys())}")
    # Adjust parameters
    if algorithm == "exhaustive":
        # For exhaustive generation, n is ignored and hand_size is used directly
        params = {"max_hand_size": hand_size}
    else:
        params = {"max_hand_size": hand_size, "n": n, "seed": rng}
    # Generate the dataset
    dataset = to_hf_dataset(GENERATION_ALGORITHMS[algorithm](**params))

    # Split dataset evenly into train and test sets
    dataset = dataset.train_test_split(test_size=0.5, seed=rng)

    # Save the dataset to compressed CSV files
    dataset["train"].to_parquet("train.parquet")
    dataset["test"].to_parquet("test.parquet")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate datasets of Ballmatro hands and plays")
    parser.add_argument("alg", type=str, help=f"Algorithm to use for generating the dataset, must be one of {list(GENERATION_ALGORITHMS.keys())}")
    parser.add_argument("len", type=int, help="Maximum number of cards in the hands. For exhaustive generation, this is always the hand size.")
    parser.add_argument("n", type=int, help="Number of hands to generate. For exhaustive generation, this is ignored.")
    parser.add_argument("--rng", type=int, help="Random seed for reproducibility. For exhaustive generation, this is ignored.", default=42)
    args = parser.parse_args()
    main(args.alg, args.len, args.n, args.rng)
