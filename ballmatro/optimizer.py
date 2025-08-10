"""Functions to find the best hand in a given set of cards"""
from itertools import combinations
import math
from typing import List

from ballmatro.card import Card
from ballmatro.score import Score

def brute_force_optimize(cards: List[Card]) -> Score:
    """Find the best hand in a given set of cards using brute force"""
    # Joker can't be played, so we keep them apart
    non_joker_cards = [card for card in cards if card.is_joker is False]

    best_score = -math.inf
    for i in range(0, len(non_joker_cards) + 1):
        for hand in combinations(non_joker_cards, i):
            score_info = Score(cards, list(hand))
            if score_info.score > best_score:
                best_score = score_info.score
                best_result = score_info
    return best_result
