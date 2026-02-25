from testing_base import * 

game = Games()
playerList = [Player("Player1"), Player("Player2"), Player("Player3")]


def test_amountPlayers():
    #call startGame(), include instructions to input for each case that you're testing
    #https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    assert game.startGame(True) ==  Exception("That's too many players! Try again.")
