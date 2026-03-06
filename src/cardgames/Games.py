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
        
        input('Press [Enter] to exit.')

    
    def startGame(self):
        deck = Deck()
        dealer = Dealer(deck)

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
        self.round(self.pl_list, dealer)


    # Loop through all the players
    # Parameters is a player list and a dealer object
    def round(self, players, dealer):
        # dealCards()      Need to reset player hands and hand out two cards per player

        # Repeat length of players minus gertrude
        for player in players:
            turn = True

            # Easy way to make new moves with dictionary
            moves = {
                "hit": {
                    "enabled": True,
                    "aliases": {"h"},
                    "action": player.hit,
                    "args": (dealer),
                },
                "stand": {
                    "enabled": True,
                    "aliases": {"s"},
                    "action": player.stand,
                    "args": (),
                },
                "split": {
                    "enabled": False,
                    "aliases": {"sp"},
                    #"action": player.split,
                    "args": (),
                },
                "doubleDown": {
                    "enabled": False,
                    "aliases": {"dd", "double down"},
                    #"action": player.doubleDown,
                    "args": (),
                },
                "help": {
                    "enabled": False, # True
                    "aliases": {"h", "?"},
                    #"action": player.help,
                    "args": (),
                },
                "quit": {
                    "enabled": False, # True
                    "aliases": {"q"},
                    #"action": player.quit,
                    "args": (),
                },
            }

            print(f"\n--- {player.name}'s turn ---")

            while turn:
                # refresh availability each loop
                #moves["split"]["enabled"] = player.can_split()
                #moves["doubleDown"]["enabled"] = player.can_double()

                player.showHand()

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
                    fn = moves[selected]["action"]
                    args = moves[selected]["args"]
                    fn(*args)

                    # Create a list with the values of the cards in the player's hand b/c the check_cards function in Player.py doesn't work
                    hand = []
                    for card in player.hand:
                        hand.append(card.value)

                    # Check if the player has busted by using the check_cards function in Player.py, and if they have, end their turn and show their hand and hand value
                    if (player.check_cards(hand) >= 21):
                        player.bust()
                    if (player.active == False):
                        player.showHand()
                        print(f"{player.name} ends with a hand value of {player.check_cards(hand)}.")
                        turn = False
                else:
                    print("Not a valid move.")

            # playerGertrude()        start gertrude's turn
            # calculateWinner()   end round and calculate winner

if __name__ == "__main__":
    game = Games()
    game.main()