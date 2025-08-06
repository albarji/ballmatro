"""Tests for the Joker class"""

from ballmatro.jokers.joker import BlankJoker
from ballmatro.card import Card

def test_joker_to_card():
    """Test the to_card method of the Joker class"""
    joker = BlankJoker()
    card = joker.to_card()
    assert isinstance(card, Card), "to_card should return a Card instance"
    assert card.txt == "🂿Blank: Does nothing at all", "Card name should match the joker's name and description"
    assert card.is_joker, "Card should be identified as a joker"
    assert card.joker_name == "Blank", "Card joker name should match the joker's name"
    assert card.joker_rule == "Does nothing at all", "Card joker rule should match the joker's description"
