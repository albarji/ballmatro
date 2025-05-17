from ballmatro.generators import exhaustive_generator
from ballmatro.score import ScoreInfo
from ballmatro.hands import InvalidHand

def test_exhaustive_generator_size1():
    # Use a small hand size for tractable test
    results = exhaustive_generator(1)
    # Each result is a tuple: (hand, ScoreInfo)
    assert all(isinstance(hand, list) for hand, _ in results)
    assert all(isinstance(score_info, ScoreInfo) for _, score_info in results)
    # Check that the number of generated hands matches the expected count
    # There are 4 suits, 13 ranks, 2 modifiers, so 4*13*2 = 104 possible cards
    assert len(results) == 104
    # Check no repetitions in the generated hands
    assert len({tuple(hand) for hand, _ in results}) == len(results)
    # Check no invalid hands
    assert all(result.hand != InvalidHand for _, result in results)

def test_exhaustive_generator_size2():
    # Use a small hand size for tractable test
    results = exhaustive_generator(2)
    # Check that the number of generated hands matches the expected count
    # There are 4 suits, 13 ranks, 2 modifiers, so 4*13*2 = 104 possible cards
    # The number of combinations with replacement is C(104, 2) = (104*105)/2 = 5460
    assert len(results) == 5460
    # Check no repetitions in the generated hands
    assert len({tuple(hand) for hand, _ in results}) == len(results)
    # Check no invalid hands
    assert all(result.hand != InvalidHand for _, result in results)
