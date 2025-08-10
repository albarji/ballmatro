"""Tests for the test boosters in the jokers module."""

import pytest
from ballmatro.card import Card

from ballmatro.jokers.playedchangers import BannedTwo, BannedThree, BannedFour, BannedFive, BannedSix, BannedSeven, BannedEight, BannedNine, BannedTen, BannedJack, BannedQueen, BannedKing, BannedAce
from ballmatro.jokers.playedchangers import Republic, LandOfNumbers, LandOfLetters
from ballmatro.jokers.playedchangers import BannedClub, BannedDiamond, BannedSpade, BannedHeart
from ballmatro.jokers.playedchangers import BannedRed, BannedBlack

@pytest.mark.parametrize("joker_cls, rank, other_rank", [
    (BannedTwo, "2", "3"),
    (BannedThree, "3", "4"),
    (BannedFour, "4", "5"),
    (BannedFive, "5", "6"),
    (BannedSix, "6", "7"),
    (BannedSeven, "7", "8"),
    (BannedEight, "8", "9"),
    (BannedNine, "9", "10"),
    (BannedTen, "10", "J"),
    (BannedJack, "J", "Q"),
    (BannedQueen, "Q", "K"),
    (BannedKing, "K", "A"),
    (BannedAce, "A", "2"),
])
def test_banned_joker_on_target_rank(joker_cls, rank, other_rank):
    joker = joker_cls()
    cards = [Card(f"{rank}♠"), Card(f"{rank}♦"), Card(f"{rank}♥"), Card(f"{rank}♣"), Card(f"{other_rank}♣")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card(f"{other_rank}♣")]

def test_republic():
    joker = Republic()
    cards = [Card("K♠"), Card("Q♦"), Card("2♥")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card("2♥")]

def test_land_of_numbers():
    joker = LandOfNumbers()
    cards = [Card("K♠"), Card("Q♦"), Card("J♦"), Card("2♥"), Card("7♥")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card("2♥"), Card("7♥")]

def test_land_of_letters():
    joker = LandOfLetters()
    cards = [Card("K♠"), Card("Q♦"), Card("J♦"), Card("2♥"), Card("7♥")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card("K♠"), Card("Q♦"), Card("J♦")]

@pytest.mark.parametrize("joker_cls, suit, other_suit", [
    (BannedClub, "♣", "♠"),
    (BannedDiamond, "♦", "♣"),
    (BannedSpade, "♠", "♦"),
    (BannedHeart, "♥", "♠"),
])
def test_banned_joker_on_target_suit(joker_cls, suit, other_suit):
    joker = joker_cls()
    cards = [Card(f"2{suit}"), Card(f"3{suit}"), Card(f"4{suit}"), Card(f"5{suit}"), Card(f"6{other_suit}")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card(f"6{other_suit}")]

def test_banned_red():
    joker = BannedRed()
    cards = [Card("K♠"), Card("Q♦"), Card("J♦"), Card("2♥"), Card("7♥"), Card("Q♣")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card("K♠"), Card("Q♣")]

def test_banned_black():
    joker = BannedBlack()
    cards = [Card("K♠"), Card("Q♦"), Card("J♦"), Card("2♥"), Card("7♥"), Card("Q♣")]
    newcards = joker.played_cards_callback(cards)
    assert newcards == [Card("Q♦"), Card("J♦"), Card("2♥"), Card("7♥")]
