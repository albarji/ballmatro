"""Module to list all joker cards available, and a factory to create them from their names."""

from ballmatro.card import Card
from ballmatro.jokers.joker import Joker, BlankJoker
from ballmatro.jokers.planets import Pluto, Mercury, Uranus, Venus, Saturn, Jupiter, Earth, Mars, Neptune
from ballmatro.jokers.planets import PlutoPlus, MercuryPlus, UranusPlus, VenusPlus, SaturnPlus, JupiterPlus, MarsPlus, NeptunePlus, EarthPlus
from ballmatro.jokers.planets import MarsPlusPlus, VenusPlusPlus, JupiterPlusPlus, SaturnPlusPlus, UranusPlusPlus, MercuryPlusPlus, PlutoPlusPlus, EarthPlusPlus, NeptunePlusPlus
from ballmatro.jokers.planets import PlutoShard, MercuryShard, UranusShard, VenusShard, SaturnShard, JupiterShard, EarthShard, MarsShard, NeptuneShard
from ballmatro.jokers.planets import BarrenPluto, BarrenMercury, BarrenUranus, BarrenVenus, BarrenSaturn, BarrenJupiter, BarrenEarth, BarrenMars, BarrenNeptune 
from ballmatro.jokers.rankboosters import DerankedTwo, DerankedThree, DerankedFour, DerankedFive, DerankedSix, DerankedSeven, DerankedEight, DerankedNine, DerankedTen, DerankedJack, DerankedQueen, DerankedKing, DerankedAce
from ballmatro.jokers.rankboosters import EmpoweredTwo, EmpoweredThree, EmpoweredFour, EmpoweredFive, EmpoweredSix, EmpoweredSeven, EmpoweredEight, EmpoweredNine, EmpoweredTen, EmpoweredJack, EmpoweredQueen, EmpoweredKing, EmpoweredAce
from ballmatro.jokers.rankboosters import EvenSteven, Oddity, Fibonacci, Populism, Monarchy, RoyalCourt
from ballmatro.jokers.suitboosters import DesuitedClub, DesuitedDiamond, DesuitedSpade, DesuitedHeart
from ballmatro.jokers.suitboosters import EmpoweredClub, EmpoweredDiamond, EmpoweredSpade, EmpoweredHeart
from ballmatro.jokers.suitboosters import RedEmpire, BlackEmpire
from ballmatro.jokers.playedchangers import BannedTwo, BannedThree, BannedFour, BannedFive, BannedSix, BannedSeven, BannedEight, BannedNine, BannedTen, BannedJack, BannedQueen, BannedKing, BannedAce
from ballmatro.jokers.playedchangers import Republic, LandOfNumbers, LandOfLetters
from ballmatro.jokers.playedchangers import BannedClub, BannedDiamond, BannedSpade, BannedHeart
from ballmatro.jokers.playedchangers import BannedRed, BannedBlack

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
    NeptuneShard,       # 036
    BarrenPluto,        # 037
    BarrenMercury,      # 038
    BarrenUranus,       # 039
    BarrenVenus,        # 040
    BarrenSaturn,       # 041
    BarrenJupiter,      # 042
    BarrenEarth,        # 043
    BarrenMars,         # 044
    BarrenNeptune,      # 045
    DerankedTwo,        # 046
    DerankedThree,      # 047
    DerankedFour,       # 048
    DerankedFive,       # 049
    DerankedSix,        # 050
    DerankedSeven,      # 051
    DerankedEight,      # 052
    DerankedNine,       # 053
    DerankedTen,        # 054
    DerankedJack,       # 055
    DerankedQueen,      # 056
    DerankedKing,       # 057
    DerankedAce,        # 058
    EmpoweredTwo,       # 059
    EmpoweredThree,     # 060
    EmpoweredFour,      # 061
    EmpoweredFive,      # 062
    EmpoweredSix,       # 063
    EmpoweredSeven,     # 064
    EmpoweredEight,     # 065
    EmpoweredNine,      # 066
    EmpoweredTen,       # 067
    EmpoweredJack,      # 068
    EmpoweredQueen,     # 069
    EmpoweredKing,      # 070
    EmpoweredAce,       # 071
    EvenSteven,         # 072
    Oddity,             # 073
    Fibonacci,          # 074
    Populism,           # 075
    Monarchy,           # 076
    RoyalCourt,         # 077
    DesuitedClub,       # 078
    DesuitedDiamond,    # 079
    DesuitedHeart,      # 080
    DesuitedSpade,      # 081
    EmpoweredClub,      # 082
    EmpoweredDiamond,   # 083
    EmpoweredSpade,     # 084
    EmpoweredHeart,     # 085
    RedEmpire,          # 086
    BlackEmpire,        # 087
    BannedTwo,          # 088
    BannedThree,        # 089
    BannedFour,         # 090
    BannedFive,         # 091
    BannedSix,          # 092
    BannedSeven,        # 093
    BannedEight,        # 094
    BannedNine,         # 095
    BannedTen,          # 096
    BannedJack,         # 097
    BannedQueen,        # 098
    BannedKing,         # 099
    BannedAce,          # 100
    Republic,           # 101
    LandOfLetters,      # 102
    LandOfNumbers,      # 103
    BannedClub,         # 104
    BannedDiamond,      # 105
    BannedSpade,        # 106
    BannedHeart,        # 107
    BannedRed,          # 108
    BannedBlack,        # 109
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
