from testing_base import *

#confirm the following:
"""
1. The turn loop keeps going when no books exist. -- works when game is created
2. The turn loop keeps going when >13 books exist. -- works the whole way through main game
3. The turn loop is broken out of when the 13th book is made by:
    A. Stealing a card -- logic ends propperly and turn cycle breaks out of the while true into the scoreboard (see canvas screenshot)
    B. Drawing a card -- logic ends propperly and turn cycle breaks out of the while true into the scoreboard (see canvas screenshot)
"""

def endGameBreakTest():
    game = Games()
    game.main()  #verify the above criterium by playing them out

endGameBreakTest()