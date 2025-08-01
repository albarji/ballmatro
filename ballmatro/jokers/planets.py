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
    """Pluto: High Card with a multiplier of 2"""
    name = "Pluto"
    description = "Pluto: multiplies by 2 the chips and multiplier of the High Card hand"
    target_hand = HighCard

class Mercury(PlanetCard):
    """Mercury: Pair with a multiplier of 2"""
    name = "Mercury"
    description = "Mercury: multiplies by 2 the chips and multiplier of the Pair hand"
    target_hand = Pair

class Uranus(PlanetCard):
    """Uranus: Two Pair with a multiplier of 2"""
    name = "Uranus"
    description = "Uranus: multiplies by 2 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair

class Venus(PlanetCard):
    """Venus: Three of a Kind with a multiplier of 2"""
    name = "Venus"
    description = "Venus: multiplies by 2 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind

class Saturn(PlanetCard):
    """Saturn: Straight with a multiplier of 2"""
    name = "Saturn"
    description = "Saturn: multiplies by 2 the chips and multiplier of the Straight hand"
    target_hand = Straight

class Jupiter(PlanetCard):
    """Jupiter: Flush with a multiplier of 2"""
    name = "Jupiter"
    description = "Jupiter: multiplies by 2 the chips and multiplier of the Flush hand"
    target_hand = Flush

class Earth(PlanetCard):
    """Earth: Full House with a multiplier of 2"""
    name = "Earth"
    description = "Earth: multiplies by 2 the chips and multiplier of the Full House hand"
    target_hand = FullHouse

class Mars(PlanetCard):
    """Mars: Four of a Kind with a multiplier of 2"""
    name = "Mars"
    description = "Mars: multiplies by 2 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind

class Neptune(PlanetCard):
    """Neptune: Straight Flush with a multiplier of 2"""
    name = "Neptune"
    description = "Neptune: multiplies by 2 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush

class PlutoPlus(PlanetCard):
    """Pluto+: High Card with a multiplier of 5"""
    name = "Pluto+"
    description = "Pluto+: multiplies by 5 the chips and multiplier of the High Card hand"
    target_hand = HighCard
    multiplier = 5

class MercuryPlus(PlanetCard):
    """Mercury+: Pair with a multiplier of 5"""
    name = "Mercury+"
    description = "Mercury+: multiplies by 5 the chips and multiplier of the Pair hand"
    target_hand = Pair
    multiplier = 5

class UranusPlus(PlanetCard):
    """Uranus+: Two Pair with a multiplier of 5"""
    name = "Uranus+"
    description = "Uranus+: multiplies by 5 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    multiplier = 5

class VenusPlus(PlanetCard):
    """Venus+: Three of a Kind with a multiplier of 5"""
    name = "Venus+"
    description = "Venus+: multiplies by 5 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    multiplier = 5

class SaturnPlus(PlanetCard):
    """Saturn+: Straight with a multiplier of 5"""
    name = "Saturn+"
    description = "Saturn+: multiplies by 5 the chips and multiplier of the Straight hand"
    target_hand = Straight
    multiplier = 5

class JupiterPlus(PlanetCard):
    """Jupiter+: Flush with a multiplier of 5"""
    name = "Jupiter+"
    description = "Jupiter+: multiplies by 5 the chips and multiplier of the Flush hand"
    target_hand = Flush
    multiplier = 5

class EarthPlus(PlanetCard):
    """Earth+: Full House with a multiplier of 5"""
    name = "Earth+"
    description = "Earth+: multiplies by 5 the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    multiplier = 5

class MarsPlus(PlanetCard):
    """Mars+: Four of a Kind with a multiplier of 5"""
    name = "Mars+"
    description = "Mars+: multiplies by 5 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    multiplier = 5

class NeptunePlus(PlanetCard):
    """Neptune+: Straight Flush with a multiplier of 5"""
    name = "Neptune+"
    description = "Neptune+: multiplies by 5 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    multiplier = 5

class PlutoPlusPlus(PlanetCard):
    """Pluto++: High Card with a multiplier of 10"""
    name = "Pluto++"
    description = "Pluto++: multiplies by 10 the chips and multiplier of the High Card hand"
    target_hand = HighCard
    multiplier = 10

class MercuryPlusPlus(PlanetCard):
    """Mercury++: Pair with a multiplier of 10"""
    name = "Mercury++"
    description = "Mercury++: multiplies by 10 the chips and multiplier of the Pair hand"
    target_hand = Pair
    multiplier = 10

class UranusPlusPlus(PlanetCard):
    """Uranus++: Two Pair with a multiplier of 10"""
    name = "Uranus++"
    description = "Uranus++: multiplies by 10 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    multiplier = 10

class VenusPlusPlus(PlanetCard):
    """Venus++: Three of a Kind with a multiplier of 10"""
    name = "Venus++"
    description = "Venus++: multiplies by 10 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    multiplier = 10

class SaturnPlusPlus(PlanetCard):
    """Saturn++: Straight with a multiplier of 10"""
    name = "Saturn++"
    description = "Saturn++: multiplies by 10 the chips and multiplier of the Straight hand"
    target_hand = Straight
    multiplier = 10

class JupiterPlusPlus(PlanetCard):
    """Jupiter++: Flush with a multiplier of 10"""
    name = "Jupiter++"
    description = "Jupiter++: multiplies by 10 the chips and multiplier of the Flush hand"
    target_hand = Flush
    multiplier = 10

class EarthPlusPlus(PlanetCard):
    """Earth++: Full House with a multiplier of 10"""
    name = "Earth++"
    description = "Earth++: multiplies by 10 the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    multiplier = 10

class MarsPlusPlus(PlanetCard):
    """Mars++: Four of a Kind with a multiplier of 10"""
    name = "Mars++"
    description = "Mars++: multiplies by 10 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    multiplier = 10

class NeptunePlusPlus(PlanetCard):
    """Neptune++: Straight Flush with a multiplier of 10"""
    name = "Neptune++"
    description = "Neptune++: multiplies by 10 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    multiplier = 10
