"""Module to list all joker cards available, and a factory to create them from their names."""

from ballmatro.card import Card
from ballmatro.jokers.joker import Joker, BlankJoker
from ballmatro.jokers.planets import Pluto, Mercury, Uranus, Venus, Saturn, Jupiter, Earth, Mars, Neptune
from ballmatro.jokers.planets import PlutoPlus, MercuryPlus, UranusPlus, VenusPlus, SaturnPlus, JupiterPlus, MarsPlus, NeptunePlus, EarthPlus
from ballmatro.jokers.planets import MarsPlusPlus, VenusPlusPlus, JupiterPlusPlus, SaturnPlusPlus, UranusPlusPlus, MercuryPlusPlus, PlutoPlusPlus, EarthPlusPlus, NeptunePlusPlus
from ballmatro.jokers.planets import PlutoShard, MercuryShard, UranusShard, VenusShard, SaturnShard, JupiterShard, EarthShard, MarsShard, NeptuneShard

JOKERS = [
    BlankJoker,         # 000
    Pluto,              # 001
    Mercury,            # 002
    Uranus,             # 003
    Venus,              # 004
    Saturn,             # 005
    Jupiter,            # 006
    Mars,               # 007
    Neptune,            # 008
    Earth,              # 009
    PlutoPlus,          # 010
    MercuryPlus,        # 011
    UranusPlus,         # 012
    VenusPlus,          # 013
    SaturnPlus,         # 014
    JupiterPlus,        # 015
    MarsPlus,           # 016
    NeptunePlus,        # 017
    EarthPlus,          # 018
    MarsPlusPlus,       # 019
    VenusPlusPlus,      # 020
    JupiterPlusPlus,    # 021
    SaturnPlusPlus,     # 022
    UranusPlusPlus,     # 023
    MercuryPlusPlus,    # 024
    PlutoPlusPlus,      # 025
    EarthPlusPlus,      # 026
    NeptunePlusPlus,    # 027
    PlutoShard,         # 028
    MercuryShard,       # 029
    UranusShard,        # 030
    VenusShard,         # 031
    SaturnShard,        # 032
    JupiterShard,       # 033
    EarthShard,         # 034
    MarsShard,          # 035
    NeptuneShard        # 036
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
