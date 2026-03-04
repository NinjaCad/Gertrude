from operator import truediv
from ssl import Options

from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')

    # Loop through all the players
    # Parameters is a player list
    def round(self, pList):
        # dealCards()      Need to reset player hands and hand out cards

        # Repeat length of players minus gertrude
        for player in pList:
            # Display current hand
            print(f"{player.name}'s hand: ")
            player.showHand()

            turn = True
            while(turn): # (turn && endTurn() == False)   end turn after certain conditions
                # Check to see what the player can do
                options = {}
                options["hit"] = True
                options["stand"] = True
                options["split"] = False
                options["doubleDown"] = False
                #options["insurance"] = False

                # Print what the player can do
                move = input("Choose either to: ")
                for key, value in pList.items():
                    if value:  # only if True
                        print(key)

                # Call functions according to players choice
                if (options["hit"] and (move == "hit" or move == "h")):
                    print("hit")
                    # player.hit()
                elif (options["stand"] and (move == "stand" or move == "s")):
                    print("stand")
                    # player.stand()
                elif (options["split"] and (move == "split" or move == "sp")):
                    print("split")
                    # player.split()
                elif (options["doubleDown"] and (move == "doubleDown" or move == "dd")):
                    print("double down")
                    # player.doubleDown()
                else:
                    print("That is not a valid repsonse")

            # playerGertrude()        start gertrude's turn
            # calculateWinner()   end round and calculate winner


if __name__ == "__main__":
    game = Games()
    game.main()