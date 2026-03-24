"""
PLEASE READ

To run game:
    cd into: /app/src
    run: python -m cardgames.Games

Only add files individually and never use "git add ."
    run: git add file.py

Make sure to comment on everything new you make and ask if you need help or clarification
"""

from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        self.dealer = Dealer(self.deck)

        print('\nWelcome to the Gertrude\'s BlackJack!')

        # Sets up game and player list, which will be used for rounds
        self.playerList = self.startGame()

        while True:
            # Each player places bets
            for player in self.playerList[1:]:
                player.bet()

            # Each player and gertrude is given 2 cards
            self.dealer.dealCards(2, self.playerList)
            
            # Each player takes turn
            self.round()

            # Gertrude takes turn
            self.playerList[0].gertTurn(self.dealer)

            # Calculate results
            results = self.calculateWinner()

            # Give money to winner
            for player in results:
                player.resolve_bet(player, self.dealer)

            # Play again
            quit = input("\nPlay another round? (y/n): ").strip().lower()
            while quit not in ["y", "yes", "n", "no"]:
                quit = input("Not a valid input. Do you want to play another round? (y/n): ").strip().lower()
            if quit in ["n", "no"]:
                break
        
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
        self.pl_list.append(Player("GERTRUDE"))
        for i in range(self.amtPlayers):
            self.pl_list.append(Player(str(input("Player {:d}'s name is: ".format(i+1)))))
        return self.pl_list

    # Loop through all the players and there actions
    def round(self):
        # Repeat length of players minus gertrude
        for player in self.playerList[1:]:
            print(f"\n--- {player.name}'s turn ---")
            print(f"--- {player.name}'s hand ---")
            player.showHand()

            while True:
                # Check if the player's turn has ended, and if so, end their turn and print their hand value
                if (player.active == False):
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

                if (choice in enabled_moves or choice in aliases):
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
                    player.showHand()
                else:
                    print("Gertrude raises an eyebrow: 'That's not a valid move. Try again.'")

if __name__ == "__main__":
    game = Games()
    game.main()