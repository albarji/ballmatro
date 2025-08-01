"""Tests for the joker factory methods"""

import pytest

from ballmatro.card import Card
from ballmatro.jokers.factory import find_joker_name, find_joker_card, JOKERS
from ballmatro.jokers.joker import BlankJoker

def test_find_joker_name_returns_instance():
    """Test that find_joker_name returns an instance of the Joker class."""
    for joker_class in JOKERS:
        instance = find_joker_name(joker_class.name)
        assert isinstance(instance, joker_class)

def test_find_joker_name_blankjoker():
    """Test that find_joker_name returns an instance of BlankJoker when requested."""
    instance = find_joker_name("Blank")
    assert isinstance(instance, BlankJoker)

def test_find_joker_card_blankjoker():
    """Test that find_joker_card returns an instance of BlankJoker when requested."""
    instance = find_joker_card(Card("🂿 Blank: Does nothing at all."))
    assert isinstance(instance, BlankJoker)

def test_find_joker_card_blankjoker_diffdesc():
    """Test that find_joker_card returns an instance of BlankJoker when requested, even if the card has a different description."""
    instance = find_joker_card(Card("🂿 Blank: something something"))
    assert isinstance(instance, BlankJoker)

def test_find_joker_name_invalid_name_raises():
    """Test that find_joker_name raises ValueError for an invalid joker name."""
    with pytest.raises(ValueError) as excinfo:
        find_joker_name("NonExistentJoker")
    assert "Joker with name 'NonExistentJoker' not found." in str(excinfo.value)
