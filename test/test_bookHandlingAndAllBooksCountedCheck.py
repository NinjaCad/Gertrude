from testing_base import *

# Create deck and dealer
deck = Deck()
dealer = Dealer(deck)

# # Create players
player1 = Player("Tim")
player2 = Player("Tom")
players = [player1, player2]

# Deal 5 cards to each player
dealer.dealCards(5, list(players))

# Show each player's hand
for player in players:
    print(f'{player.name}:')
    player.showHand(True)
    print()

def test_empty_hand_bookless():
    player1.books = 0
    #Has no cards
    player.clearHand()
    player.bookHandling()
    assert player.books == 0
    assert dealer.checkIfAllThirteenBooksHaveBeenFormed(players) == False 
    assert player.hand == []
    assert len(player.knownCards) == len(player.hand)

def test_small_hand_bookless():
    player.books = 0
    #Does not have enough cards
    cardImages=[0]
    index=0
    cardBack=0
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack)]
    player.clearHand()
            # in practice, we will ge getting cards normally with deck.getCard with something like what is below; however, for now I can not figure out how to draw specific cards as it onlt takes the self argument, so I am using setHand for proof of the logic working given different scenarios of kinds of sets of cards in hand.
            # player.hand.append(deck.getCard())
            # P.S. if any of you are doing test scenarios like this, be sure to do it where the cards are in brackets for a list; I accidentally used parenthesees and it was giving me so many problems with tuples when trying to remove cards
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == []
    player.bookHandling()
    assert player.books == 0
    assert dealer.checkIfAllThirteenBooksHaveBeenFormed(players) == False
    assert player.hand == list_of_cards
    assert len(player.knownCards) == len(player.hand)

def test_big_hand_bookless():
    player.books = 0
    #Has Enough cards but no Book
    cardImages=[0]
    index=0
    cardBack=0
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Spades", 2, cardImages[index], cardBack), Card("Clubs", 2, cardImages[index], cardBack)]
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == []
    player.bookHandling()
    assert player.books == 0
    assert dealer.checkIfAllThirteenBooksHaveBeenFormed(players) == False
    assert player.hand == list_of_cards
    assert len(player.knownCards) == len(player.hand)


def test_book_in_hand():
    player.books = 0
    #Has A book
    cardImages=[0]
    index=0
    cardBack=0
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Diamonds", 1, cardImages[index], cardBack), Card("Spades", 2, cardImages[index], cardBack)]
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == ['Aces']
    player.bookHandling()
    assert player.books == 1
    assert dealer.checkIfAllThirteenBooksHaveBeenFormed(players) == False
    assert player.hand == [Card("Spades", 2, cardImages[index], cardBack)]
    assert len(player.knownCards) == len(player.hand)

def test_books_in_hand():
    player.books = 0
    #Has 2 Books
    cardImages=[0]
    index=0
    cardBack=0
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Diamonds", 1, cardImages[index], cardBack), Card("Spades", 2, cardImages[index], cardBack), Card("Clubs", 2, cardImages[index], cardBack), Card("Hearts", 2, cardImages[index], cardBack), Card("Diamonds", 2, cardImages[index], cardBack)]
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == ['Aces', 'Twos']
    player.bookHandling()
    assert player.books == 2
    assert dealer.checkIfAllThirteenBooksHaveBeenFormed(players) == False
    assert player.hand == []
    assert len(player.knownCards) == len(player.hand)


def test_last_book_in_hand():
    player1.books = 6
    player2.books = 6
    #Has the 13th Book
    cardImages=[0]
    index=0
    cardBack=0
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Diamonds", 1, cardImages[index], cardBack)]
    player1.clearHand()
    player2.clearHand()
    player1.setHand(list_of_cards)
    assert player1.checkForFourOfAKind() == ['Aces']
    player1.bookHandling()
    assert player1.books == 7 
    assert dealer.checkIfAllThirteenBooksHaveBeenFormed(players) == True
    assert player1.hand == []
    assert len(player1.knownCards) == 0