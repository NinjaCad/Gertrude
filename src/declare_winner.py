from cardgames.Player import Player
def declare_winner(player1, player2):
    card1 = player1.chosen_card.value
    card2 = player2.chosen_card.value
    if card1 == 0 or card2 == 0: # someone is missing a card
        return None
    elif card1.compare(card2)==1: # player1 wins
        return player1
    elif card1.compare(card2)==-1: # player2 wins
        return player2
    elif card1.compare(card2)==0: # tie
        return player1, player2
