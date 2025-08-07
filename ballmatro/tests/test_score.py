from ballmatro.card import Card
from ballmatro.hands import InvalidPlay
from ballmatro.score import Score, ScoreDataset
from datasets import Dataset

### Score Tests

def test_score_invalid_hand():
    available = [Card(txt="2♥"), Card(txt="3♦"), Card(txt="A♠")]
    played = [Card(txt="2♥"), Card(txt="A♠")]
    assert Score(available, played).score == 0

def test_score_unavailable_card():
    available = [Card(txt="2♥"), Card(txt="3♦"), Card(txt="A♠")]
    played = [Card(txt="2♥"), Card(txt="K♠")]
    assert Score(available, played).score == 0  # Card not available

def test_score_high_card():
    available = [Card(txt="2♥"), Card(txt="3♦"), Card(txt="A♠")]
    played = [Card(txt="3♦")]
    assert Score(available, played).score == 8

def test_score_pair():
    available = [Card(txt="3♥"), Card(txt="3♦"), Card(txt="A♠")]
    played = [Card(txt="3♥"), Card(txt="3♦")]
    assert Score(available, played).score == 32

def test_score_two_pair():
    available = played = [Card(txt="3♥"), Card(txt="3♦"), Card(txt="A♠"), Card(txt="A♦")]
    assert Score(available, played).score == 96

def test_score_three_of_a_kind():
    available = [Card(txt="3♥"), Card(txt="3♦"), Card(txt="3♠"), Card(txt="A♦")]
    played = [Card(txt="3♥"), Card(txt="3♦"), Card(txt="3♠")]
    assert Score(available, played).score == 117

def test_score_straight():
    available = played = [Card(txt="2♥"), Card(txt="3♦"), Card(txt="4♠"), Card(txt="5♦"), Card(txt="6♠")]
    assert Score(available, played).score == 200

def test_score_flush():
    available = played = [Card(txt="2♥"), Card(txt="3♥"), Card(txt="5♥"), Card(txt="8♥"), Card(txt="J♥")]
    assert Score(available, played).score == 252

def test_score_full_house():
    available = played = [Card(txt="3♥"), Card(txt="3♦"), Card(txt="3♠"), Card(txt="A♦"), Card(txt="A♠")]
    assert Score(available, played).score == 284

def test_score_four_of_a_kind():
    available = played = [Card(txt="3♥"), Card(txt="3♦"), Card(txt="3♠"), Card(txt="3♣")]
    assert Score(available, played).score == 504

def test_score_straight_flush():
    available = played = [Card(txt="2♥"), Card(txt="3♥"), Card(txt="4♥"), Card(txt="5♥"), Card(txt="6♥")]
    assert Score(available, played).score == 960

def test_score_card_two_hearts():
    card = Card(txt="2♥")
    score = Score(input=[card], played=[card])
    chips, multiplier = score._score_card(card, 0, 1)
    assert (chips, multiplier) == (2, 1)

def test_score_card_bonus():
    card = Card(txt="A♠+")
    score = Score(input=[card], played=[card])
    chips, multiplier = score._score_card(card, 0, 1)
    assert (chips, multiplier) == (41, 1)

def test_score_card_mult():
    card = Card(txt="K♠x")
    score = Score(input=[card], played=[card])
    chips, multiplier = score._score_card(card, 0, 1)
    assert (chips, multiplier) == (10, 5)

def test_score_string_input():
    """Test Score with string inputs for available and played cards."""
    available = "[2♥,3♦,A♠]"
    played = "[3♦]"
    score = Score(available, played)
    assert score.score == 8
    assert score.hand.name == "High Card"
    assert score.remaining == [Card(txt="2♥"), Card(txt="A♠")]

def test_score_joker_pluto():
    """Test Score with a Pluto joker card."""
    available = "[2♥,2♦,A♠,🂿 Pluto: multiplies by 2 the chips and multiplier of the High Card hand]"
    assert Score(available, "[2♥,2♦]").score == 28  # Pair without Pluto joker effect
    assert Score(available, "[A♠]").score == 42  # High Card with Pluto joker

