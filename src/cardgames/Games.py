from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
import random
import time
import sys
import os

class Games:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(Deck())

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def slow_Print(text, delay=0.03):
        for char in text:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def show_Title():
        print(r"""
        ========================================
    
██╗     ███████╗████████╗███████╗    ███████╗██╗███████╗██╗  ██╗██╗
██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██║██╔════╝██║  ██║██║
██║     █████╗     ██║   ███████╗    █████╗  ██║███████╗███████║██║
██║     ██╔══╝     ██║   ╚════██║    ██╔══╝  ██║╚════██║██╔══██║╚═╝
███████╗███████╗   ██║   ███████║    ██║     ██║███████║██║  ██║██╗
╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝
                                                                                                                                                 
        ========================================
    A Card Game of Chance, Choice, & Everything Inbetween
        ========================================
    """)

    def opening_Sequence():
        show_Title()

        lines = [
            "The cards are shuffled...",
            "Your opponents are ready...",
            "Time to test your luck..."
        ]

        for line in lines:
            slow_Print(line, 0.04)
            time.sleep(0.3)

        slow_Print("\nWelcome to Let's Fish!\n", 0.05)

    def show_Rules():
        print("\n========== HOW TO PLAY ==========")
        print("- Each player takes a turn, asking a player for a card rank (e.g., 'Aces') or drawing a card from the deck.")
        print("- If the chosen player has the requested card, they must give ALL of them.")
        print("- If not... fishing time! Draw a single card from the deck.")
        print("- The player who has the most matching sets at the end of the game wins!")
        print("(The game draws to a close as the deck empties and every card set finds their pairs).")
        print("================================\n")

    def main_Menu():
        while True:
            print("\n1. Start Game")
            print("2. How to Play")
            print("3. Quit")

            choice = input("\nChoose an option: ")

            if choice == "1":
                return "Starting game..."
            elif choice == "2":
                show_Rules()
            elif choice == "3":
                print("Bye bye!")
                exit()
            else:
                print("Please enter '1', '2', or '3'.\n")

    def run_Game():
        clear()
        opening_Sequence()
        choice = main_Menu()
        
        if choice == "Starting game...":
            print("\nStarting game...\n")

    def create_players(self):
        players = []
        acceptedPlayerCount = [2,3,4]
        playerNames = []
        while True:
            try:
                # Creates between 2 and 4 players
                numOfPlayers = int(input("Enter amount of players (2-4): "))
                if numOfPlayers in acceptedPlayerCount:

                    # Inputting player name
                    for i in range(numOfPlayers):
                        while True:
                            player = input(f"Enter name of player {i + 1}: ")
                            if player.strip() == '':
                                print("Please enter a name.")
                            elif player in playerNames:
                                print("Name must be unique!")
                            elif len(player) > 16:
                                print("Name is too long! Must be under 17 characters.")
                            else:
                                players.append(Player(player))
                                playerNames.append(player)
                                break
                    break
                else:
                    print("Must be a positive integer between 2 and 4!")
            except ValueError:
                print("Must be a valid number!")
        return players
    
    def showOpponentsHands(self, players):
        for player in players:
            if player.isTurn or player.hand == []: # Skips the player whos turn it is, as well as players with empty hands
                continue
            
            print(f'{player.name}\'s hand:')
            knownCardsStore = player.knownCards
            player.knownCards = [False] * len(player.knownCards) # Changes cards in opponents' hands to not be visible

            player.showHand()
            print()

            player.knownCards = knownCardsStore # Reverses cards to be visible
    
    def start_game(self, players):
        playerlist = players[:]
        random.shuffle(playerlist)
        turn_list = playerlist

        if len(players) < 4:
            cardsdealt = 7
        else:
            cardsdealt = 5
        self.dealer.dealCards(cardsdealt, turn_list)
        list.reverse(turn_list) #last dealt goes first

        return turn_list

            
    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players) #player[0] in list goes first.
        
        game_running = True #game essentially runs forever. logic is needed to state when the game ends!!!!
        while game_running:
            for player in turn_list:
                player.isTurn = True
                print(f"\n{player.name}'s turn")
        #for each player in the turn list:
            #that player takes a turn
                if len(self.dealer.deck.size) == 0:
                    print("Draw pile is empty. Cannot pick up new cards.")
                else:
                    while True:
                        choice = input("Do you want to draw a card? (y/n)").lower()
                        if choice == 'y':
                            card = self.dealer.deck.getCard()
                            player.hand.append(card) #we're assuming the player has a hand
                            print(f"You drew: {card}")
                            break
                        elif choice == 'n':
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                
                #print("Next, choose a player to ask and a card value") would come next                    
                #end of player's turn
                player.isTurn = False
    
        input('Press [Enter] to exit.')

        print('First 5 cards in standard 52-card deck:')
        self.deck = Deck() #deck is created here; deck knows how, games decides when
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py

        for card in self.deck.cards[:5]:
            print(card)
        print('Press [Enter] to exit.')

if __name__ == "__main__":
    game = Games()
    game.main()