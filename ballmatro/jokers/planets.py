"""Planet cards: jokers that modify the values of hands"""

from copy import deepcopy

from ballmatro.hands import PokerHand, HighCard, Pair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush
from ballmatro.jokers.joker import Joker

class PlanetCard(Joker):
    """Base class for planet cards that modify the value of hands.
    
    Each planet card modifies the value of a hand by applying an addition and product to the chips and multiplier of the hand,
    in the form:
        hand.chips = hand.chips * product + addition.
        hand.multiplier = hand.multiplier * product + addition.

    """
    target_hand: PokerHand
    product: int = 2  # Default product for planet cards
    adder: int = 0  # Default addition for planet cards

    def played_hand_callback(self, hand: PokerHand) -> PokerHand:
        """Callback that modifies the played hand when this planet card is present."""
        if isinstance(hand, self.target_hand):
            hand = deepcopy(hand)
            hand.chips = hand.chips * self.product + self.adder
            hand.multiplier = hand.multiplier * self.product + self.adder
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
    product = 5

class MercuryPlus(PlanetCard):
    """Mercury+: multiplies by 5 the chips and multiplier of the Pair hand"""
    name = "Mercury+"
    description = "Multiplies by 5 the chips and multiplier of the Pair hand"
    target_hand = Pair
    product = 5

class UranusPlus(PlanetCard):
    """Uranus+: multiplies by 5 the chips and multiplier of the Two Pair hand"""
    name = "Uranus+"
    description = "Multiplies by 5 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    product = 5

class VenusPlus(PlanetCard):
    """Venus+: multiplies by 5 the chips and multiplier of the Three of a Kind hand"""
    name = "Venus+"
    description = "Multiplies by 5 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    product = 5

class SaturnPlus(PlanetCard):
    """Saturn+: multiplies by 5 the chips and multiplier of the Straight hand"""
    name = "Saturn+"
    description = "Multiplies by 5 the chips and multiplier of the Straight hand"
    target_hand = Straight
    product = 5

class JupiterPlus(PlanetCard):
    """Jupiter+: multiplies by 5 the chips and multiplier of the Flush hand"""
    name = "Jupiter+"
    description = "Multiplies by 5 the chips and multiplier of the Flush hand"
    target_hand = Flush
    product = 5

class EarthPlus(PlanetCard):
    """Earth+: multiplies by 5 the chips and multiplier of the Full House hand"""
    name = "Earth+"
    description = "Multiplies by 5 the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    product = 5

class MarsPlus(PlanetCard):
    """Mars+: multiplies by 5 the chips and multiplier of the Four of a Kind hand"""
    name = "Mars+"
    description = "Multiplies by 5 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    product = 5

class NeptunePlus(PlanetCard):
    """Neptune+: multiplies by 5 the chips and multiplier of the Straight Flush hand"""
    name = "Neptune+"
    description = "Multiplies by 5 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    product = 5

class PlutoPlusPlus(PlanetCard):
    """Pluto++: multiplies by 10 the chips and multiplier of the High Card hand"""
    name = "Pluto++"
    description = "Multiplies by 10 the chips and multiplier of the High Card hand"
    target_hand = HighCard
    product = 10

class MercuryPlusPlus(PlanetCard):
    """Mercury++: multiplies by 10 the chips and multiplier of the Pair hand"""
    name = "Mercury++"
    description = "Multiplies by 10 the chips and multiplier of the Pair hand"
    target_hand = Pair
    product = 10

class UranusPlusPlus(PlanetCard):
    """Uranus++: multiplies by 10 the chips and multiplier of the Two Pair hand"""
    name = "Uranus++"
    description = "Multiplies by 10 the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    product = 10

class VenusPlusPlus(PlanetCard):
    """Venus++: multiplies by 10 the chips and multiplier of the Three of a Kind hand"""
    name = "Venus++"
    description = "Multiplies by 10 the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    product = 10

class SaturnPlusPlus(PlanetCard):
    """Saturn++: multiplies by 10 the chips and multiplier of the Straight hand"""
    name = "Saturn++"
    description = "Multiplies by 10 the chips and multiplier of the Straight hand"
    target_hand = Straight
    product = 10

class JupiterPlusPlus(PlanetCard):
    """Jupiter++: multiplies by 10 the chips and multiplier of the Flush hand"""
    name = "Jupiter++"
    description = "Multiplies by 10 the chips and multiplier of the Flush hand"
    target_hand = Flush
    product = 10

class EarthPlusPlus(PlanetCard):
    """Earth++: multiplies by 10 the chips and multiplier of the Full House hand"""
    name = "Earth++"
    description = "Multiplies by 10 the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    product = 10

class MarsPlusPlus(PlanetCard):
    """Mars++: multiplies by 10 the chips and multiplier of the Four of a Kind hand"""
    name = "Mars++"
    description = "Multiplies by 10 the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    product = 10

class NeptunePlusPlus(PlanetCard):
    """Neptune++: multiplies by 10 the chips and multiplier of the Straight Flush hand"""
    name = "Neptune++"
    description = "Multiplies by 10 the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    product = 10