def test_score_joker_venus_plus_plus():
    """Test Score with a Venus Plus Plus joker card."""
    available = "[2♥,2♦,2♠,3♦,A♠,🂿 Venus++: multiplies by 10 the chips and multiplier of the Three of a Kind hand]"
    played = "[2♥,2♦,2♠]"
    score = Score(available, played)
    assert score.score == 9180

def test_score_jokers_mars_and_shard():
    """Test Score with Mars and Mars Shard joker cards, in both orders"""
    available = "[🂿 Mars: multiplies by 2 the chips and multiplier of the Four of a Kind hand,🂿 Mars Shard: adds 1 to the chips and multiplier of the Four of a Kind hand,2♥,2♦,2♠,2♣]"
    played = "[2♥,2♦,2♠,2♣]"
    score = Score(available, played).score == 1935
    available = "[🂿 Mars Shard: adds 1 to the chips and multiplier of the Four of a Kind hand,🂿 Mars: multiplies by 2 the chips and multiplier of the Four of a Kind hand,2♥,2♦,2♠,2♣]"
    played = "[2♥,2♦,2♠,2♣]"
    score = Score(available, played)
    assert score.score == 2080

def test_score_jokers_barren_planets():
    """Test Score with barren planet jokers that set chips and multipliers to 1"""
    available = "[🂿 Barren Pluto: sets the chips and multiplier of the High Card hand to 1,2♥,3♦,A♠]"
    played = "[2♥]"
    score = Score(available, played)
    assert score.score == 3

def test_score_jokers_earth_and_barren():
    """Test Score with Earth and Barren jokers"""
    available = "[🂿 Earth: multiplies by 2 the chips and multiplier of the Full House hand,🂿 Barren Earth: sets the chips and multiplier of the Full House hand to 1,2♥,2♦,2♠,3♦,3♠]"
    played = "[2♥,2♦,2♠,3♦,3♠]"
    score = Score(available, played)
    assert score.score == 13
    # Try also with the Barren Earth first
    available = "[🂿 Barren Earth: sets the chips and multiplier of the Full House hand to 1,🂿 Earth: multiplies by 2 the chips and multiplier of the Full House hand,2♥,2♦,2♠,3♦,3♠]"
    played = "[2♥,2♦,2♠,3♦,3♠]"
    score = Score(available, played)
    assert score.score == 28

def test_score_asdict():
    available = [Card(txt="2♥"), Card(txt="3♦"), Card(txt="A♠")]
    played = [Card(txt="3♦")]
    score = Score(available, played)
    score_dict = score.asdict()
    assert score_dict["input"] == ["2♥", "3♦", "A♠"]
    assert score_dict["played"] == ["3♦"]
    assert score_dict["remaining"] == ["2♥", "A♠"]
    assert score_dict["hand"] == "High Card"
    assert score_dict["chips"] == 8
    assert score_dict["multiplier"] == 1
    assert score_dict["score"] == 8

def test_score_asdict_invalid_play():
    available = [Card(txt="2♥"), Card(txt="3♦"), Card(txt="A♠")]
    played = [Card(txt="K♠")]  # not available
    score = Score(available, played)
    score_dict = score.asdict()
    assert score_dict["input"] == ["2♥", "3♦", "A♠"]
    assert score_dict["played"] == ["K♠"]
    assert score_dict["remaining"] is None
    assert score_dict["hand"] == "Invalid Play"
    assert score_dict["chips"] == 0
    assert score_dict["multiplier"] == 0
    assert score_dict["score"] == 0

def test_score_asdict_invalid_format_backticks():
    available = [Card(txt="2♠x"), Card(txt="3♦"), Card(txt="A♠")]
    played = """```
        [2♠x]
    ```"""  # Invalid format
    score = Score(available, played)
    score_dict = score.asdict()
    assert score_dict["input"] == ["2♠x", "3♦", "A♠"]
    assert score_dict["played"] == played
    assert score_dict["remaining"] is None
    assert score_dict["hand"] == "Invalid Play"
    assert score_dict["chips"] == 0
    assert score_dict["multiplier"] == 0
    assert score_dict["score"] == 0

