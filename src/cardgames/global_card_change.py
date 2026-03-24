from cardgames.Games import GAME_STATE

def global_card_change():
    current_player = GAME_STATE["current_player"]
    if current_player is None or not current_player.hand:
        return "No card to play"
    
    GAME_STATE["current_card"] = current_player.hand.pop() # delete this line, uncomment the line below, after merge.
    # GAME_STATE["current_card"] = current_player.pop_card()
    current_card = GAME_STATE["current_card"]

    # Also to be replaced after merge
    return str(current_card)
    # return card_art(current_card.suit, current_card.value)