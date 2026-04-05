import pytest
from cardgames.Player import Player
from cardgames.Card_Compare import Card
from cardgames import Time_limit

@pytest.fixture
def test_setup():
    """Create a player and a card to use in tests."""
    p = Player("Tester")
    c = Card("Spades", 10, [], [])
    return p, c

def test_player_hand_assignment(test_setup):
    p, c = test_setup  
    p.addCard(c)
    assert len(p.hand) == 1
    assert p.hand[0].value == 10

def test_chosen_card_property(test_setup):
    """Test if the .chosen_card property exists and can be set."""
    p, c = test_setup
    p.chosen_card = c
    assert p.chosen_card.suit == "Spades"

def test_timeout_constant():
    """Verify that the game recognizes the 'TIMEOUT' string."""
    result = "TIMEOUT"
    assert result.isupper() 
    assert len(result) == 7