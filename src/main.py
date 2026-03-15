from cardgames.Player import *
from cardgames.Deck import *
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
dealer.dealCards(3, [player1, player2])

# player1 chooses a card
# stand in code
player1.chosen_card = player1.hand[0]

# swap turn function

# player2 chooses a card
# stand in code
player2.chosen_card = player2.hand[0]
winner = declare_winner(player1, player2)
print("The winner is: ", winner)
