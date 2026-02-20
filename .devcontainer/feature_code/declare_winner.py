from src.cardgames import *;
function declare_winner(player1, player2):
    card1 = player1.chosen_card;
    card2 = player2.chosen_card;
    if card1.value > card2.value:
        return "Player 1 wins with " + card1.name
    elif card2.value > card1.value:
        return "Player 2 wins with " + card2.name
    else:
        return "It's a tie! Both players have a(n)" + card1.name    
