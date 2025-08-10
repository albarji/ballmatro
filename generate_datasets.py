"""Main function to generate datasets of Ballmatro hands and plays"""
import argparse

from ballmatro.jokers.factory import JOKERS
from ballmatro.generators import GENERATION_ALGORITHMS, add_jokers, add_optimal_plays, to_hf_dataset

def main(algorithm: str, hand_size: int, n: int, rng: int, min_n_jokers: int, max_n_jokers: int, jokers_max_id: int):
    """Main function to generate datasets of Ballmatro hands and plays"""
    # Check inputs
    if algorithm not in GENERATION_ALGORITHMS:
        raise ValueError(f"Unknown algorithm: {algorithm}. Available algorithms: {list(GENERATION_ALGORITHMS.keys())}")
    if min_n_jokers < 0 or max_n_jokers < min_n_jokers:
        raise ValueError(f"Invalid joker range: {min_n_jokers} - {max_n_jokers}")
    # Adjust parameters
    if algorithm == "exhaustive":
        # For exhaustive generation, n is ignored and hand_size is used directly
        params = {"max_hand_size": hand_size}
    else:
        params = {"max_hand_size": hand_size, "n": n, "seed": rng}
    # Generate the dataset
    generator = GENERATION_ALGORITHMS[algorithm](**params)
    # Add jokers if specified
    if min_n_jokers > 0:
        generator = add_jokers(generator, min_n_jokers, max_n_jokers, jokers_max_id)
    generator = add_optimal_plays(generator)
    dataset = to_hf_dataset(generator)

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
    parser.add_argument("--min_n_jokers", type=int, help="Minimum number of jokers to add to each hand", default=0)
    parser.add_argument("--max_n_jokers", type=int, help="Maximum number of jokers to add to each hand", default=0)
    parser.add_argument("--jokers_max_id", type=int, help="Limit range of jokers to include in the generation to include only jokers with IDs between 0 and the given number (inclusive).", default=len(JOKERS)-1)
    args = parser.parse_args()
    main(args.alg, args.len, args.n, args.rng, args.min_n_jokers, args.max_n_jokers, args.jokers_max_id)
