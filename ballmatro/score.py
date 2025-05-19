"""Functions to score ballmatro hands"""
from dataclasses import dataclass
from typing import List, Tuple


from ballmatro.card import Card
from ballmatro.hands import find_hand, InvalidHand


CHIPS_PER_RANK = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


@dataclass
class Score:
    """Class that represents the score and details of a played hand"""
    input: List[Card]  # Cards that were available for play
    played: List[Card]  # Cards played in the hand

    def __post_init__(self):
        # Find cards that were not played
        try:
            self.remaining = self._remaining_cards(self.input, self.played)
        except ValueError:
            self.remaining = None
        # Find the hand that was played
        self.hand = find_hand(self.played)
        # Score the played cards
        self._score_played()

    def __repr__(self):
        """Return a string representation of the score info"""
        return f"Score(input={self.input}, played={self.played}, remaining={self.remaining}, pokerhand={self.hand}, chips={self.chips}, multiplier={self.multiplier}, score={self.score})"
    
    def _remaining_cards(self, available: List[Card], played: List[Card]) -> List[Card]:
        """Returns the remaining (not played) cards after playing a hand"""
        remaining = available.copy()
        for card in played:
            # Check if the card is available
            if card not in remaining:
                raise ValueError(f"Impossible play: card {card} not in available cards")
            # Remove the card from the remaining cards
            remaining.remove(card)
        return remaining

    def _score_played(self):
        """Given a list of played cards, find their ballmatro score

        A score of 0 is attained when the hand is not recognized or the list of played cards contains cards that are not available.
        """
        # Check if the played cards were really available
        if self.remaining is None or self.hand == InvalidHand:
            self.chips = 0
            self.multiplier = 0
            self.score = 0
            return

        # Start scoring using the chips and multiplier of the hand type
        self.chips, self.multiplier = self.hand.chips, self.hand.multiplier
        # Now iterate over the cards in the order played, and score each card individually
        for card in self.played:
            self.chips, self.multiplier = _score_card(card, self.chips, self.multiplier)

        self.score = self.chips * self.multiplier

def _score_card(card: Card, chips: int, multiplier: int) -> Tuple[int, int]:
    """Applies the scoring of a single card to the current chips and multiplier"""
    # Add the chips of the card rank to the current chips
    chips += CHIPS_PER_RANK.get(card.rank, 0)
    # Apply modifiers
    if card.modifier == "+":
        chips += 30
    elif card.modifier == "x":
        multiplier += 4
    return chips, multiplier
