"""Rank boosters jokers: modify the score provided by a card depending on the rank of the card played."""

from ballmatro.jokers.joker import Joker
from ballmatro.card import Card


class DerankedJoker(Joker):
    """A joker that changes the scoring of a rank card to 0 chips and 0 multiplier, ignoring possible modifiers."""
    target_rank: str

    def card_score_callback(self, card: Card, chips: int, multiplier: int, added_chips: int = 0, added_multiplier: int = 0) -> tuple[int, int]:
        if card.rank == self.target_rank:
            return 1, 0
        else:            
            return added_chips, added_multiplier

class DerankedTwo(DerankedJoker):
    """A joker that changes the scoring of a rank 2 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Two"
    description = "Card with rank 2 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "2"

class DerankedThree(DerankedJoker):
    """A joker that changes the scoring of a rank 3 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Three"
    description = "Card with rank 3 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "3"

class DerankedFour(DerankedJoker):
    """A joker that changes the scoring of a rank 4 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Four"
    description = "Card with rank 4 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "4"

class DerankedFive(DerankedJoker):
    """A joker that changes the scoring of a rank 5 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Five"
    description = "Card with rank 5 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "5"

class DerankedSix(DerankedJoker):
    """A joker that changes the scoring of a rank 6 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Six"
    description = "Card with rank 6 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "6"

class DerankedSeven(DerankedJoker):
    """A joker that changes the scoring of a rank 7 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Seven"
    description = "Card with rank 7 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "7"

class DerankedEight(DerankedJoker):
    """A joker that changes the scoring of a rank 8 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Eight"
    description = "Card with rank 8 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "8"

class DerankedNine(DerankedJoker):
    """A joker that changes the scoring of a rank 9 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Nine"
    description = "Card with rank 9 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "9"

class DerankedTen(DerankedJoker):
    """A joker that changes the scoring of a rank 10 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Ten"
    description = "Card with rank 10 give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "10"

class DerankedJack(DerankedJoker):
    """A joker that changes the scoring of a rank J card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Jack"
    description = "Card with rank J give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "J"

class DerankedQueen(DerankedJoker):
    """A joker that changes the scoring of a rank Q card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Queen"
    description = "Card with rank Q give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "Q"

class DerankedKing(DerankedJoker):
    """A joker that changes the scoring of a rank K card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked King"
    description = "Card with rank K give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "K"

class DerankedAce(DerankedJoker):
    """A joker that changes the scoring of a rank A card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Ace"
    description = "Card with rank A give 1 chip and 0 multiplier, ignoring modifiers"
    target_rank = "A"
