from cardgames.Games import GAME_STATE
from cardgames.Player import Player

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

def win_check(players: "list[Player]"):
    first_player_to_slap = players[0]
    if len(first_player_to_slap.hand) == 0:
        print(f"{first_player_to_slap.name} won!")
        return True
    else:
        return False

# Renamed function for better readability.
def advance_turn(game_state, player_list):                                              #counter function
    """Increments counter and returns (rank, player_index)"""
    game_state['counter'] += 1
    current_count = game_state['counter']
    return current_count % 13, current_count % len(player_list)

def card_art(rank, suit):
    rank_str = str(rank)
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"
    if rank_str == "10":
        rank_left = rank_str + " " * 7
        rank_right = " " * 7 + rank_str
    else:
        rank_left = rank_str + " " * 8
        rank_right = " " * 8 + rank_str
    line1 = top
    line2 = f"│{rank_left}│"
    line3 = side
    line4 = f"│    {suit}    │"
    line5 = side
    line6 = f"│{rank_right}│"
    line7 = bottom
    return f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}"