class PlutoShard(PlanetCard):
    """Pluto Shard: adds 1 to the chips and multiplier of the High Card hand"""
    name = "Pluto Shard"
    description = "Adds 1 to the chips and multiplier of the High Card hand"
    target_hand = HighCard
    product = 1
    adder = 1

class MercuryShard(PlanetCard):
    """Mercury Shard: adds 1 to the chips and multiplier of the Pair hand"""
    name = "Mercury Shard"
    description = "Adds 1 to the chips and multiplier of the Pair hand"
    target_hand = Pair
    product = 1
    adder = 1

class UranusShard(PlanetCard):
    """Uranus Shard: adds 1 to the chips and multiplier of the Two Pair hand"""
    name = "Uranus Shard"
    description = "Adds 1 to the chips and multiplier of the Two Pair hand"
    target_hand = TwoPair
    product = 1
    adder = 1

class VenusShard(PlanetCard):
    """Venus Shard: adds 1 to the chips and multiplier of the Three of a Kind hand"""
    name = "Venus Shard"
    description = "Adds 1 to the chips and multiplier of the Three of a Kind hand"
    target_hand = ThreeOfAKind
    product = 1
    adder = 1

class SaturnShard(PlanetCard):
    """Saturn Shard: adds 1 to the chips and multiplier of the Straight hand"""
    name = "Saturn Shard"
    description = "Adds 1 to the chips and multiplier of the Straight hand"
    target_hand = Straight
    product = 1
    adder = 1

class JupiterShard(PlanetCard):
    """Jupiter Shard: adds 1 to the chips and multiplier of the Flush hand"""
    name = "Jupiter Shard"
    description = "Adds 1 to the chips and multiplier of the Flush hand"
    target_hand = Flush
    product = 1
    adder = 1

class EarthShard(PlanetCard):
    """Earth Shard: adds 1 to the chips and multiplier of the Full House hand"""
    name = "Earth Shard"
    description = "Adds 1 to the chips and multiplier of the Full House hand"
    target_hand = FullHouse
    product = 1
    adder = 1

class MarsShard(PlanetCard):
    """Mars Shard: adds 1 to the chips and multiplier of the Four of a Kind hand"""
    name = "Mars Shard"
    description = "Adds 1 to the chips and multiplier of the Four of a Kind hand"
    target_hand = FourOfAKind
    product = 1
    adder = 1

class NeptuneShard(PlanetCard):
    """Neptune Shard: adds 1 to the chips and multiplier of the Straight Flush hand"""
    name = "Neptune Shard"
    description = "Adds 1 to the chips and multiplier of the Straight Flush hand"
    target_hand = StraightFlush
    product = 1
    adder = 1

class BarrenPluto(PlanetCard):
    """Barren Pluto: sets the chips and multiplier of the High Card hand to 1"""
    name = "Barren Pluto"
    description = "Sets the chips and multiplier of the High Card hand to 1"
    target_hand = HighCard
    product = 0
    adder = 1

class BarrenMercury(PlanetCard):
    """Barren Mercury: sets the chips and multiplier of the Pair hand to 1"""
    name = "Barren Mercury"
    description = "Sets the chips and multiplier of the Pair hand to 1"
    target_hand = Pair
    product = 0
    adder = 1

class BarrenUranus(PlanetCard):
    """Barren Uranus: sets the chips and multiplier of the Two Pair hand to 1"""
    name = "Barren Uranus"
    description = "Sets the chips and multiplier of the Two Pair hand to 1"
    target_hand = TwoPair
    product = 0
    adder = 1

class BarrenVenus(PlanetCard):
    """Barren Venus: sets the chips and multiplier of the Three of a Kind hand to 1"""
    name = "Barren Venus"
    description = "Sets the chips and multiplier of the Three of a Kind hand to 1"
    target_hand = ThreeOfAKind
    product = 0 
    adder = 1

class BarrenSaturn(PlanetCard):
    """Barren Saturn: sets the chips and multiplier of the Straight hand to 1"""
    name = "Barren Saturn"
    description = "Sets the chips and multiplier of the Straight hand to 1"
    target_hand = Straight
    product = 0
    adder = 1

class BarrenJupiter(PlanetCard):
    """Barren Jupiter: sets the chips and multiplier of the Flush hand to 1"""
    name = "Barren Jupiter"
    description = "Sets the chips and multiplier of the Flush hand to 1"
    target_hand = Flush
    product = 0
    adder = 1

class BarrenEarth(PlanetCard):
    """Barren Earth: sets the chips and multiplier of the Full House hand to 1"""
    name = "Barren Earth"
    description = "Sets the chips and multiplier of the Full House hand to 1"
    target_hand = FullHouse
    product = 0
    adder = 1

class BarrenMars(PlanetCard):
    """Barren Mars: sets the chips and multiplier of the Four of a Kind hand to 1"""
    name = "Barren Mars"
    description = "Sets the chips and multiplier of the Four of a Kind hand to 1"
    target_hand = FourOfAKind
    product = 0
    adder = 1

class BarrenNeptune(PlanetCard):
    """Barren Neptune: sets the chips and multiplier of the Straight Flush hand to 1"""
    name = "Barren Neptune"
    description = "Sets the chips and multiplier of the Straight Flush hand to 1"
    target_hand = StraightFlush
    product = 0
    adder = 1
