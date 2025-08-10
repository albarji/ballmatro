"""Rank boosters jokers: modify the score provided by a card depending on the rank of the card played."""

from typing import List
from ballmatro.jokers.joker import Joker
from ballmatro.card import Card


class DerankedJoker(Joker):
    """A joker that changes the scoring of a rank card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    target_rank: str

    def card_score_callback(self, card: Card, chips: int, multiplier: int, added_chips: int = 0, added_multiplier: int = 0) -> tuple[int, int]:
        if card.rank == self.target_rank:
            return 1, 0
        else:            
            return added_chips, added_multiplier

class DerankedTwo(DerankedJoker):
    """A joker that changes the scoring of a rank 2 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Two"
    description = "Cards with rank 2 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "2"

class DerankedThree(DerankedJoker):
    """A joker that changes the scoring of a rank 3 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Three"
    description = "Cards with rank 3 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "3"

class DerankedFour(DerankedJoker):
    """A joker that changes the scoring of a rank 4 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Four"
    description = "Cards with rank 4 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "4"

class DerankedFive(DerankedJoker):
    """A joker that changes the scoring of a rank 5 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Five"
    description = "Cards with rank 5 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "5"

class DerankedSix(DerankedJoker):
    """A joker that changes the scoring of a rank 6 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Six"
    description = "Cards with rank 6 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "6"

class DerankedSeven(DerankedJoker):
    """A joker that changes the scoring of a rank 7 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Seven"
    description = "Cards with rank 7 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "7"

class DerankedEight(DerankedJoker):
    """A joker that changes the scoring of a rank 8 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Eight"
    description = "Cards with rank 8 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "8"

class DerankedNine(DerankedJoker):
    """A joker that changes the scoring of a rank 9 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Nine"
    description = "Cards with rank 9 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "9"

class DerankedTen(DerankedJoker):
    """A joker that changes the scoring of a rank 10 card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Ten"
    description = "Cards with rank 10 give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "10"

class DerankedJack(DerankedJoker):
    """A joker that changes the scoring of a rank J card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Jack"
    description = "Cards with rank J give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "J"

class DerankedQueen(DerankedJoker):
    """A joker that changes the scoring of a rank Q card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Queen"
    description = "Cards with rank Q give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "Q"

class DerankedKing(DerankedJoker):
    """A joker that changes the scoring of a rank K card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked King"
    description = "Cards with rank K give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "K"

class DerankedAce(DerankedJoker):
    """A joker that changes the scoring of a rank A card to 1 chip and 0 multiplier, ignoring possible modifiers."""
    name = "Deranked Ace"
    description = "Cards with rank A give 1 chip and 0 multiplier. Modifiers are ignored."
    target_rank = "A"

class PowerRankJoker(Joker):
    """A joker that duplicates the chips and multiplier of a card if its rank is in a target set."""
    target_ranks: List[str]

    def card_score_callback(self, card: Card, chips: int, multiplier: int, added_chips: int = 0, added_multiplier: int = 0) -> tuple[int, int]:
        if card.rank in self.target_ranks:
            return added_chips * 2, added_multiplier * 2
        else:
            return added_chips, added_multiplier

class EmpoweredTwo(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 2."""
    name = "Empowered Two"
    description = "Double the chips and multiplier for cards with rank 2"
    target_ranks = ["2"]

class EmpoweredThree(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 3."""
    name = "Empowered Three"
    description = "Double the chips and multiplier for cards with rank 3"
    target_ranks = ["3"]

class EmpoweredFour(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 4."""
    name = "Empowered Four"
    description = "Double the chips and multiplier for cards with rank 4"
    target_ranks = ["4"]

class EmpoweredFive(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 5."""
    name = "Empowered Five"
    description = "Double the chips and multiplier for cards with rank 5"
    target_ranks = ["5"]

class EmpoweredSix(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 6."""
    name = "Empowered Six"
    description = "Double the chips and multiplier for cards with rank 6"
    target_ranks = ["6"]

class EmpoweredSeven(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 7."""
    name = "Empowered Seven"
    description = "Double the chips and multiplier for cards with rank 7"
    target_ranks = ["7"]

class EmpoweredEight(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is an 8."""
    name = "Empowered Eight"
    description = "Double the chips and multiplier for cards with rank 8"
    target_ranks = ["8"]

class EmpoweredNine(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 9."""
    name = "Empowered Nine"
    description = "Double the chips and multiplier for cards with rank 9"
    target_ranks = ["9"]

class EmpoweredTen(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a 10."""
    name = "Empowered Ten"
    description = "Double the chips and multiplier for cards with rank 10"
    target_ranks = ["10"]

class EmpoweredJack(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a J."""
    name = "Empowered Jack"
    description = "Double the chips and multiplier for cards with rank J"
    target_ranks = ["J"]

class EmpoweredQueen(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a Q."""
    name = "Empowered Queen"
    description = "Double the chips and multiplier for cards with rank Q"
    target_ranks = ["Q"]

class EmpoweredKing(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a K."""
    name = "Empowered King"
    description = "Double the chips and multiplier for cards with rank K"
    target_ranks = ["K"]

class EmpoweredAce(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is an A."""
    name = "Empowered Ace"
    description = "Double the chips and multiplier for cards with rank A"
    target_ranks = ["A"]

class EvenSteven(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is an even number."""
    name = "Even Steven"
    description = "Double the chips and multiplier for cards with even rank (2 4 6 8 10)"
    target_ranks = ["2", "4", "6", "8", "10"]

class Oddity(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is an odd number."""
    name = "Oddity"
    description = "Double the chips and multiplier for cards with odd rank (1 3 5 7 9)"
    target_ranks = ["1", "3", "5", "7", "9"]

class Fibonacci(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a Fibonacci number."""
    name = "Fibonacci"
    description = "Double the chips and multiplier for cards with Fibonacci rank (1 2 3 5 8)"
    target_ranks = ["1", "2", "3", "5", "8"]

class Populism(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a non-figure rank."""
    name = "Populism"
    description = "Double the chips and multiplier for cards with non-figure rank (1 to 10)"
    target_ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

class Monarchy(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a Queen or a King."""
    name = "Monarchy"
    description = "Double the chips and multiplier for cards with figure rank (Q K)"
    target_ranks = ["Q", "K"]

class RoyalCourt(PowerRankJoker):
    """A joker that duplicates the chips and multiplier of a card if its rank is a Jack, a Queen or a King."""
    name = "Royal Court"
    description = "Double the chips and multiplier for cards with figure rank (J Q K)"
    target_ranks = ["J", "Q", "K"]
