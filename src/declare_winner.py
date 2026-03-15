from cardgames.Player import Player
def declare_winner(player1, player2):
    card1 = player1.chosen_card
    card2 = player2.chosen_card
    try:
        if card1.compare(card2)==1: # player1 wins
            return player1.name
        elif card1.compare(card2)==-1: # player2 wins
            return player2.name
        else:
            return "It's a tie!"
    except TypeError: # tie
        print("Error: Both players must have chosen a card to declare a winner.")
