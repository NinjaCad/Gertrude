from testing_base import *
from cardgames.Games import GAME_STATE
from cardgames.global_card_change import global_card_change

def test_card_change():
    default_player = Player("default", 0)
    GAME_STATE["current_player"] = default_player
    default_deck = Deck()
    default_player.hand = default_deck.cards
    initial_hand_size = len(default_player.hand)

    played_card = global_card_change()
    
    # Check that the card is the right one
    assert played_card == str(GAME_STATE["current_card"])
    # Check that the card isn't in the player hand anymore
    assert GAME_STATE["current_card"] not in default_player.hand
    # Check that player hand size has decreased
    assert len(default_player.hand) == initial_hand_size - 1

def test_empty_hand():
    default_player = Player("default", 0)
    GAME_STATE["current_player"] = default_player

    assert global_card_change() == "No card to play"