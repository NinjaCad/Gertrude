from cardgames.Player import *
from cardgames.Deck import *
from cardgames.Card_Compare import *
from cardgames.Dealer import *
from declare_winner import *
from cardgames.Games import HighCardDrawInstructions

# NOTEE: this show_cards function is supposed to show multiple cards, but it currently only shows one.
def show_cards(card: Card):
    face_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    card_name = face_names.get(card.value, card.value)
    
    display_text = f"--- {card_name} of {card.suit} ---\n"
    
    for line in card.image:
        display_text += line + "\n"
        
    return display_text

# print instructions
print(HighCardDrawInstructions.get("overview"))
print(HighCardDrawInstructions.get("winning"), "\n")

# initiate variables
player1 = Player("Player 1")
player2 = Player("Player 2")
deck = Deck()
deck.shuffle()
dealer = Dealer(deck)

# deal cards to players
dealer.dealCards(3, [player1, player2])

# display player 1's cards
for card in player1.hand:
    print(show_cards(card))
# player1 chooses a card
# I am waiting for the function that allows player to choose a card
# stand in code
player1.chosen_card = player1.hand[0]

# swap turn function
# I am also waiting on the code to switch turns
switch = input("Enter "s" to switch turns: ")
if switch == "s":
    print("Switched turns. Player 2's turn to choose a card.")
# player2 chooses a card
# stand in code
player2.chosen_card = player2.hand[0]

# display winner
winner = declare_winner(player1, player2)
print("The winner is: ", winner)

