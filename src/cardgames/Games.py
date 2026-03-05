from operator import truediv
from ssl import Options

from cardgames.Deck import Deck
#from cardgames.Player import Player
#from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Simple BlackJack!')
        self.playerList = self.startGame()
        
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
        self.pl_list.append(Player("GERTRUDE")) #Player("GERTRUDE") will be eventually replaced
        self.round(self.pl_list)


    # Loop through all the players
    # Parameters is a player list
    def round(self, players):
        # dealCards()      Need to reset player hands and hand out two cards per player

        # Repeat length of players minus gertrude
        for player in players:
            turn = True

            moves = {
                "hit": {
                    "enabled": True,
                    "aliases": {"h"},
                    "action": player.hit,
                },
                "stand": {
                    "enabled": True,
                    "aliases": {"s"},
                    "action": player.stand,
                },
                "split": {
                    "enabled": player.can_split(),
                    "aliases": {"sp"},
                    "action": player.split,
                },
                "doubleDown": {
                    "enabled": player.can_double(),
                    "aliases": {"dd", "double down"},
                    "action": player.doubleDown,
                },
                "help": {
                    "enabled": True,
                    "aliases": {"h", "?"},
                    "action": player.help,
                },
            }

            print(f"\n--- {player.name}'s turn ---")

            while turn:
                # refresh availability each loop
                moves["split"]["enabled"] = player.can_split()
                moves["doubleDown"]["enabled"] = player.can_double()

                enabled_moves = [n for n, info in moves.items() if info["enabled"]]
                print("Choose:", ", ".join(enabled_moves))

                choice = input("> ").strip().lower()

                selected = None
                for name, info in moves.items():
                    if choice == name.lower() or choice in info["aliases"]:
                        selected = name
                        break

                if selected and moves[selected]["enabled"]:
                    moves[selected]["action"]()

                    if player.status:
                        turn = False
                else:
                    print("Not a valid move.")

            # playerGertrude()        start gertrude's turn
            # calculateWinner()   end round and calculate winner

if __name__ == "__main__":
    game = Games()
    game.main()
 
 

