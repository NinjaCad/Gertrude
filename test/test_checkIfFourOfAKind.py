from testing_base import *

# Create deck and dealer
deck = Deck()
dealer = Dealer(deck)

# # Create players
players = {}
name = "Tim"
players[name] = Player(name)
name = "Tom"
players[name] = Player(name)

# Deal 5 cards to each player
dealer.dealCards(5, list(players.values()))

# Show each player's hand
for player in players.values():
    print(f'{player.name}:')
    player.showHand(True)
    print()

    cardImages=[0]
    index=0
    cardBack=0
def test_empty_hand_bookless():
    #Has no cards
    player.clearHand()
    assert player.checkForFourOfAKind() == False

def test_small_hand_bookless():
    #Does not have enough cards
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack)]
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == False

def test_big_hand_bookless():
    #Has Enough cards but no Book
    list_of_cards = [Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Spades", 2, cardImages[index], cardBack), Card("Clubs", 2, cardImages[index], cardBack)]
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == False

def test_book_in_hand():
    #Has A book
    list_of_cards = (Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Diamonds", 1, cardImages[index], cardBack), Card("Spades", 2, cardImages[index], cardBack))
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == (['Aces'], 1)

def test_books_in_hand():
    #Has 2 Books
    list_of_cards = (Card("Spades", 1, cardImages[index], cardBack), Card("Clubs", 1, cardImages[index], cardBack), Card("Hearts", 1, cardImages[index], cardBack), Card("Diamonds", 1, cardImages[index], cardBack), Card("Spades", 2, cardImages[index], cardBack), Card("Clubs", 2, cardImages[index], cardBack), Card("Hearts", 2, cardImages[index], cardBack), Card("Diamonds", 2, cardImages[index], cardBack))
    player.clearHand()
    player.setHand(list_of_cards)
    assert player.checkForFourOfAKind() == (['Aces', 'Twos'], 2)