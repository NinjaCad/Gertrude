"""
PLEASE READ BEFORE DOING ANYTHING

To run game:
    cd into: /app/src
    run: python -m cardgames.Games

Only add files individually and never use "git add ."
    run: git add file.py

Make sure to comment on whatever new function you make
"""

from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer

import random


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('\nWelcome to the Gertrude\'s BlackJack!')

        # Sets up game and player list, which will be used for rounds
        self.playerList = self.startGame()

        while True:
            # bet()
            # dealCards()
            self.round()

            # playerGertrude()        start gertrude's turn
            # calculateWinner()   end round and calculate winner

            break

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
        dealer = Dealer(self.deck) # Eventually this will be from the Gertrude object in player list

        # Repeat length of players minus gertrude
        for player in self.playerList[1:]:
            # Easy way to make new moves with dictionary
            moves = {
                "hit": {
                    "enabled": True,
                    "aliases": {"h"},
                    "action": lambda: player.hit(dealer),
                },
                "stand": {
                    "enabled": True,
                    "aliases": {"s"},
                    "action": player.stand,
                },
                "split": {
                    "enabled": False,
                    "aliases": {"sp"},
                    #"action": player.split,       doesnt exist yet
                },
                "Double Down": {
                    "enabled": False,
                    "aliases": {"dd"},
                    #"action": player.doubleDown,           doesnt exist yet
                },
                "help": {
                    "enabled": True,
                    "aliases": {"?"},
                    "action": None,
                },
                "quit": {
                    "enabled": True,
                    "aliases": {"q"},
                    "action": self.quit,
                },
            }
            print(f"\n--- {player.name}'s turn ---")
            print(f"--- {player.name}'s hand ---")
            #player.showHand()     right now its empty b/c dealCards() does'nt exist yet

            while True:
                # Check if the player's turn has ended, and if so, end their turn and print their hand value
                total = player.check_cards(player.hand)
                if (player.active == False):
                    print(f"{player.name} ends with a hand value of {total}.")
                    break
                
                # refresh availability each loop because the commands change
                #moves["split"]["enabled"] = (lambda: player.can_split())
                #moves["doubleDown"]["enabled"] = (lambda: player.can_double())
                moves["help"]["action"] = (lambda: self.help(player, moves))

                # Print what moves are available based on enabled key in moves dictionary
                enabled_moves = [n for n, info in moves.items() if info["enabled"]]
                print("Choose:", ", ".join(enabled_moves))

                choice = input("> ").strip().lower()

                # Check to see what move the player chose by comparing the name and the aliases
                selected = None
                for name, info in moves.items():
                    if choice == name.lower() or choice in info["aliases"]:
                        selected = name
                        break
                    
                # Use the selected move to call the appropriate function with the appropriate arguments and check enabled
                if selected and moves[selected]["enabled"]:
                    # Call the function associated with the move, if it has one
                    moves[selected]["action"]()

                    # Print hand only after valid move and it's not help or quit, because those dont change the hand
                    if selected not in ["help", "quit"]:
                        print(f"\n--- {player.name}'s hand ---")
                        player.showHand()
                else:
                    print("Not a valid move.")

    # Simple that prints the rules, the available commands, and the player's current hand and hand value
    def help(self, player: Player, moves: dict = {}):
        # Basics of the game
        print("""
BLACKJACK (21) - HOW TO PLAY:

GOAL:
Beat the dealer by getting closer to 21 without going over.

CARD VALUES:
  - Number cards (2–10) = face value
  - Face cards (J, Q, K) = 10
  - Ace = 1 or 11

SETUP:
  - You and the dealer each get 2 cards
  - Your cards are face up
  - Dealer has 1 face up, 1 face down

PLAYER ACTIONS:
  - Hit: Take another card
  - Stand: Keep your hand
  - Double Down: Double bet, take 1 card only
  - Split: If you have 2 matching cards, split into 2 hands

BUST:
  - If your total goes over 21, you lose immediately

DEALER RULES:
  - Dealer reveals hidden card after your turn
  - Must hit until at least 17
  - Must stand on 17 or higher

WINNING:
  - Higher than dealer without busting = win
  - Dealer busts = win
  - Lower than dealer = lose
  - Tie = push (bet returned)

BLACKJACK:
  - Ace + 10-value card
  - Best possible hand
  - Pays extra (usually 3:2)

TIPS:
  - Hit if under 12
  - Stand on 17+
  - Play aggressive if dealer has 7 or higher
  - Be cautious if dealer has 4–6
        """)
        # Print all the commands, their alternate name(s), and if they they can use it
        print("COMMANDS CURRENTLY AVAILABLE:")
        for name, info in moves.items():
            aliases = ", ".join(sorted(info.get("aliases", [])))
            status = "enabled" if info.get("enabled") else "disabled"
            if aliases:
                print(f"  - {name} ({aliases}) [{status}]")
            else:
                print(f"  - {name} [{status}]")
        
        # Print current hand
        print("\nCURRENT HAND:")
        player.showHand()

        # Create a list with the values of the cards in the player's hand b/c the check_cards function in Player.py only takes values
        #hand_values = [card.value for card in player.hand]
        #total = player.check_cards(hand_values)
        total = player.check_cards(player.hand)
        print("\nCURRENT HAND VALUE:", total)
        print()
    
    # Just some fun trash talk lines that gertrude can say for some reason
    def trashTalk(self):
        lines = [
        "Gertrude smirks: 'You call that a hand? I've seen better from a toddler.'",
        "Gertrude laughs: 'Bold move… unfortunately, a bad one.'",
        "Gertrude sighs: 'You sure you know the rules, or are you just guessing?'",
        "Gertrude grins: 'Go ahead, hit again. I love watching this.'",
        "Gertrude chuckles: 'Oh no… this isn't going to end well for you.'",
        "Gertrude raises an eyebrow: 'Risky. I almost respect it… almost.'",
        "Gertrude smirks: 'You’re making this way too easy for me.'",
        "Gertrude laughs softly: 'House always wins, sweetheart.'",
        "Gertrude leans in: 'You might want to rethink that strategy.'",
        "Gertrude shrugs: 'I’ll try not to embarrass you too much.'"
        ]
    
        print("\n" + random.choice(lines) + "\n")

    # Quit function that ends the game when the player inputs "quit" or "q"
    def quit(self):
        print("Quitting game. Goodbye!")
        raise SystemExit(0)

if __name__ == "__main__":
    game = Games()
    game.main()