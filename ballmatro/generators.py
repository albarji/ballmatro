"""Functions to generate datasets for LLM training with ballmatro hands"""
from itertools import combinations_with_replacement
from typing import List, Tuple

from ballmatro.card import Card, SUITS, RANKS, MODIFIERS
from ballmatro.optimizer import brute_force_optimize
from ballmatro.score import ScoreInfo

def exhaustive_generator(hand_size: int) -> List[Tuple[List[Card], ScoreInfo]]:
    """Generate a dataset with all possible hands of a given size
    and their optimal plays using brute force optimization.
    Args:
        hand_size (int): The size of the hands to generate.
    Returns:
        List[Tuple[List[Card], ScoreInfo]]: A list of tuples, each containing a hand and its optimal play in the form of a ScoreInfo object.
    """
    # Generate all possible cards
    cards = [Card(f"{rank}{suit}{modifier}") for suit in SUITS for rank in RANKS for modifier in MODIFIERS]
    
    # Generate all combinations of the given size
    inputs = [list(hand) for hand in combinations_with_replacement(cards, hand_size)]
    # Find optimal hands and scores for each combination
    optimal_plays = [brute_force_optimize(hand) for hand in inputs]

    return list(zip(inputs, optimal_plays))
