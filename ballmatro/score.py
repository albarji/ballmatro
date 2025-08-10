"""Functions to score ballmatro hands"""
from dataclasses import dataclass
from datasets import Dataset
from typing import List, Tuple, Union


from ballmatro.card import Card, parse_card_list
from ballmatro.hands import find_hand, NoPokerHand, InvalidPlay
from ballmatro.jokers.factory import find_joker_card
from ballmatro.jokers.joker import Joker


CHIPS_PER_RANK = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


@dataclass
class Score:
    """Class that represents the score and details of a played hand.

    The scoring procedure is as follows:
    1. Check if the played hand is valid (i.e., all cards were available).
    2. Find the type of hand played (e.g., Straight Flush, Four of a Kind, etc.), and initialize the chips and multiplier based on that hand.
    3. Go over each card and apply its rank and multipliers to the current chips and multiplier.
    4. The final score is the product of the chips and multiplier.
    """
    input: Union[List[Card], str]  # Cards that were available for play
    played: Union[List[Card], str]  # Cards played in the hand

    def __post_init__(self):
        try:
            # Parse the input and played cards
            if isinstance(self.input, str):
                self.input = parse_card_list(self.input)
            if isinstance(self.played, str):
                self.played = parse_card_list(self.played)
            # Find cards that were not played
            self.remaining = self._remaining_cards(self.input, self.played)
            # Find jokers in the remaining cards
            self.jokers = self._find_jokers()
            # Apply the jokers to the played cards
            for joker in self.jokers:
                self.played = joker.played_cards_callback(self.played)
            # Find the hand that was played
            self.hand = find_hand(self.played)
            # Apply the jokers to the hand if any
            for joker in self.jokers:
                self.hand = joker.played_hand_callback(self.hand)
        except ValueError:
            self.remaining = None
            self.hand = InvalidPlay()
        # Score the played cards to compute the final score
        self._score_played()

    def __repr__(self):
        """Return a string representation of the score info"""
        return f"Score(input={self.input}, played={self.played}, remaining={self.remaining}, hand={self.hand.name}, chips={self.chips}, multiplier={self.multiplier}, score={self.score})"
    
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

    def _find_jokers(self) -> List[Joker]:
        """Find jokers in the remaining cards"""
        return [find_joker_card(card) for card in self.remaining if card.is_joker]

    def _score_played(self):
        """Given a list of played cards, find their ballmatro score

        A score of 0 is attained when the hand is not recognized or the list of played cards contains cards that are not available.
        """
        # Check if the played cards were really available
        if self.remaining is None or isinstance(self.hand, (NoPokerHand, InvalidPlay)):
            self.chips = 0
            self.multiplier = 0
            self.score = 0
            return

        # Start scoring using the chips and multiplier of the hand type
        self.chips, self.multiplier = self.hand.chips, self.hand.multiplier
        # Now iterate over the cards in the order played, and score each card individually
        for card in self.played:
            self.chips, self.multiplier = self._score_card(card, self.chips, self.multiplier)

        self.score = self.chips * self.multiplier

    def asdict(self) -> dict:
        """Return the score as a dictionary"""
        return {
            "input": [card.txt for card in self.input] if isinstance(self.input, list) else self.input,
            "played": [card.txt for card in self.played] if isinstance(self.played, list) else self.played,
            "remaining": [card.txt for card in self.remaining] if self.remaining else None,
            "hand": self.hand.name,
            "chips": self.chips,
            "multiplier": self.multiplier,
            "score": self.score
        }

    def _score_card(self, card: Card, chips: int, multiplier: int) -> Tuple[int, int]:
        """Applies the scoring of a single card to the current chips and multiplier"""
        # Add the chips of the card rank to the current chips
        extra_chips = CHIPS_PER_RANK.get(card.rank, 0)
        extra_multiplier = 0
        # Apply modifiers
        if card.modifier == "+":
            extra_chips += 30
        elif card.modifier == "x":
            extra_multiplier += 4
        # Apply jokers to the card score
        for joker in self.jokers:
            extra_chips, extra_multiplier = joker.card_score_callback(card, chips, multiplier, extra_chips, extra_multiplier)
        # Return the new chips and multiplier
        return chips + extra_chips, multiplier + extra_multiplier

@dataclass
class ScoreDataset:
    """Class that represents the scores obtained over a whole Ballmatro dataset"""
    dataset: Dataset  # Dataset containing the hands and optimal plays
    plays: List[Union[str, List[Card]]]  # List of plays (hands) carried out for the dataset
    scores: List[Score] = None  # Detailed Score objects for each play
    total_score: int = 0  # Total score of the plays over the whole dataset
    normalized_score: float = 0.0  # Normalized score [0,1] of the plays over the whole dataset
    invalid_hands: int = 0  # Number of invalid hands played
    normalized_invalid_hands: float = 0.0  # Fraction of invalid hands played [0,1]

    def __post_init__(self):
        # Check inputs
        if len(self.dataset) != len(self.plays):
            raise ValueError("Dataset and plays must have the same length")
        # Score the plays
        self.scores = [Score(input, played) for input, played in zip(self.dataset["input"], self.plays)]
        # Compute normalized scores
        self.normalized_scores = [score.score / reference_score for score, reference_score in zip(self.scores, self.dataset["score"])]
        # Compute statistics
        self.total_score = sum(score.score for score in self.scores)
        self.total_normalized_score = sum(self.normalized_scores) / len(self.normalized_scores)
        self.invalid_hands = sum(1 for score in self.scores if isinstance(score.hand, (NoPokerHand, InvalidPlay)))
        self.normalized_invalid_hands = self.invalid_hands / len(self.scores)

    def __repr__(self):
        """Return a string representation of the score info"""
        return f"ScoreDataset(total_score={self.total_score}, total_normalized_score={self.total_normalized_score}, invalid_hands={self.invalid_hands}, normalized_invalid_hands={self.normalized_invalid_hands})"

    def asdict(self) -> dict:
        """Return the score dataset as a dictionary"""
        return {
            "total_score": self.total_score,
            "total_normalized_score": self.total_normalized_score,
            "invalid_hands": self.invalid_hands,
            "normalized_invalid_hands": self.normalized_invalid_hands,
            "scores": [score.asdict() for score in self.scores],
            "normalized_scores": self.normalized_scores,
        }