def test_score_asdict_invalid_format_backticks_plaintext():
    available = [Card(txt="2♥"), Card(txt="8♠"), Card(txt="A♠")]
    played = """```plaintext
        [8♠]
    ````"""  # Invalid format
    score = Score(available, played)
    score_dict = score.asdict()
    assert score_dict["input"] == ["2♥", "8♠", "A♠"]
    assert score_dict["played"] == played
    assert score_dict["remaining"] is None
    assert score_dict["hand"] == "Invalid Play"
    assert score_dict["chips"] == 0
    assert score_dict["multiplier"] == 0
    assert score_dict["score"] == 0

### ScoreDataset Tests

def test_scoredataset_all_valid():
    data = {
        "input": ["[3♥,3♦]", "[2♥,3♦]"],
        "score": [32, 8],
    }
    ds = Dataset.from_dict(data)
    plays = [
        [Card("3♥"), Card("3♦")],  # valid pair
        [Card("3♦")],              # high card
    ]
    score_dataset = ScoreDataset(dataset=ds, plays=plays)
    assert score_dataset.total_score == 32 + 8
    assert score_dataset.total_normalized_score == 1.0
    assert score_dataset.invalid_hands == 0
    assert score_dataset.normalized_invalid_hands == 0.0

def test_scoredataset_with_invalid_play():
    data = {
        "input": ["[3♥,3♦]"],
        "score": [32],
    }
    ds = Dataset.from_dict(data)
    plays = [
        [Card("A♠")],  # not available, should be invalid
    ]
    score_dataset = ScoreDataset(dataset=ds, plays=plays)
    assert score_dataset.total_score == 0
    assert score_dataset.normalized_score == 0.0
    assert score_dataset.invalid_hands == 1
    assert score_dataset.normalized_invalid_hands == 1.0
    assert score_dataset.scores[0].hand == InvalidPlay

def test_scoredataset_mixed_valid_invalid():
    data = {
        "input": ["[3♥,3♦]", "[2♥,3♦]"],
        "score": [32, 8],
    }
    ds = Dataset.from_dict(data)
    plays = [
        [Card("3♥"), Card("3♦")],  # valid
        [Card("A♠")],              # invalid
    ]
    score_dataset = ScoreDataset(dataset=ds, plays=plays)
    assert score_dataset.total_score == 32
    assert score_dataset.invalid_hands == 1
    assert score_dataset.normalized_invalid_hands == 0.5
    assert score_dataset.total_normalized_score == 0.5
    assert score_dataset.scores[1].hand == InvalidPlay

def test_scoredataset_strings():
    """Test ScoreDataset with string inputs for plays."""
    data = {
        "input": ["[3♥,3♦]", "[2♥,3♦]"],
        "score": [32, 8],
    }
    ds = Dataset.from_dict(data)
    plays = [
        "[3♥,3♦]",  # valid pair
        "[3♦]"      # high card
    ]
    score_dataset = ScoreDataset(dataset=ds, plays=plays)
    assert score_dataset.total_score == 32 + 8
    assert score_dataset.total_normalized_score == 1.0
    assert score_dataset.invalid_hands == 0
    assert score_dataset.normalized_invalid_hands == 0.0

def test_scoredataset_asdict():
    data = {
        "input": ["[3♥,3♦]", "[2♥,3♦]"],
        "score": [32, 8],
    }
    ds = Dataset.from_dict(data)
    plays = [
        [Card("3♥"), Card("3♦")],
        [Card("3♦")],
    ]
    score_dataset = ScoreDataset(dataset=ds, plays=plays)
    d = score_dataset.asdict()
    assert d["total_score"] == 40
    assert d["total_normalized_score"] == 1.0
    assert d["invalid_hands"] == 0
    assert d["normalized_invalid_hands"] == 0.0
    assert isinstance(d["scores"], list)
    assert d["scores"][0]["score"] == 32
    assert d["scores"][1]["score"] == 8
