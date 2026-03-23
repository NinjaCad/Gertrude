from testing_base import *
from cardgames.card_system import card_art
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
def test_card_art_returns_string():
    result = card_art('♠', 'A')
    assert isinstance(result, str)
def test_card_art_dimensions():
    result = card_art('♣', '10')
    lines = [line for line in result.split('\n') if line.strip()]
    assert len(lines) == 7
def test_card_art_width():
    result = card_art('♥', '10')
    lines = [line for line in result.split('\n') if line.strip()]
    for line in lines:
        assert len(line) == 11
def test_suit_and_rank_presence():
    result = card_art('♦', 'Q')
    assert '♦' in result
    assert 'Q' in result
    assert card_art('K', '♦') == ('K', '♦')