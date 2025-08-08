"""Tests for the rank boosters in the jokers module."""

import pytest
from ballmatro.card import Card

from ballmatro.jokers.rankboosters import (
    DerankedTwo, DerankedThree, DerankedFour, DerankedFive,
    DerankedSix, DerankedSeven, DerankedEight, DerankedNine, DerankedTen,
    DerankedJack, DerankedQueen, DerankedKing, DerankedAce
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
