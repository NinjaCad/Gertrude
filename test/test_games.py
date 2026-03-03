from testing_base import * 

game = Games()



def test_amountPlayers():
    #call startGame(), include instructions to input for each case that you're testing
    playerList = game.startGame()
    #test case 1:
        #"How many people are playing" -----> input: 10
        #EXPECTED: "Thats too many players! Try again."
    #test case 2 (restart not needed if case 1 passed): 
        #"How many people are playing" -----> input: 0
        #EXPECTED: "There needs to be at least one player! Try again."
    #test case 3 (restart not needed if case 1 and 2 passed):
        #"How many people are playing" -----> input: 1.2
        #EXPECTED: "That doesn't make any sense, try again."
    #test case 4 (restart not needed if case 1-3 passed): 
        #"How many people are playing" -----> input: 2
        #EXPECTED: 
            #"This round of blackjack will be played with 2 players, against the dealer, GERTRUDE"
            #"Player 1's name is: " -----> input: Matthew
            #"Player 2's name is: " -----> input: Mark
            #EXPECTED: [cardgames.Player.Playerobject..., cardgames.Player.Playerobject...,
                #cardgames.Player.Playerobject...] (this is printed by test_amountPlayers(), it
                #simply shows that for loop did make player objects)
                #one of these values may read cardgames.Gertrude.Gertrudeobject, if you are testing
                #after the gertrude class has been made
    print(playerList)
test_amountPlayers()