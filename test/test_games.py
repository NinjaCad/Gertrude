from testing_base import * 

game = Games()
playerList = [Player("Player1"), Player("Player2"), Player("Player3")]
def test_amountPlayers():
    #ask prof about in class: how could I test a function that requires 
    #an input and outputs a print statement
    pass

def test_choice():
    #calls a function choice() that is just the exception statement
    #in 6b (view doc)
    
    #choice(desiredAction, currentRound)  
    result = game.choice(0, 0)
    assert result == -1

    result2 = game.choice(4, 0)
    assert result2 == -1
    #or not GERTRUDE busted or not

    result3 = game.choice(3, 1)
    assert result3 == -1

#two funcs below calls a function gertBust() in Games() that determines,
    #based off a true or false value whether 
    #GERTRUDE busted or not
    #gertBust(boolBust, score, playerList) 
def test_gertBust():
    result = game.gertBust(True, -1, playerList)
    assert result == -1

def test_gertNoBust():
    playerList[0].addCard(getCard('Clubs', 12))
    playerList[0].addCard(getCard('Spades', 7))
    
    playerList[1].addCard(getCard('Diamonds', 12))
    playerList[1].addCard(getCard('Clubs', 10))
    
    playerList[2].addCard(getCard('Hearts', 12)) 
    playerList[2].addCard(getCard('Spades', 5))

    result = game.gertBust(False, 18, playerList)
    assert result == 1