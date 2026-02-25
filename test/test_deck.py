from testing_base import *

def test_deck_size():

    deck = Deck()
    assert len(deck.cards) == 52

def test_get_card_discard():

    deck = Deck()
    # take 5 cards off of the top of the deck
    popped = []
    for _ in range(5):
        card = deck.getCard()
        popped.append(card)
    
    assert deck.discarded == popped

def test_get_card_deck_size():

    deck = Deck()
    for _ in range(23):
        deck.getCard()
    
    assert len(deck.cards) == 52-23

def test_reset():

    deck = Deck()
    # Remove some cards from the deck
    for _ in range(40):
        deck.getCard()
    assert len(deck.cards) != 52

    deck.reset()
    assert len(deck.cards) == 52

def test_shuffle():

    deck1 = Deck()
    deck2 = Deck()

    matching = 0
    for i in range(len(deck2.cards)):
        if deck1.cards[i] == deck2.cards[i]:
            matching += 1
    assert matching == 52

    deck2.shuffle()
    matching = 0
    for i in range(len(deck2.cards)):
        if deck1.cards[i] == deck2.cards[i]:
            matching += 1
    # the probability of two random decks having 7+ matching cards
    # in fixed locations is 0.0084% (about 1 in 12,000)
    assert matching < 7

#Roman Menotti Test for Deck.py
def test_get_card_Suit():
    # Test 1
    deck = Deck()
    card = deck.getCard()
    if card.suit == "Spades":
        print("Got a Spade")
    elif card.suit == "Clubs":
        print("Got a Club")
    elif card.suit == "Hearts":
        print("Got a Heart")
    elif card.suit == "Diamonds":
        print("Got a Diamond")
    # Test 2
    assert card.suit in ["Spades", "Clubs", "Hearts", "Diamonds"]

# Test 2 Roman Menotti Test for Deck.py
def test_each_suit_has_13_cards():
    deck = Deck()
    suit_counts = {}
    for card in deck.cards:
        suit_counts[card.suit] = suit_counts.get(card.suit, 0) + 1

    for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
        assert suit_counts.get(suit, 0) == 13