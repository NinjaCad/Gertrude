from cardgames.Games import win_check
from testing_base import *

def test_player_won():
    #To see if a player with no cards left wins
    deck = Deck()
    players = [Player("Harry"), Player("Ron"), Player("Hermione")]
    dealer = Dealer(deck)
    dealer.deal_cards(players)
    players[0].clear_hand()
    assert win_check(players) == True

def test_player_did_not_win():
    #To see if a player with cards left does not win
    deck = Deck()
    players = [Player("Ted"), Player("George"), Player("Anna"), Player("Katie")]
    dealer = Dealer(deck)
    dealer.deal_cards(players)
    assert win_check(players) == False