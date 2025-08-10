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

    def card_score_callback(self, card: Card, chips: int, multiplier: int, added_chips: int = 0, added_multiplier: int = 0) -> tuple[int, int]:
        """Callback that modifies the score of a card when this joker is present.

        Can be used to modify the score of a card based on the joker's rules.

        Args:
            card (Card): The card being scored.
            chips (int): chips score previous to scoring this card.
            multiplier (int): multiplier score previous to scoring this card.
            added_chips (int): additional chips that would normally be added to the score.
            added_multiplier (int): additional multiplier that would normally be added to the score.

        Returns:
            tuple[int, int]: the modified chips and multiplier values that will be added to the score due to this card.

        This method should be overridden by specific joker implementations.
        """
        return added_chips, added_multiplier

    def played_cards_callback(self, played_cards: list[Card]) -> list[Card]:
        """Callback that modifies the played cards when this joker is present.

        Can be used to modify the played cards based on the joker's rules.

        This method should be overridden by specific joker implementations.
        """
        return played_cards

    def __str__(self):
        return f"Joker(name={self.name})"

    def to_card(self) -> Card:
        """Returns a Card representation of the joker."""
        return Card(f"{JOKER}{self.name}: {self.description}")

class BlankJoker(Joker):
    """A joker that does not have any effect at all."""
    name = "Blank"
    description = "Does nothing at all"
