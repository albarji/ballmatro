"""Class that represents a card, and associated functions"""
from dataclasses import dataclass
import re

SUITS = ["♣️", "♦️", "♠️", "♥️"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
MODIFIERS = [
    "+",  # Bonus card: +30 chips
    "x",  # Mult card: +4 multiplier
    "*",  # Wild card: can be used as a card from any suit
]
JOKER = "🃏"

@dataclass(frozen=True)
class Card:
    """Class that represents a card"""
    txt: str  # Text representation of the card

    @property
    def suit(self) -> str:
        """Return the suit of the card, or None if the card has no suit"""
        for suit in SUITS:
            if suit in self.txt:
                return suit
        return None

    @property
    def rank(self) -> str:
        """Return the rank of the card, or None if the card has no rank"""
        match = re.match(r"([2-9]|10|J|Q|K|A)", self.txt)
        if match is not None:
            return match.group(0)
        return None
    
    @property
    def rank_numeric(self) -> int:
        """Return the numeric value of the rank of the card, or None if the card has no rank"""
        return RANKS.index(self.rank) if self.rank is not None else None

    @property
    def modifier(self) -> str:
        """Return the modifier of the card, or None if the card has no modifier"""
        for modifier in MODIFIERS:
            if modifier in self.txt[-1]:
                return modifier
        return None
    
    @property
    def is_joker(self) -> bool:
        """Return True if the card is a joker, False otherwise"""
        return self.txt[0] == JOKER
    
    @property
    def joker_rule(self) -> str:
        """Return the joker rule of the card, or None if the card is not a joker"""
        if self.is_joker:
            return self.txt[1:]
        return None
