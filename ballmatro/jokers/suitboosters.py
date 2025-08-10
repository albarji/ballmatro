"""Suit boosters jokers: modify the score provided by a card depending on the suit of the card played."""

from typing import List
from ballmatro.jokers.joker import Joker
from ballmatro.card import Card


class DesuitedJoker(Joker):
    """A joker that changes the scoring of a suit card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    target_suit: str

    def card_score_callback(self, card: Card, chips: int, multiplier: int, added_chips: int = 0, added_multiplier: int = 0) -> tuple[int, int]:
        if card.suit == self.target_suit:
            return 1, 0
        else:            
            return added_chips, added_multiplier

class DesuitedClub(DesuitedJoker):
    """A joker that changes the scoring of a club card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Desuited Club"
    description = "Cards with club suit give 1 chip and 0 multiplier, ignoring modifiers"
    target_suit = "♣"

class DesuitedDiamond(DesuitedJoker):
    """A joker that changes the scoring of a diamond card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Desuited Diamond"
    description = "Cards with diamond suit give 1 chip and 0 multiplier, ignoring modifiers"
    target_suit = "♦"

class DesuitedSpade(DesuitedJoker):
    """A joker that changes the scoring of a spade card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Desuited Spade"
    description = "Cards with spade suit give 1 chip and 0 multiplier, ignoring modifiers"
    target_suit = "♠"

class DesuitedHeart(DesuitedJoker):
    """A joker that changes the scoring of a heart card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Desuited Heart"
    description = "Cards with heart suit give 1 chip and 0 multiplier, ignoring modifiers"
    target_suit = "♥"

class PowerSuitJoker(Joker):
    """A joker that duplicates the chips and multiplier of a card if its suit is in a target set."""
    target_suits: List[str]

    def card_score_callback(self, card: Card, chips: int, multiplier: int, added_chips: int = 0, added_multiplier: int = 0) -> tuple[int, int]:
        if card.suit in self.target_suits:
            return added_chips * 2, added_multiplier * 2
        else:
            return added_chips, added_multiplier

class EmpoweredClub(PowerSuitJoker):
    """A joker that duplicates the chips and multiplier of a card if its suit is a club."""
    name = "Empowered Club"
    description = "Double the chips and multiplier for cards with club suit"
    target_suits = ["♣"]

class EmpoweredDiamond(PowerSuitJoker):
    """A joker that duplicates the chips and multiplier of a card if its suit is a diamond."""
    name = "Empowered Diamond"
    description = "Double the chips and multiplier for cards with diamond suit"
    target_suits = ["♦"]

class EmpoweredSpade(PowerSuitJoker):
    """A joker that duplicates the chips and multiplier of a card if its suit is a spade."""
    name = "Empowered Spade"
    description = "Double the chips and multiplier for cards with spade suit"
    target_suits = ["♠"]

class EmpoweredHeart(PowerSuitJoker):
    """A joker that duplicates the chips and multiplier of a card if its suit is a heart."""
    name = "Empowered Heart"
    description = "Double the chips and multiplier for cards with heart suit"
    target_suits = ["♥"]

class RedEmpire(PowerSuitJoker):
    """A joker that duplicates the chips and multiplier of a card if its suit is a heart or a diamond."""
    name = "Red Empire"
    description = "Double the chips and multiplier for cards with heart or diamond suit"
    target_suits = ["♥", "♦"]

class BlackEmpire(PowerSuitJoker):
    """A joker that duplicates the chips and multiplier of a card if its suit is a spade or a club."""
    name = "Black Empire"
    description = "Double the chips and multiplier for cards with spade or club suit"
    target_suits = ["♠", "♣"]
