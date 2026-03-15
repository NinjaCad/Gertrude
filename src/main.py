from src.cardgames.Player import *
from src.cardgames.Deck import *
from cardgames.Card_Compare import *
from cardgames.Deck import *
from cardgames.Player import *
from cardgames.Dealer import *
from declare_winner import *
from cardgames.Games import HighCardDrawInstructions


# print instructions
HighCardDrawInstructions.get("overview") 

# create 2 players and dealer
player1 = Player("Player 1")
player2 = Player("Player 2")

deck = Deck()
deck.shuffle()

# deal cards to players
dealer = Dealer(deck)
dealer.dealCards([player1, player2])

# player1 chooses a card

# swap turn function

# player2 chooses a card

# declare_winner(player1, player2)


