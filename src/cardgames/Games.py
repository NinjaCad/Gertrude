from operator import truediv
from ssl import Options

from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Simple BlackJack!')
        self.playerList = self.startGame()
        
        # GERT-36 fixing main() in Games.py (see below outline of main)
        # WHILE PLAYING BLACKJACK (prompt after each game if they want to play again) {
        #
        #     player.bet() for each player
        #     GERT-33 Gertrude.dealCards() (see dealer class)
        #
        #     WHILE PLAYING GAME {
        #         round()
        #     }
        #     GERT-29 get gertrude player action (hit, stand)
        #
        #     calculateWinner()
        #     reset/shuffle deck, clear player hands using gertrude dealer
        #     
        
        input('Press [Enter] to exit.')

    # startGame()
    # inputs: none
    # outputs: list of player objects, where list[0] = Gertrude and list[1:] is the list of human players. GERT-29 Gertrude should be an object with a Player class and a Dealer class
    # goals: initialize Gertrude and player objects
    # suggestions: a) do not use self. before variables. That is creating a bunch of attributes for the class that we aren't using. Just use normal variables.
    #              b) GERT-29 add Gertrude before players so Gertrude object is always at index 0
    #              c) return pl_list
    def startGame(self):
        while True:
            try:
                self.amtPlayers = int(input("How many people are playing? (7 players max.) "))
                
                if self.amtPlayers > 7:
                    print("That's too many players! Try again.")
                    continue
                if self.amtPlayers < 1:
                    print("There needs to be at least one player! Try again.")
                    continue
                break
            except ValueError:
                print("That doesn't make any sense, try again.")
        print('This round of blackjack will be played with {:d} players, against the dealer, GERTRUDE'.format(self.amtPlayers))
        self.pl_list = []
        for i in range(self.amtPlayers):
            self.pl_list.append(Player(str(input("Player {:d}'s name is: ".format(i+1)))))
        self.pl_list.append(Player("GERTRUDE")) #Player("GERTRUDE") will be eventually replaced
        self.round(self.pl_list)


    # round()
    # inputs: none
    # outputs: none
    # goals: loop through every player and get an action (or lack thereof)
    # suggestions: a) no need for pList parameter when we have initialized self.playerList in main(). Use self.playerList instead
    #              b) print the hand of every player at the beginning of the round and after each player's move to simulate what players would see in a physical game. currently, it only prints each individual players hand once when asking for their turn
    #              c) when asking each player what move they want to do, do not ask Gertrude. only ask human players
    #              d) rework so that it gets player input, checks if player input == each possible action and whether or not the requirements to make that move are made all at once
    #                 
    #                     Example:
    #                     move = input
    #                     if move is stand
    #                         player.stand()
    #                     if move is split and player has 2 identical cards
    #                         player.split()
    #                     ...
    #                     else (no valid move was entered or conditions for move were not met, such as trying to split with two different cards)
    #                         repeat everything above
    #
    #              e) gertrude and playerWinner functions will not run inside this loop, they will run in main()
    #              f) implement check for self.active to tell if a player has already stood or busted
    #              g) after each player makes a move, call player.check_cards to determine if they busted
    #              h) GERT-26 accept help as a possible move. however, make sure a players turn isn't skipped if they use (help)
    def round(self, pList):
        # Loop through all the players
        # Parameters is a player list
        # dealCards()      Need to reset player hands and hand out two cards per player

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
                    player.hit(True)
                elif (options["stand"] and (move == "stand" or move == "s")):
                    print("stand")
                    player.stand()
                elif (options["split"] and (move == "split" or move == "sp")):
                    print("split")
                    player.split()
                elif (options["doubleDown"] and (move == "doubleDown" or move == "dd")):
                    print("double down")
                    player.doubleDown()
                else:
                    print("That is not a valid repsonse")

            # playerGertrude()        start gertrude's turn
            # calculateWinner()   end round and calculate winner
            
    # GERT-31 calculateWinner()
    # inputs: none
    # outputs: none
    # goals: a) using self.playerList, compare every human player score to Gertrude player's score using player.check_cards()
    #        b) reapportion player money based on player bets earlier (see resolve_bet() in Player.py for more information on format)
    #        c) GERT-30 call trashtalk() on the players who lose

    # GERT-26 help()
    # inputs: none
    # outputs: none
    # goals: print out general game instructions

if __name__ == "__main__":
    game = Games()
    game.main()
 
 

