from cardgames.Player import Player
def declare_winner(player1, player2):
    card1 = player1.chosen_card
    card2 = player2.chosen_card
    if card1.value > card2.value:
        print("Player 1 wins with " + card1.name)
        return player1
    elif card2.value > card1.value:
        print("Player 2 wins with " + card2.name)
        return player2
    elif card1.value == card2.value & (card1.value != 0 | card2.value != 0):
        print("It's a tie! Both players have a(n)" + card1.name)
        return player1, player2
    else:
        print("No winner could be determined. One or more players may be missing a card.")
        return None
