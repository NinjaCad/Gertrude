from cardgames.Player import Player
def declare_winner(player1, player2):
    card1 = player1.chosen_card.value
    card2 = player2.chosen_card.value
    if card1 == 0 or card2 == 0: # someone is missing a card
        return None
    elif card1.value > card2.value: # player1 wins
        return player1
    elif card2.value > card1.value: # player2 wins
        return player2
    elif card1.value == card2.value: # tie
        return player1, player2
