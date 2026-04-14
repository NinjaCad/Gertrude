from testing_base import *
import pytest
import flask

#referenced test_game_initialization.py and test_play_card.py to help build test cases

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def simulate_game():
    # Initiate players
    faith = Player("Faith")
    rose = Player("Rose")
    david = Player("David")
    joseph = Player("Joseph")
    eli = Player("Eli")
    daniel = Player("Daniel")

    # Create and shuffle a deck
    new_deck = Deck()
    new_deck.shuffle()

    # Set current card to Ace of Diamonds
    ace_diamonds = None
    for card in new_deck.cards:
        if (card.suit == "Diamonds" and card.value == 1):
            ace_diamonds = card
            break
    GAME_STATE["current_card"] = ace_diamonds
    GAME_STATE["counter"] = 1

    #referenced https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment to help solve a problem involving player_list
    for player in [faith, rose, david, joseph, eli, daniel]:
        player_list.append(player)
    Dealer(Deck()).deal_cards(player_list[1:])

    for player in player_list:
        GAME_STATE["played_cards"].append(player.pop_card())

    GAME_STATE["slap_list"] = player_list

    return GAME_STATE, player_list

def test_win_page_route(client):
     response = client.get("/win_page")
     assert response.status_code == 200

def test_win_page_data(client):
    response = client.get("/win_page")
    html = response.get_data(as_text=True)
    assert "Faith has won" in html