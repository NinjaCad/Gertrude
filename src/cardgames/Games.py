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
        self.dealer = Dealer(self.deck)
        self.playerList = [ ]

    def main(self):
        """
        Main game loop
        """

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
            self.playerList[0].knownCards = [True for _ in self.playerList[0].knownCards]
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
                for i in range(len(self.playerList)-1, -1, -1):
                    
                    player = self.playerList[i]
                    player.active = True
                    player.clearHand()
                    
                    if "right hand" in player.name:
                        del self.playerList[i]
                        
                self.deck.reset()
                self.deck.shuffle()
        
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
            
            name = str(input("Player {:d}'s name is: ".format(i+1)))
            # to avoid conflicts with checks when dealing with player.split() and Games.round() when split
            while "left hand" in name:
                name = str(input("Your name cannot contain the phrase 'left hand'. Please put in a new name: "))
            new_player = Player(name)

            new_player.money = starting_money

            self.pl_list.append(new_player)

        return self.pl_list

    # Loop through all the players and there actions
    def round(self):
        # Repeat length of players minus gertrude
        i = 1
        while True:
            player = self.playerList[i]
            
            # show everyone's current hand for convenience
            for playerH in self.playerList:
                playerH.showHand()
            
            print(f"\n=== {player.name}'s turn ===")
            player.showHand()
            
            # hit if first turn for right hand after split
            if "right hand" in player.name:
                player.hit(self.dealer)
                player.check_cards()
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
                if (player.can_double()):
                    enabled_moves.append("double down")
                    aliases.append("dd")
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
                    elif choice in ["split", "sp"]:
                        player.split(self)
                        print([player.name for player in self.playerList])
                    elif choice in ["double down", "dd"]:
                       player.double_down(self.dealer)
                    elif choice in ["help", "?"]:
                        print(player.help(enabled_moves + aliases))
                        continue
                    else:
                        print("Gertrude smiles menacingly: 'I don't know how you got here, but this shouldn't be possible. Try again.'")
                        continue

                    player.check_cards()
                    player.showHand()
                else:
                    print("Gertrude raises an eyebrow: 'That's not a valid move. Try again.'")
            
            # iterate to next player and check if we are at the end of the list
            i += 1
            if i == len(self.playerList):
                break
                    
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
            
            # unique resolve_bet run if there was a split
            if "right hand" in player.name:
                player = playerList[playerList.index(player) - 1]
                player.resolve_bet( { "split": standard_result } )
            else:
                # Calculate results and give money for perfect pairs
                player.resolve_bet({
                    "standard": standard_result,
                    "pairs": player.perfectPairs(),
                    "insurance": player.insurance(self.playerList[0])
                    # "21+3": player.twentyone(),
                })
            
            # reset player name to original name (without 'left hand'/'right hand') (for split only)
            if "left hand" in player.name:
                player.name = player.name[:-12]
            elif "right hand" in player.name:
                player.name = player.name[:-13]


if __name__ == "__main__":
    game = Games()
    game.main()