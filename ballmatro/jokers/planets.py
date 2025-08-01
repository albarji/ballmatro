"""Planet cards: jokers that modify the values of hands"""

from copy import deepcopy

from ballmatro.hands import PokerHand, HighCard, Pair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush
from ballmatro.jokers.joker import Joker

PLANET_CARDS_MULTIPLIERS = {
    "": 2, 
    "+": 5, 
    "++": 10
}

class PlanetCard(Joker):
    """Base class for planet cards that modify the value of hands.
    
    Each planet card modifies the value of a hand by applying a multiplier to the chips and multiplier of the hand.
    """
    target_hand: PokerHand
    multiplier: int = 2  # Default multiplier for planet cards

    def played_hand_callback(self, hand: PokerHand) -> PokerHand:
        """Callback that modifies the played hand when this planet card is present."""
        if isinstance(hand, self.target_hand):
            hand = deepcopy(hand)
            hand.chips *= self.multiplier
            hand.multiplier *= self.multiplier
            return hand
        return hand

class Pluto(PlanetCard):
    """Pluto: multiplies by 2 the chips and multiplier of the High Card hand"""
    name = "Pluto"
    description = "Multiplies by 2 the chips and multiplier of the High Card hand"
    target_hand = HighCard

class Mercury(PlanetCard):
    """Mercury: multiplies by 2 the chips and multiplier of the Pair hand"""
    name = "Mercury"
    description = "Multiplies by 2 the chips and multiplier of the Pair hand"
    target_hand = Pair

class Uranus(PlanetCard):
    """Uranus: multiplies by 2 the chips and multiplier of the Two Pair hand"""
    name = "Uranus"
    description = "Multiplies by 2 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair

class Venus(PlanetCard):
    """Venus: multiplies by 2 the chips and multiplier of the Three of a Kind hand"""
    name = "Venus"
    description = "Multiplies by 2 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind

class Saturn(PlanetCard):
    """Saturn: multiplies by 2 the chips and multiplier of the Straight hand"""
    name = "Saturn"
    description = "Multiplies by 2 the chips and multiplier of the Straight hand"
    target_hand = Straight

class Jupiter(PlanetCard):
    """Jupiter: multiplies by 2 the chips and multiplier of the Flush hand"""
    name = "Jupiter"
    description = "Multiplies by 2 the chips and multiplier of the Flush hand"
    target_hand = Flush

class Earth(PlanetCard):
    """Earth: multiplies by 2 the chips and multiplier of the Full House hand"""
    name = "Earth"
    description = "Multiplies by 2 the chips and multiplier of the Full House hand"
    target_hand = FullHouse

class Mars(PlanetCard):
    """Mars: multiplies by 2 the chips and multiplier of the Four of a Kind hand"""
    name = "Mars"
    description = "Multiplies by 2 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind

class Neptune(PlanetCard):
    """Neptune: multiplies by 2 the chips and multiplier of the Straight Flush hand"""
    name = "Neptune"
    description = "Multiplies by 2 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush

class PlutoPlus(PlanetCard):
    """Pluto+: multiplies by 5 the chips and multiplier of the High Card hand"""
    name = "Pluto+"
    description = "Multiplies by 5 the chips and multiplier of the High Card hand"
    target_hand = HighCard
    multiplier = 5

class MercuryPlus(PlanetCard):
    """Mercury+: multiplies by 5 the chips and multiplier of the Pair hand"""
    name = "Mercury+"
    description = "Multiplies by 5 the chips and multiplier of the Pair hand"
    target_hand = Pair
    multiplier = 5

class UranusPlus(PlanetCard):
    """Uranus+: multiplies by 5 the chips and multiplier of the Two Pair hand"""
    name = "Uranus+"
    description = "Multiplies by 5 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    multiplier = 5

class VenusPlus(PlanetCard):
    """Venus+: multiplies by 5 the chips and multiplier of the Three of a Kind hand"""
    name = "Venus+"
    description = "Multiplies by 5 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    multiplier = 5

class SaturnPlus(PlanetCard):
    """Saturn+: multiplies by 5 the chips and multiplier of the Straight hand"""
    name = "Saturn+"
    description = "Multiplies by 5 the chips and multiplier of the Straight hand"
    target_hand = Straight
    multiplier = 5

class JupiterPlus(PlanetCard):
    """Jupiter+: multiplies by 5 the chips and multiplier of the Flush hand"""
    name = "Jupiter+"
    description = "Multiplies by 5 the chips and multiplier of the Flush hand"
    target_hand = Flush
    multiplier = 5

class EarthPlus(PlanetCard):
    """Earth+: multiplies by 5 the chips and multiplier of the Full House hand"""
    name = "Earth+"
    description = "Multiplies by 5 the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    multiplier = 5

class MarsPlus(PlanetCard):
    """Mars+: multiplies by 5 the chips and multiplier of the Four of a Kind hand"""
    name = "Mars+"
    description = "Multiplies by 5 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    multiplier = 5

class NeptunePlus(PlanetCard):
    """Neptune+: multiplies by 5 the chips and multiplier of the Straight Flush hand"""
    name = "Neptune+"
    description = "Multiplies by 5 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    multiplier = 5

class PlutoPlusPlus(PlanetCard):
    """Pluto++: multiplies by 10 the chips and multiplier of the High Card hand"""
    name = "Pluto++"
    description = "Multiplies by 10 the chips and multiplier of the High Card hand"
    target_hand = HighCard
    multiplier = 10

class MercuryPlusPlus(PlanetCard):
    """Mercury++: multiplies by 10 the chips and multiplier of the Pair hand"""
    name = "Mercury++"
    description = "Multiplies by 10 the chips and multiplier of the Pair hand"
    target_hand = Pair
    multiplier = 10

class UranusPlusPlus(PlanetCard):
    """Uranus++: multiplies by 10 the chips and multiplier of the Two Pair hand"""
    name = "Uranus++"
    description = "Multiplies by 10 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    multiplier = 10

class VenusPlusPlus(PlanetCard):
    """Venus++: multiplies by 10 the chips and multiplier of the Three of a Kind hand"""
    name = "Venus++"
    description = "Multiplies by 10 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    multiplier = 10

class SaturnPlusPlus(PlanetCard):
    """Saturn++: multiplies by 10 the chips and multiplier of the Straight hand"""
    name = "Saturn++"
    description = "Multiplies by 10 the chips and multiplier of the Straight hand"
    target_hand = Straight
    multiplier = 10

class JupiterPlusPlus(PlanetCard):
    """Jupiter++: multiplies by 10 the chips and multiplier of the Flush hand"""
    name = "Jupiter++"
    description = "Multiplies by 10 the chips and multiplier of the Flush hand"
    target_hand = Flush
    multiplier = 10

class EarthPlusPlus(PlanetCard):
    """Earth++: multiplies by 10 the chips and multiplier of the Full House hand"""
    name = "Earth++"
    description = "Multiplies by 10 the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    multiplier = 10

class MarsPlusPlus(PlanetCard):
    """Mars++: multiplies by 10 the chips and multiplier of the Four of a Kind hand"""
    name = "Mars++"
    description = "Multiplies by 10 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    multiplier = 10

class NeptunePlusPlus(PlanetCard):
    """Neptune++: multiplies by 10 the chips and multiplier of the Straight Flush hand"""
    name = "Neptune++"
    description = "Multiplies by 10 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    multiplier = 10
