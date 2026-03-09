from operator import truediv
from ssl import Options

from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('\nWelcome to the Simple BlackJack!')
        self.playerList = self.startGame()
        # playerGertrude()        start gertrude's turn
        # calculateWinner()   end round and calculate winner
        
        input('Press [Enter] to exit.')
    
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
        #self.pl_list.append(Player("GERTRUDE")) #Player("GERTRUDE") will be eventually replaced
        self.round()


    # Loop through all the players
    # Parameters is a player list and a dealer object
    def round(self):
        dealer = Dealer(self.deck)
        
        # dealCards()      Need to reset player hands and hand out two cards per player

        # Repeat length of players minus gertrude (Currently gertrude is not part of the player list and just gets called in a seperate function)
        for player in self.pl_list:
            turn = True

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
                "doubleDown": {
                    "enabled": False,
                    "aliases": {"dd", "double down"},
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

            while turn:
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

                    # Print hand only after valid move
                    print(f"\n--- {player.name}'s hand ---")
                    player.showHand()

                    # Create a list with the values of the cards in the player's hand b/c the check_cards function in Player.py only takes values
                    hand_values = [card.value for card in player.hand]
                    total = player.check_cards(hand_values)

                    # Check if the player has busted by using the check_cards function in Player.py, and if they have, end their turn and show their hand value
                    if (total >= 21):
                        player.bust()

                    if (player.active == False):
                        print(f"{player.name} ends with a hand value of {total}.")
                        turn = False
                else:
                    print("Not a valid move.")

    def help(self, player, moves: dict):
        # Basics of the game
        print("\nHow to Play:")
        print("Each player tries to get as close to 21 as possible without going over.")
        print("Dealer must hit on 16 and stand on 17.")

        # Print all the commands, their alternate name(s), and if they they can use it
        print("\nCommands:")
        for name, info in moves.items():
            aliases = ", ".join(sorted(info.get("aliases", [])))
            status = "enabled" if info.get("enabled") else "disabled"
            if aliases:
                print(f"  - {name} ({aliases}) [{status}]")
            else:
                print(f"  - {name} [{status}]")
        
        # Create a list with the values of the cards in the player's hand b/c the check_cards function in Player.py only takes values
        hand_values = [card.value for card in player.hand]
        total = player.check_cards(hand_values)
        print("\nCurrent hand value:", total)
        print()

    def quit(self):
        print("Quitting game. Goodbye!")
        raise SystemExit(0)

if __name__ == "__main__":
    game = Games()
    game.main()

"""
To run game:
cd into to /app/src
python -m cardgames.Games
"""