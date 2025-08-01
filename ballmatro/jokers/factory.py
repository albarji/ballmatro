"""Module to list all joker cards available, and a factory to create them from their names."""

from ballmatro.card import Card
from ballmatro.jokers.joker import Joker, BlankJoker
from ballmatro.jokers.planets import Pluto, Mercury, Uranus, Venus, Saturn, Jupiter, Mars, Neptune, Earth
from ballmatro.jokers.planets import PlutoPlus, MercuryPlus, UranusPlus, VenusPlus, SaturnPlus, JupiterPlus, MarsPlus, NeptunePlus, EarthPlus
from ballmatro.jokers.planets import MarsPlusPlus, VenusPlusPlus, JupiterPlusPlus, SaturnPlusPlus, UranusPlusPlus, MercuryPlusPlus, PlutoPlusPlus, EarthPlusPlus, NeptunePlusPlus

JOKERS = [
    BlankJoker,
    Pluto,
    Mercury,
    Uranus,
    Venus,
    Saturn,
    Jupiter,
    Mars,
    Neptune,
    Earth,
    PlutoPlus,
    MercuryPlus,
    UranusPlus,
    VenusPlus,
    SaturnPlus,
    JupiterPlus,
    MarsPlus,
    NeptunePlus,
    EarthPlus,
    MarsPlusPlus,
    VenusPlusPlus,
    JupiterPlusPlus,
    SaturnPlusPlus,
    UranusPlusPlus,
    MercuryPlusPlus,
    PlutoPlusPlus,
    EarthPlusPlus,
    NeptunePlusPlus,
]

# Dictionary from joker names to their classes
JOKER_CLASSES = {joker.name: joker for joker in JOKERS}

def find_joker_name(name: str) -> Joker:
    """Factory function to find Joker class by its name and return an instance of it."""
    if name in JOKER_CLASSES:
        return JOKER_CLASSES[name]()
    else:
        raise ValueError(f"Joker with name '{name}' not found.")


def find_joker_card(card: Card) -> Joker:
    """Factory function to find Joker class by its associated card and return an instance of it."""
    return find_joker_name(card.joker_name)
