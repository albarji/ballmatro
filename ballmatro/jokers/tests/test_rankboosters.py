"""Tests for the rank boosters in the jokers module."""

import pytest
from ballmatro.card import Card

from ballmatro.jokers.rankboosters import (
    DerankedTwo, DerankedThree, DerankedFour, DerankedFive,
    DerankedSix, DerankedSeven, DerankedEight, DerankedNine, DerankedTen,
    DerankedJack, DerankedQueen, DerankedKing, DerankedAce,
    EmpoweredTwo, EmpoweredThree, EmpoweredFour, EmpoweredFive,
    EmpoweredSix, EmpoweredSeven, EmpoweredEight, EmpoweredNine, EmpoweredTen,
    EmpoweredJack, EmpoweredQueen, EmpoweredKing, EmpoweredAce,
    EvenSteven, Oddity, Fibonacci, Populism, Monarchy, RoyalCourt
)

@pytest.mark.parametrize("joker_cls, rank", [
    (DerankedTwo, "2"),
    (DerankedThree, "3"),
    (DerankedFour, "4"),
    (DerankedFive, "5"),
    (DerankedSix, "6"),
    (DerankedSeven, "7"),
    (DerankedEight, "8"),
    (DerankedNine, "9"),
    (DerankedTen, "10"),
    (DerankedJack, "J"),
    (DerankedQueen, "Q"),
    (DerankedKing, "K"),
    (DerankedAce, "A"),
])
def test_deranked_joker_on_target_rank(joker_cls, rank):
    joker = joker_cls()
    card = Card(f"{rank}♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 1
    assert multiplier == 0

@pytest.mark.parametrize("joker_cls, target_rank, other_rank", [
    (DerankedTwo, "2", "3"),
    (DerankedThree, "3", "4"),
    (DerankedFour, "4", "5"),
    (DerankedFive, "5", "6"),
    (DerankedSix, "6", "7"),
    (DerankedSeven, "7", "8"),
    (DerankedEight, "8", "9"),
    (DerankedNine, "9", "10"),
    (DerankedTen, "10", "J"),
    (DerankedJack, "J", "Q"),
    (DerankedQueen, "Q", "K"),
    (DerankedKing, "K", "A"),
    (DerankedAce, "A", "2"),
])
def test_deranked_joker_on_other_rank(joker_cls, target_rank, other_rank):
    joker = joker_cls()
    card = Card(f"{other_rank}♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 3
    assert multiplier == 4

@pytest.mark.parametrize("joker_cls, rank", [
    (EmpoweredTwo, "2"),
    (EmpoweredThree, "3"),
    (EmpoweredFour, "4"),
    (EmpoweredFive, "5"),
    (EmpoweredSix, "6"),
    (EmpoweredSeven, "7"),
    (EmpoweredEight, "8"),
    (EmpoweredNine, "9"),
    (EmpoweredTen, "10"),
    (EmpoweredJack, "J"),
    (EmpoweredQueen, "Q"),
    (EmpoweredKing, "K"),
    (EmpoweredAce, "A"),
])
def test_empowered_ranks_on_target_rank(joker_cls, rank):
    joker = joker_cls()
    card = Card(f"{rank}♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 6
    assert multiplier == 8

@pytest.mark.parametrize("joker_cls, target_rank, other_rank", [
    (EmpoweredTwo, "2", "3"),
    (EmpoweredThree, "3", "4"),
    (EmpoweredFour, "4", "5"),
    (EmpoweredFive, "5", "6"),
    (EmpoweredSix, "6", "7"),
    (EmpoweredSeven, "7", "8"),
    (EmpoweredEight, "8", "9"),
    (EmpoweredNine, "9", "10"),
    (EmpoweredTen, "10", "J"),
    (EmpoweredJack, "J", "Q"),
    (EmpoweredQueen, "Q", "K"),
    (EmpoweredKing, "K", "A"),
    (EmpoweredAce, "A", "2"),
])
def test_empowered_ranks_on_other_rank(joker_cls, target_rank, other_rank):
    joker = joker_cls()
    card = Card(f"{other_rank}♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 3
    assert multiplier == 4

def test_even_steven():
    joker = EvenSteven()
    card = Card("2♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 6
    assert multiplier == 8
    card = Card("3♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 3
    assert multiplier == 4

def test_oddity():
    joker = Oddity()
    card = Card("3♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 6
    assert multiplier == 8
    card = Card("4♠")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 3
    assert multiplier == 4

def test_fibonacci():
    joker = Fibonacci()
    for i in [2, 3, 5, 8]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 6
        assert multiplier == 8
    for i in [4, 6, 7, 9, 10]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 3
        assert multiplier == 4

def test_populism():
    joker = Populism()
    for i in range(2, 11):
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 6
        assert multiplier == 8
    for i in ["J", "Q", "K", "A"]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 3
        assert multiplier == 4

def test_monarchy():
    joker = Monarchy()
    for i in ["Q", "K"]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 6
        assert multiplier == 8
    for i in list(range(2, 11)) + ["J", "A"]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 3
        assert multiplier == 4

def test_royal_court():
    joker = RoyalCourt()
    for i in ["J", "Q", "K"]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 6
        assert multiplier == 8
    for i in list(range(2, 11)) + ["A"]:
        card = Card(f"{i}♠")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 3
        assert multiplier == 4
