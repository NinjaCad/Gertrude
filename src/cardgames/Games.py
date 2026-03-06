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
    # Parameters is a player list
    def round(self, players, dealer):
        # dealCards()      Need to reset player hands and hand out two cards per player

        # Repeat length of players minus gertrude
        for player in players:
            turn = True

            moves = {
                "hit": {
                    "enabled": True,
                    "aliases": {"h"},
                    "action": player.hit,
                    "args": (dealer,),
                },
                "stand": {
                    "enabled": True,
                    "aliases": {"s"},
                    "action": player.stand,
                    "args": (),
                },
                # "split": {
                #     "enabled": player.can_split(),
                #     "aliases": {"sp"},
                #     "action": player.split,
                #     "args": (),
                # },
                # "doubleDown": {
                #     "enabled": player.can_double(),
                #     "aliases": {"dd", "double down"},
                #     "action": player.doubleDown,
                #     "args": (),
                # },
                # "help": {
                #     "enabled": True,
                #     "aliases": {"h", "?"},
                #     "action": player.help,
                #     "args": (),
                # },
                #"quit": {
                #     "enabled": True,
                #     "aliases": {"q"},
                #     "action": player.quit,
                #     "args": (),
                # },
            }

            print(f"\n--- {player.name}'s turn ---")

            while turn:
                # refresh availability each loop
                #moves["split"]["enabled"] = player.can_split()
                #moves["doubleDown"]["enabled"] = player.can_double()

                player.showHand()

                enabled_moves = [n for n, info in moves.items() if info["enabled"]]
                print("Choose:", ", ".join(enabled_moves))

                choice = input("> ").strip().lower()

                selected = None
                for name, info in moves.items():
                    if choice == name.lower() or choice in info["aliases"]:
                        selected = name
                        break

                if selected and moves[selected]["enabled"]:
                    fn = moves[selected]["action"]
                    args = moves[selected]["args"]
                    fn(*args)

                    hand = []
                    for card in player.hand:
                        hand.append(card.value)

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