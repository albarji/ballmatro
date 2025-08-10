"""Jokers that change the played cards"""

from typing import List
from ballmatro.card import Card
from ballmatro.jokers.joker import Joker

class BannedRankJoker(Joker):
    """Abstract Joker that removes from the played cards all those that belong to a specific rank."""
    target_ranks: List[str]
    
    def played_cards_callback(self, played_cards: list[Card]) -> list[Card]:
        return [card for card in played_cards if card.rank not in self.target_ranks]

class BannedTwo(BannedRankJoker):
    """A joker that removes all rank 2 cards from the list of played cards"""
    name = "Banned Two"
    description = "Played cards with rank 2 will be ignored in poker hand determination and scoring"
    target_ranks = ["2"]

class BannedThree(BannedRankJoker):
    """A joker that removes all rank 3 cards from the list of played cards"""
    name = "Banned Three"
    description = "Played cards with rank 3 will be ignored in poker hand determination and scoring"
    target_ranks = ["3"]

class BannedFour(BannedRankJoker):
    """A joker that removes all rank 4 cards from the list of played cards"""
    name = "Banned Four"
    description = "Played cards with rank 4 will be ignored in poker hand determination and scoring"
    target_ranks = ["4"]

class BannedFive(BannedRankJoker):
    """A joker that removes all rank 5 cards from the list of played cards"""
    name = "Banned Five"
    description = "Played cards with rank 5 will be ignored in poker hand determination and scoring"
    target_ranks = ["5"]

class BannedSix(BannedRankJoker):
    """A joker that removes all rank 6 cards from the list of played cards"""
    name = "Banned Six"
    description = "Played cards with rank 6 will be ignored in poker hand determination and scoring"
    target_ranks = ["6"]

class BannedSeven(BannedRankJoker):
    """A joker that removes all rank 7 cards from the list of played cards"""
    name = "Banned Seven"
    description = "Played cards with rank 7 will be ignored in poker hand determination and scoring"
    target_ranks = ["7"]

class BannedEight(BannedRankJoker):
    """A joker that removes all rank 8 cards from the list of played cards"""
    name = "Banned Eight"
    description = "Played cards with rank 8 will be ignored in poker hand determination and scoring"
    target_ranks = ["8"]

class BannedNine(BannedRankJoker):
    """A joker that removes all rank 9 cards from the list of played cards"""
    name = "Banned Nine"
    description = "Played cards with rank 9 will be ignored in poker hand determination and scoring"
    target_ranks = ["9"]

class BannedTen(BannedRankJoker):
    """A joker that removes all rank 10 cards from the list of played cards"""
    name = "Banned Ten"
    description = "Played cards with rank 10 will be ignored in poker hand determination and scoring"
    target_ranks = ["10"]

class BannedJack(BannedRankJoker):
    """A joker that removes all rank J cards from the list of played cards"""
    name = "Banned Jack"
    description = "Played cards with rank J will be ignored in poker hand determination and scoring"
    target_ranks = ["J"]

class BannedQueen(BannedRankJoker):
    """A joker that removes all rank Q cards from the list of played cards"""
    name = "Banned Queen"
    description = "Played cards with rank Q will be ignored in poker hand determination and scoring"
    target_ranks = ["Q"]

class BannedKing(BannedRankJoker):
    """A joker that removes all rank K cards from the list of played cards"""
    name = "Banned King"
    description = "Played cards with rank K will be ignored in poker hand determination and scoring"
    target_ranks = ["K"]

class BannedAce(BannedRankJoker):
    """A joker that removes all rank A cards from the list of played cards"""
    name = "Banned Ace"
    description = "Played cards with rank A will be ignored in poker hand determination and scoring"
    target_ranks = ["A"]

class Republic(BannedRankJoker):
    """A joker that removes all rank Q and K cards from the list of played cards"""
    name = "Republic"
    description = "Played cards with rank Q and K will be ignored in poker hand determination and scoring"
    target_ranks = ["Q", "K"]

class LandOfNumbers(BannedRankJoker):
    """A joker that removes all non-numbered rank cards from the list of played cards"""
    name = "Land Of Numbers"
    description = "Played cards with rank J, Q, K, and A will be ignored in poker hand determination and scoring"
    target_ranks = ["J", "Q", "K", "A"]

class LandOfLetters(BannedRankJoker):
    """A joker that removes all numbered rank cards from the list of played cards"""
    name = "Land Of Letters"
    description = "Played cards with rank 2 to 10 will be ignored in poker hand determination and scoring"
    target_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

class BannedSuitJoker(Joker):
    """Abstract Joker that removes from the played cards all those that belong to a specific suit."""
    target_suits: List[str]

    def played_cards_callback(self, played_cards: list[Card]) -> list[Card]:
        return [card for card in played_cards if card.suit not in self.target_suits]

class BannedClub(BannedSuitJoker):
    """A joker that removes all club cards from the list of played cards"""
    name = "Banned Club"
    description = "Played cards of club suit will be ignored in poker hand determination and scoring"
    target_suits = ["♣"]

class BannedDiamond(BannedSuitJoker):
    """A joker that removes all diamond cards from the list of played cards"""
    name = "Banned Diamond"
    description = "Played cards of diamond suit will be ignored in poker hand determination and scoring"
    target_suits = ["♦"]

class BannedSpade(BannedSuitJoker):
    """A joker that removes all spade cards from the list of played cards"""
    name = "Banned Spade"
    description = "Played cards of spade suit will be ignored in poker hand determination and scoring"
    target_suits = ["♠"]

class BannedHeart(BannedSuitJoker):
    """A joker that removes all heart cards from the list of played cards"""
    name = "Banned Heart"
    description = "Played cards of heart suit will be ignored in poker hand determination and scoring"
    target_suits = ["♥"]

class BannedRed(BannedSuitJoker):
    """A joker that removes all red cards from the list of played cards"""
    name = "Banned Red"
    description = "Played cards of red suit (♥, ♦) will be ignored in poker hand determination and scoring"
    target_suits = ["♥", "♦"]

class BannedBlack(BannedSuitJoker):
    """A joker that removes all black cards from the list of played cards"""
    name = "Banned Black"
    description = "Played cards of black suit (♣, ♠) will be ignored in poker hand determination and scoring"
    target_suits = ["♣", "♠"]
