"""
GERTRUDE'S BLACKJACK TIPS

To run game:
    cd into src:   cd /app/src
    start new game:   python -m cardgames.Games
"""

from cardgames.Deck import Deck
from cardgames.Player import Player, Gertrude
from cardgames.Dealer import Dealer

class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        """
        Main game loop
        """

        self.dealer = Dealer(self.deck)

        print('\nWelcome to the Gertrude\'s BlackJack!')

        # Sets up game and player list, which will be used for rounds
        self.playerList = self.startGame()

        while True:
            # Each player places bets
            for player in self.playerList[1:]:
                player.bet("standard")
                player.bet("pairs")

            # Each player and gertrude is given 2 cards
            self.dealer.dealCards(2, self.playerList)
            
            # GERT-24 check dealers hand to see if their revealed card is an ACE
            # If so, ask each player if they want to place an insurance bet. If so, call player.insurance()
            
            if self.playerList[0].hand[0].value == 1 :  #Checking for Ace! 
                for player in self.playerList:
                    player.bet("insurance")

            # Each player takes turn
            self.round()

            # Gertrude takes turn
            self.playerList[0].gertTurn(self.dealer)
            self.playerList[0].showHand()

            # Calculate results
            results = self.calculateWinner(self.playerList)

            # Give money to winner
            for player, condition in results.items():
                player.resolve_bet({"standard": condition})

            for player in self.playerList[1:]:
                player.resolve_bet({"pairs": player.perfectPairs()})
                player.resolve_bet({"insurance": player.insurance()})
            
            # Play again
            quit = input("\nPlay another round? (y/n): ").strip().lower()
            while quit not in ["y", "yes", "n", "no"]:
                quit = input("Not a valid input. Do you want to play another round? (y/n): ").strip().lower()
            
            if quit in ["n", "no"]:
                break
            else:
                # resetting player active status, hands, and the deck after each round
                for player in self.playerList:
                    player.active = True
                    player.clearHand()
                self.deck.reset()
        
        # End game
        print("\nThanks for playing!")
        input('Press [Enter] to exit.')
    
    def startGame(self):

        while True:
            try:
                self.amtPlayers = int(input("How many people are playing? (7 players max.): "))
                
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
        self.pl_list.append(Gertrude("GERTRUDE")) 
        for i in range(self.amtPlayers):
            self.pl_list.append(Player(str(input("Player {:d}'s name is: ".format(i+1)))))
        
        return self.pl_list

    # Loop through all the players and there actions
    def round(self):
        # Repeat length of players minus gertrude
        
        print(f"--- Gertrude's hand ---")
        self.playerList[0].showHand()
        
        for player in self.playerList[1:]:
            print(f"\n--- {player.name}'s turn ---")
            print(f"--- {player.name}'s hand ---")
            player.showHand()

            while True:
                # Check if the player's turn has ended, and if so, end their turn and print their hand value
                if player.active == False:
                    print(f"{player.name} ends with a hand value of {player.check_cards()}.")
                    break

                # refresh availability each loop because the commands change
                enabled_moves = ["hit", "stand"]
                aliases = ["h", "s"]
                # if (player.can_split()):
                #     enabled_moves.append("split")
                #     aliases.append("sp")
                # if (player.can_double()):
                #     enabled_moves.append("double down")
                #     aliases.append("dd")
                enabled_moves.append("help")
                aliases.append("?")

                # Print what moves are available based on enabled key in moves dictionary
                print("Choose:", ", ".join(enabled_moves))

                choice = input("> ").strip().lower()

                if choice in enabled_moves or choice in aliases:
                    if choice in ["hit", "h"]:
                        player.hit(self.dealer)
                    elif choice in ["stand", "s"]:
                        player.stand()
                    # elif choice in ["split", "sp"]:
                    #     player.split(self.dealer)
                    # elif choice in ["double down", "dd"]:
                    #    player.double_down(self.dealer)
                    elif choice in ["help", "?"]:
                        print(player.help(enabled_moves + aliases))
                        continue
                    else:
                        print("Gertrude smiles menacingly: 'I don't know how you got here, but this shouldn't be possible. Try again.'")
                        continue

                    print(f"\n--- {player.name}'s hand ---")
                    player.check_cards()
                    player.showHand()
                else:
                    print("Gertrude raises an eyebrow: 'That's not a valid move. Try again.'")
                    
    # GERT-31 calculateWinner()
    # inputs: none
    # outputs: none
    # goals: a) using self.playerList, compare every human player score to Gertrude player's score using player.check_cards()
    #        b) reapportion player money based on player bets earlier (see resolve_bet() in Player.py for more information on format)
    #        c) GERT-30 call trashtalk() on the players who lose
    def calculateWinner(self, playerList):
        dealer = playerList[0] # exclude Gurtrude.dealer  
        dealerScore = dealer.check_cards()
        results = {}

        for player in playerList[1:]: 
            playerScore = player.check_cards()

            if playerScore > 21:
                results[player] = False 
                print(player.name, ", you bust!")
            elif dealerScore > 21:
                results[player] = True 
                print(player.name, ", you win! Dealer busts!")
            elif playerScore > dealerScore:
                results[player] = True 
                print(player.name, ", you win! you take all for having a higher score than the dealer!")
            elif playerScore < dealerScore:
                results[player] = False 
                print(player.name, ", you lose! Dealer takes all for a higher score!")
            else:
                results[player] = False
                print(player.name, ", push! You Tied with the dealer.")
        return results 

if __name__ == "__main__":
    game = Games()
    game.main()