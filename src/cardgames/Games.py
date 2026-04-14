import random

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
            if self.playerList[0].hand[0].value == 1:
                print(f"--- Gertrude's hand ---")
                self.playerList[0].showHand()
                for player in self.playerList[1:]:
                    player.bet("insurance")

            # Each player takes turn
            self.round()

            # Gertrude takes turn
            self.playerList[0].gertTurn(self.dealer)
            self.playerList[0].showHand()

            # Calculate results
            self.calculateWinner(self.playerList)
            
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

        while True:
            try:
                starting_money = int(input("Enter the amount of starting Money: $"))
                if starting_money <= 0:
                    print("Starting money must be more than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid  amount.")

        print('This round of blackjack will be played with {:d} players, against the dealer, GERTRUDE'.format(self.amtPlayers))

        self.pl_list = []
        self.pl_list.append(Gertrude("GERTRUDE")) 

        for i in range(self.amtPlayers):

            new_player = Player(str(input("Player {:d}'s name is: ".format(i+1))))

            new_player.money = starting_money

            self.pl_list.append(new_player)

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
                if (player.can_split()):
                    enabled_moves.append("split")
                    aliases.append("sp")
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
                        if player.check_cards() > 21:
                            print(self.playerList[0].trashTalk("bust")) #gert always talks when you bust (feel free to change (0.1-1.0))
                        else:
                            if random.random() < 0.30: #probablility of gert talking when you hit (feel free to change (0.1-1.0))
                                print(self.playerList[0].trashTalk("hit"))
                    elif choice in ["stand", "s"]:
                        player.stand()
                        if random.random() < 0.30: #probablility of gert talking when you stand (feel free to change (0.1-1.0))
                            print(self.playerList[0].trashTalk("stand"))

                    elif choice in ["split", "sp"]:
                        player.split(self.dealer)
                        if random.random() < 0.30: #probablility of gert talking when you split (feel free to change (0.1-1.0))
                            print(self.playerList[0].trashTalk("split"))
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
        dealer = playerList[0]
        dealerScore = dealer.check_cards()

        for player in playerList[1:]:
            playerScore = player.check_cards()

            if playerScore > 21:
                standard_result = False
                print(f"{player.name}, you bust!")
            elif dealerScore > 21:
                standard_result = True
                print(f"{player.name}, you win! Dealer busts!")
            elif playerScore > dealerScore:
                standard_result = True
                print(f"{player.name}, you win! You have a higher score than the dealer!")
            elif playerScore < dealerScore:
                standard_result = False
                print(f"{player.name}, you lose! Dealer has a higher score!")
            else:
                print(player.name, ", push! You Tied with the dealer.")
                player.bets["standard"] = 0
                continue
            
            # Calculate results and give money for perfect pairs
            player.resolve_bet({
                "standard": standard_result,
                "pairs": player.perfectPairs(),
                "insurance": player.insurance(self.playerList[0])
                # "21+3": player.twentyone(),
            })


if __name__ == "__main__":
    game = Games()
    game.main()