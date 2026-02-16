import random
from testing_base import *

def test_reset_deck():

    deck = Deck()
    for i in range(random.randint(1,52)):
        deck.getCard()
    assert len(deck.cards) != 52

    #here I create a copy of the deck and reset it to show the state after self.deck.reset() and before self.deck.shuffle() as resetDeck runs the two consecutively
    deckClone = deck
    
    deckClone.reset()
    assert len(deckClone.cards) == 52
    deckA = deckClone
    deckB = deckClone

    matching = 0
    for i in range(len(deckB.cards)):
        if deckA.cards[i] == deckB.cards[i]:
            matching += 1
    assert matching == 52
    
    #normally this is where the deck would be shuffled and we would assert the matching between the suffled and unshuffled decks to be different, but instead of calling shuffle on DeckB, I will call resetDeck on deck to simulate the true test we are doing as Decks A and B were just clones of Deck representing the middle step between sub functions
    deck.resetDeck()
    assert len(deck.cards) == 52

    deck1 = deck
    deck2 = deck
    matching = 0
    for i in range(len(deck2.cards)):
        if deck1.cards[i] == deck2.cards[i]:
            matching += 1
    # the probability of two random decks having 7+ matching cards
    # in fixed locations is 0.0084% (about 1 in 12,000)
    assert matching < 7


#since the resetDeck function is strictly two subfunctions that each already have tests, the test here is primarily combining the two sub tests.
    """
    Reference code from existing tests of sub functions. I wanted to acknowledge their existance and commented further to prve I understood them.

    #for self.deck.reset()
    deck = Deck()
    # Removes some cards from the deck
    for _ in range(40):
        deck.getCard()
    assert len(deck.cards) != 52

    deck.reset()
    assert len(deck.cards) == 52

    #for self.deck.shuffle()
    deck1 = Deck()
    deck2 = Deck()

    #checks to see each card in the ordered index of deckA vs deckB to see how often the same number of pulls would yield the same card
    matching = 0 #initializes the starting value for matching at 0 so we only add later if there are matches
    for i in range(len(deck2.cards)):
        if deck1.cards[i] == deck2.cards[i]:
            matching += 1
    assert matching == 52 #makes sure that both Decks are the exact same pre-shuffle

    deck2.shuffle()
    matching = 0
    for i in range(len(deck2.cards)):
        if deck1.cards[i] == deck2.cards[i]:
            matching += 1
    # the probability of two random decks having 7+ matching cards
    # in fixed locations is 0.0084% (about 1 in 12,000)
    assert matching < 7
    """