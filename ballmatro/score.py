"""Functions to score ballmatro hands"""
from typing import List, Tuple


from ballmatro.card import Card
from ballmatro.hands import find_hand


CHIPS_PER_RANK = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


def score(available: List[Card], played: List[Card]) -> int:
    """Given a list of played cards, find their ballmatro score
    
    A score of 0 is attained when the hand is not recognized or the list of played cards contains cards that are not available.
    """
    # Check if the played cards are available
    if set(played) - set(available):
        return 0
    # Find the hand type
    hand = find_hand(played)
    if hand is None:
        return 0
    
    # Start scoring using the chips and multiplier of the hand type
    chips, multiplier = hand.chips, hand.multiplier
    # Now iterate over the cards in the order played, and score each card individually
    for card in played:
        chips, multiplier = score_card(card, chips, multiplier)

    return chips * multiplier

def score_card(card: Card, chips: int, multiplier: int) -> Tuple[int, int]:
    """Applies the scoring of a single card to the current chips and multiplier"""
    # Add the chips of the card rank to the current chips
    chips += CHIPS_PER_RANK.get(card.rank, 0)
    # Apply modifiers
    if card.modifier == "+":
        chips += 30
    elif card.modifier == "x":
        multiplier += 4
    return chips, multiplier
