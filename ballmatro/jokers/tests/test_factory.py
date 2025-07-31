"""Tests for the joker factory methods"""

import pytest

from ballmatro.jokers.factory import find_joker, BlankJoker
from ballmatro.jokers.factory import find_joker, JOKERS
from ballmatro.jokers.joker import BlankJoker

def test_find_joker_returns_instance():
    """Test that find_joker returns an instance of the Joker class."""
    for joker_class in JOKERS:
        instance = find_joker(joker_class.name)
        assert isinstance(instance, joker_class)

def test_find_joker_blankjoker():
    """Test that find_joker returns an instance of BlankJoker when requested."""
    instance = find_joker("Blank")
    assert isinstance(instance, BlankJoker)

def test_find_joker_invalid_name_raises():
    """Test that find_joker raises ValueError for an invalid joker name."""
    with pytest.raises(ValueError) as excinfo:
        find_joker("NonExistentJoker")
    assert "Joker with name 'NonExistentJoker' not found." in str(excinfo.value)
