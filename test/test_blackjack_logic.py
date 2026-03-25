from testing_base import *

# Tests for getHandValue()

def test_simple_hand_value():
    game = Games() 

    player = Player("Janice")
    player.addCard(getCard("hearts" , 10))
    player.addCard(getCard("clubs" , 7))

    assert game.getHandValue(player) == 17

    # This test undegoes a check of the getHandValue() definition that adds cards 
    # to a made up player hand and checks using assert to check for a boolean of 
    # true or false of the required value of the hand

def test_aces():

    game = Games()

    player = Player("Janice")
    player.addCard(getCard("spades" , 1)) # embedded Ace
    player.addCard(getCard("hearts" , 5))
    player.addCard(getCard("diamonds" , 9))

    assert game.getHandValue(player) == 15

    # This test undergoes an embedded ace in the hand, 
    # it has the fucntionality of testing the Ace logic 
    # function within getHandValue() to test wheter the 
    # game gives the player the best definition of Ace 
    # for their hand for them to win, 1 or 11 value.

# Tests for calculateWinner()

def test_player_wins():
    game = Games()

    player = Player("Janice")
    dealer = Player("Gertrude")

    player.addCard(getCard("hearts" , 10))
    player.addCard(getCard("clubs" , 9))

    dealer.addCard(getCard("spades" , 10))
    dealer.addCard(getCard("diamonds" , 7))

    results = game.calculateWinner([player , dealer])

    assert results["Janice"] is True

    # runs through the possibiltiy of one player vs 
    # the dealer player Gertrude having a hand that 
    # is greater than the hand Gertrude has, stopped 
    # at 17 because the Gertrude AI will not progress 
    # a hit after 17 hand value, which is standard for 
    # simple BlackJack AI's

def test_dealer_wins():
    game = Games()

    player = Player("Janice")
    dealer = Player("Gertrude")

    player.addCard(getCard("hearts" , 8))
    player.addCard(getCard("clubs" , 8))

    dealer.addCard(getCard("spades" , 10))
    dealer.addCard(getCard("diamonds" , 9))

    results = game.calculateWinner([player , dealer])

    assert results["Janice"] is False

    # Runs through the scenario that the dealer player 
    # Gertrude wins the round and beats out the players hand. 

print("file ran succesfully")