from testing_base import *
from cardgames.page_3 import resolve_slap, blank 
import copy

# Uses local game_state variable because resolve_slap doesn't need the global one and this prevents circular imports

def setup_game():
    # Initialize a game state
    game_state = {
        "current_card": None,
        "current_player": None,
        "played_cards": [],
        "slap_dict": {},
        "slap_in_progress": False,
        "slap_start_time": None,
        "counter": 0
    }

    # Create test players
    faith = Player("faith")
    rose = Player("rose")

    # Create and shuffle a deck
    new_deck = Deck()
    new_deck.shuffle()

    # Set current card to Ace of Diamonds
    ace_diamonds = None
    for card in new_deck.cards:
        if (card.suit == "Diamonds" and card.value == 1):
            ace_diamonds = card
            break
    game_state["current_card"] = ace_diamonds

    # Deal 10 cards to each player and 10 to played_cards
    for _ in range(10):
        faith.add_card(new_deck.get_card())
        rose.add_card(new_deck.get_card())
        game_state["played_cards"].append(new_deck.get_card())

    # Set up slap times
    game_state["slap_dict"]["faith"] = {"time": 110}
    game_state["slap_dict"]["rose"] = {"time": 105}

    players = [faith, rose]

    return game_state, players

# Check players are in the right order in the dictionary
def test_player_order():
    game_state, players = setup_game()
    game_state["counter"] = 1
    game_state, sorted_players, _ = resolve_slap(copy.deepcopy(game_state), players)
    assert sorted_players[0] == "rose"

# Check the right person received the deck
def test_id_loser():
    game_state, players = setup_game()

    # Check faith slapped last when it was correct to slap
    game_state["counter"] = 1
    _, _, deck_receiver = resolve_slap(copy.deepcopy(game_state), players)
    assert deck_receiver == "faith"
    
    # Check rose slapped first when it wasn't correct to slap
    game_state["counter"] = 2
    _, _, deck_receiver = resolve_slap(copy.deepcopy(game_state), players)
    assert deck_receiver == "rose"

# Check the deck receiver actually has the played_cards in their hand
def test_received_deck():
    game_state, players = setup_game()
    faith = players[0]

    game_state["counter"] = 1
    played_cards_copy = copy.copy(game_state["played_cards"])

    game_state, _, _ = resolve_slap(copy.deepcopy(game_state), players)

    for card in played_cards_copy:
        assert card in faith.get_hand()

# Check game_state is reset afterwards
def test_reset_game_state():
    game_state, players = setup_game()
    game_state["counter"] = 1

    game_state, _, _ = resolve_slap(copy.deepcopy(game_state), players)

    assert not game_state["played_cards"]
    assert not game_state["slap_dict"]
    assert game_state["slap_in_progress"] is False
    assert game_state["slap_start_time"] is None