"""Abstract class for joker cards"""

from ballmatro.card import Card, JOKER
from ballmatro.hands import PokerHand


class Joker:
    """An abstract class that represents a joker card. Implements the logic to activate the joker's effect when scoring.
    
    Each specific joker should inherit from this class and override the appropriate attributes and callbacks.
    """
    name: str  # Name of the joker card
    description: str  # Description of the joker's effect

    def played_hand_callback(self, hand: PokerHand) -> PokerHand:
        """Callback that modifies the played hand when this joker is present.

        Can be used to modify the hand type or score based on the joker's rules.

        This method should be overridden by specific joker implementations.
        """
        return hand

    def __str__(self):
        return f"Joker(name={self.name})"

    def to_card(self) -> Card:
        """Returns a Card representation of the joker."""
        return Card(f"{JOKER}{self.name}: {self.description}")

class BlankJoker(Joker):
    """A joker that does not have any effect at all."""
    name = "Blank"
    description = "Does nothing at all."
