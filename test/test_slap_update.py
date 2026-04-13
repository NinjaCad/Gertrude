from testing_base import *
from cardgames.page_3 import resolve_slap 
import copy

# Uses local game_state variable because resolve_slap doesn't need the global one and this prevents circular imports

def setup_game():
    # Initialize a game state
    game_state = {
        "current_card": None,
        "current_player": None,
        "played_cards": [],
        "slap_list": [],
        "slap_in_progress": False,
        "counter": 0
    }

    # Create test players
    faith = Player("faith")
    rose = Player("rose")
    david = Player("david")
    joseph = Player("joseph")
    eli = Player("eli")
    daniel = Player("daniel")

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
    game_state["counter"] = 1

    players = [faith, rose, david, joseph, eli, daniel]
    Dealer(Deck()).deal_cards(players)

    for player in players:
        game_state["played_cards"].append(player.pop_card())

    return game_state, players

# Check nothing happens if there's not enough slaps
def test_num_slaps():
    game_state, players = setup_game()
    game_state["slap_list"].extend(["rose", "david"])
    deck_receiver, game_state = resolve_slap(copy.deepcopy(game_state), players)

    assert deck_receiver == "faith" # the default is the first player in the player_list for testing purposes - which would be faith

# Check the last person to slap (only person to not slap) received the deck when they were supposed to slap
def test_valid_slap_loser():
    game_state, players = setup_game()
    game_state["slap_list"].extend(["rose", "david", "joseph", "eli", "daniel"])

    # Check faith slapped last when it was correct to slap
    deck_receiver, _ = resolve_slap(copy.deepcopy(game_state), players)
    assert deck_receiver == "faith"

# Check the first person to slap received the deck when they weren't supposed to slap
def test_invalid_slap_loser():
    game_state, players = setup_game()
    game_state["slap_list"].extend(["rose", "david"])

    # Check rose slapped first when it wasn't correct to slap
    game_state["counter"] = 2
    deck_receiver, _ = resolve_slap(copy.deepcopy(game_state), players)
    assert deck_receiver == "rose"

# Check the deck receiver actually has the played_cards in their hand
def test_received_deck():
    game_state, players = setup_game()
    faith = players[0]
    game_state["slap_list"].extend(["rose", "david", "joseph", "eli", "daniel"])

    played_cards_copy = copy.copy(game_state["played_cards"])

    _, game_state = resolve_slap(copy.deepcopy(game_state), players)

    for card in played_cards_copy:
        assert card in faith.get_hand()

# Check game_state is reset afterwards
def test_reset_game_state():
    game_state, players = setup_game()
    game_state["slap_list"].extend(["rose", "david", "joseph", "eli", "daniel"])

    _, game_state = resolve_slap(copy.deepcopy(game_state), players)

    assert not game_state["played_cards"]
    assert not game_state["slap_list"]
    assert game_state["slap_in_progress"] is False