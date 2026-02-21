from cardgames.Player import Player
def declare_winner(player1, player2):
    card1 = player1.chosen_card
    card2 = player2.chosen_card
    if card1.value == 0 or card2.value == 0:
        print("One or more players are missing a card. Cannot determine winner.")
        return None
    elif card1.value > card2.value:
        print("Player 1 wins!")
        return player1
    elif card2.value > card1.value:
        print("Player 2 wins!")
        return player2
    elif card1.value == card2.value & (card1.value != 0 | card2.value != 0):
        print("It's a tie!")
        return player1, player2

