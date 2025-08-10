"""Tests for the test boosters in the jokers module."""

import pytest
from ballmatro.card import Card

from ballmatro.jokers.suitboosters import (
    DesuitedClub, DesuitedDiamond, DesuitedSpade, DesuitedHeart,
    EmpoweredClub, EmpoweredDiamond, EmpoweredSpade, EmpoweredHeart,
    RedEmpire, BlackEmpire
)

@pytest.mark.parametrize("joker_cls, suit", [
    (DesuitedClub, "♣"),
    (DesuitedDiamond, "♦"),
    (DesuitedSpade, "♠"),
    (DesuitedHeart, "♥"),
])
def test_desuited_joker_on_target_suit(joker_cls, suit):
    joker = joker_cls()
    card = Card(f"2{suit}")
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 1
    assert multiplier == 0

@pytest.mark.parametrize("joker_cls, target_suit, other_suit", [
    (DesuitedClub, "♣", "♦"),
    (DesuitedDiamond, "♦", "♠"),
    (DesuitedSpade, "♠", "♥"),
    (DesuitedHeart, "♥", "♣"),
])
def test_desuited_joker_on_other_suit(joker_cls, target_suit, other_suit):
    joker = joker_cls()
    card = Card(f"2{other_suit}")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 3
    assert multiplier == 4

@pytest.mark.parametrize("joker_cls, suit", [
    (EmpoweredClub, "♣"),
    (EmpoweredDiamond, "♦"),
    (EmpoweredSpade, "♠"),
    (EmpoweredHeart, "♥"),
])
def test_empowered_suits_on_target_rank(joker_cls, suit):
    joker = joker_cls()
    card = Card(f"2{suit}")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 6
    assert multiplier == 8

@pytest.mark.parametrize("joker_cls, target_suit, other_suit", [
    (EmpoweredClub, "♣", "♦"),
    (EmpoweredDiamond, "♦", "♠"),
    (EmpoweredSpade, "♠", "♥"),
    (EmpoweredHeart, "♥", "♣"),
])
def test_empowered_suits_on_other_suit(joker_cls, target_suit, other_suit):
    joker = joker_cls()
    card = Card(f"2{other_suit}")  # Using a suit to create a valid Card object
    chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
    assert chips == 3
    assert multiplier == 4

def test_red_empire():
    joker = RedEmpire()
    for suit in ["♦", "♥"]:
        card = Card(f"2{suit}")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 6
        assert multiplier == 8
    for suit in ["♣", "♠"]:
        card = Card(f"3{suit}")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 3
        assert multiplier == 4

def test_black_empire():
    joker = BlackEmpire()
    for suit in ["♣", "♠"]:
        card = Card(f"2{suit}")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 6
        assert multiplier == 8
    for suit in ["♦", "♥"]:
        card = Card(f"3{suit}")  # Using a suit to create a valid Card object
        chips, multiplier = joker.card_score_callback(card, chips=5, multiplier=2, added_chips=3, added_multiplier=4)
        assert chips == 3
        assert multiplier == 4
