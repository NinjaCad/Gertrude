from testing_base import *

def test_num_Cards_in_Hand():
    #To see if the whole deck is now in the player's hand
    deck = Deck()
    player = Player("Mary")
    dealer = Dealer(deck)
    dealer.addDeck_to_Hand(player)
    assert len(player.hand) == 52

def test_num_Cards_left_in_deck():
    #To see if there are no more cards remaining in the deck
    deck = Deck()
    player = Player("Fred")
    dealer = Dealer(deck)
    dealer.addDeck_to_Hand(player)
    assert len(dealer.deck.cards) == 0

def test_player_Cards():
    #To see if the deck is properly added to the player's hand when the deck does not contain all 52 cards
    deck = Deck()
    player = Player("Matt")
    dealer = Dealer(deck)
    popped = []
    for idk in range(26):
        card = deck.cards.pop()
        popped.append(card)

    dealer.addDeck_to_Hand(player)
    assert len(player.hand) == len(popped)
    