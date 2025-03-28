from ballmatro.card import Card
from ballmatro.score import score, score_card

def test_score_invalid_hand():
    available = [Card(txt="2♥️"), Card(txt="3♦️"), Card(txt="A♠️")]
    played = [Card(txt="2♥️"), Card(txt="A♠️")]
    assert score(available, played) == 0

def test_score_unavailable_card():
    available = [Card(txt="2♥️"), Card(txt="3♦️"), Card(txt="A♠️")]
    played = [Card(txt="2♥️"), Card(txt="K♠️")]
    assert score(available, played) == 0  # Card not available

def test_score_high_card():
    available = [Card(txt="2♥️"), Card(txt="3♦️"), Card(txt="A♠️")]
    played = [Card(txt="3♦️")]
    assert score(available, played) == 8

def test_score_pair():
    available = [Card(txt="3♥️"), Card(txt="3♦️"), Card(txt="A♠️")]
    played = [Card(txt="3♥️"), Card(txt="3♦️")]
    assert score(available, played) == 32

def test_score_two_pair():
    available = played = [Card(txt="3♥️"), Card(txt="3♦️"), Card(txt="A♠️"), Card(txt="A♦️")]
    assert score(available, played) == 96

def test_score_three_of_a_kind():
    available = [Card(txt="3♥️"), Card(txt="3♦️"), Card(txt="3♠️"), Card(txt="A♦️")]
    played = [Card(txt="3♥️"), Card(txt="3♦️"), Card(txt="3♠️")]
    assert score(available, played) == 117

def test_score_straight():
    available = played = [Card(txt="2♥️"), Card(txt="3♦️"), Card(txt="4♠️"), Card(txt="5♦️"), Card(txt="6♠️")]
    assert score(available, played) == 200

def test_score_flush():
    available = played = [Card(txt="2♥️"), Card(txt="3♥️"), Card(txt="5♥️"), Card(txt="8♥️"), Card(txt="J♥️")]
    assert score(available, played) == 252

def test_score_full_house():
    available = played = [Card(txt="3♥️"), Card(txt="3♦️"), Card(txt="3♠️"), Card(txt="A♦️"), Card(txt="A♠️")]
    assert score(available, played) == 284

def test_score_four_of_a_kind():
    available = played = [Card(txt="3♥️"), Card(txt="3♦️"), Card(txt="3♠️"), Card(txt="3♣️")]
    assert score(available, played) == 504

def test_score_straight_flush():
    available = played = [Card(txt="2♥️"), Card(txt="3♥️"), Card(txt="4♥️"), Card(txt="5♥️"), Card(txt="6♥️")]
    assert score(available, played) == 960

def test_score_card_two_hearts():
    card = Card(txt="2♥️")
    chips, multiplier = score_card(card, 0, 1)
    assert (chips, multiplier) == (2, 1)

def test_score_card_bonus():
    card = Card(txt="A♠️+")
    chips, multiplier = score_card(card, 0, 1)
    assert (chips, multiplier) == (41, 1)

def test_score_card_mult():
    card = Card(txt="K♠️x")
    chips, multiplier = score_card(card, 0, 1)
    assert (chips, multiplier) == (10, 5)
