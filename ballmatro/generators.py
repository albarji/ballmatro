"""Functions to generate datasets for LLM training with ballmatro hands"""
from datasets import Dataset
from itertools import combinations_with_replacement
from functools import partial
from typing import List, Tuple, Generator, Callable

from ballmatro.card import Card, SUITS, RANKS, MODIFIERS
from ballmatro.optimizer import brute_force_optimize
from ballmatro.score import ScoreInfo

def exhaustive_generator(hand_size: int) -> Generator[Tuple[List[Card], ScoreInfo]]:
    """Generator functions for a dataset with all possible hands of a given size
    and their optimal plays using brute force optimization.
    Args:
        hand_size (int): The size of the hands to generate.
    Returns:
        List[Tuple[List[Card], ScoreInfo]]: A list of tuples, each containing a hand and its optimal play in the form of a ScoreInfo object.
    """
    # Generate all possible cards
    cards = [Card(f"{rank}{suit}{modifier}") for suit in SUITS for rank in RANKS for modifier in [""] + MODIFIERS]
    
    # Generate all combinations of the given size
    for input in combinations_with_replacement(cards, hand_size):
        # Find optimal play for this input
        optimal_play = brute_force_optimize(list(input))
        yield list(input), optimal_play

def generator_to_dict(func):
    """Decorator to convert a dataset generator to a dictionary generator, in a format suitable for Hugging Face datasets.
    
    Args:
        func (Callable): A generator function that yields tuples of input cards and plays with those cards.
    
    Returns:
        Callable: A generator function that yields dictionaries containing the input cards, played cards, and all the details of the score.
    """
    def wrapper(*args, **kwargs):
        for cards, score in func(*args, **kwargs):
            yield {
                "input": str(cards), 
                "output": str(score.played),
                "score": score.score, 
                "hand": score.hand.__name__, 
                "chips": score.chips,
                "multiplier": score.multiplier, 
                "remaining": score.remaining,
            }
    return wrapper

def to_hf_dataset(generating_function: Callable) -> Dataset:
    """Convert a dataset generator to a Hugging Face dataset format.
    
    Args:
        generating_function (Callable): A generator function that yields tuples of input cards and plays with those cards.
    
    Returns:
        Dataset: A Hugging Face dataset containing the generated data.
    """
    # Create a Hugging Face dataset from the generator
    return Dataset.from_generator(generator_to_dict(generating_function))
