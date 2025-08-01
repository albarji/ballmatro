import pytest
from ballmatro.jokers import planets
from ballmatro.hands import HighCard, Pair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush

"""Module for testing the planet joker cards."""
@pytest.mark.parametrize(
    "planet_cls,hand_cls,multiplier",
    [
        (planets.Pluto, HighCard, 2),
        (planets.Mercury, Pair, 2),
        (planets.Uranus, TwoPair, 2),
        (planets.Venus, ThreeOfAKind, 2),
        (planets.Saturn, Straight, 2),
        (planets.Jupiter, Flush, 2),
        (planets.Earth, FullHouse, 2),
        (planets.Mars, FourOfAKind, 2),
        (planets.Neptune, StraightFlush, 2),
        (planets.PlutoPlus, HighCard, 5),
        (planets.MercuryPlus, Pair, 5),
        (planets.UranusPlus, TwoPair, 5),
        (planets.VenusPlus, ThreeOfAKind, 5),
        (planets.SaturnPlus, Straight, 5),
        (planets.JupiterPlus, Flush, 5),
        (planets.EarthPlus, FullHouse, 5),
        (planets.MarsPlus, FourOfAKind, 5),
        (planets.NeptunePlus, StraightFlush, 5),
        (planets.PlutoPlusPlus, HighCard, 10),
        (planets.MercuryPlusPlus, Pair, 10),
        (planets.UranusPlusPlus, TwoPair, 10),
        (planets.VenusPlusPlus, ThreeOfAKind, 10),
        (planets.SaturnPlusPlus, Straight, 10),
        (planets.JupiterPlusPlus, Flush, 10),
        (planets.EarthPlusPlus, FullHouse, 10),
        (planets.MarsPlusPlus, FourOfAKind, 10),
        (planets.NeptunePlusPlus, StraightFlush, 10),
    ]
)
def test_planet_card_applies_multiplier(planet_cls, hand_cls, multiplier):
    # Create a dummy hand of the correct type
    hand = hand_cls()
    planet = planet_cls()
    modified = planet.played_hand_callback(hand)
    if isinstance(hand, planet.target_hand):
        assert modified.chips == hand.chips * multiplier
        assert modified.multiplier == hand.multiplier * multiplier
    else:
        assert modified.chips == hand.chips
        assert modified.multiplier == hand.multiplier

def test_planet_card_does_not_apply_to_other_hand_types():
    # Pluto targets HighCard, so test with Pair
    hand = Pair()
    planet = planets.Pluto()
    modified = planet.played_hand_callback(hand)
    assert modified.chips == hand.chips
    assert modified.multiplier == hand.multiplier

def test_planet_card_repr_and_attributes():
    planet = planets.MarsPlusPlus()
    assert planet.name == "Mars++"
    assert "multiplies by 10" in planet.description
    assert planet.multiplier == 10
    assert planet.target_hand == FourOfAKind
