"""Module to list all joker cards available, and a factory to create them from their names."""

from ballmatro.jokers.joker import Joker, BlankJoker
from ballmatro.jokers.planets import *

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

def find_joker(name: str) -> Joker:
    """Factory function to find Joker class by its name and return an instance of it."""
    if name in JOKER_CLASSES:
        return JOKER_CLASSES[name]()
    else:
        raise ValueError(f"Joker with name '{name}' not found.")
