from testing_base import *
from cardgames.Dealer import Dealer

def test_num_cards_in_Hand():
    #To see if the whole deck is now in the player's hand
    deck = Deck()
    player = Player("Mary")
    dealer = Dealer(deck)
    dealer.add_deck_to_Hand(player)
    assert len(player.hand) == 52

def test_num_cards_left_in_deck():
    #To see if there are no more cards remaining in the deck
    deck = Deck()
    player = Player("Fred")
    dealer = Dealer(deck)
    dealer.add_deck_to_Hand(player)
    assert len(dealer.deck.cards) == 0

def test_player_cards():
    #To see if the deck is properly added to the player's hand when the deck does not contain all 52 cards
    deck = Deck()
    player = Player("Matt")
    dealer = Dealer(deck)
    popped = []
    for i in range(26):
        popped.append(deck.getCard())

    dealer.add_deck_to_Hand(player)
    assert len(player.hand) == 52-len(popped)
    
def test_add_modified_deck():
    #Somewhat different test to see if the modified deck is still added properly
    deck = Deck()
    player = Player("Faith")
    dealer = Dealer(deck)
    for _ in range(5):
        deck.getCard()
    assert len(deck.cards) == 47