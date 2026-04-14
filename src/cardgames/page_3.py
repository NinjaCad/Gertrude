from cardgames.Player import Player
import random

def global_card_change(game_state):
    current_player = game_state["current_player"]
    if current_player is None or not current_player.hand:
        return "No card to play"
    
    game_state["current_card"] = current_player.hand.pop() # delete this line, uncomment the line below, after merge.
    # game_state["current_card"] = current_player.pop_card()
    current_card = game_state["current_card"]

    # Also to be replaced after merge
    return str(current_card), game_state
    # return card_art(current_card.suit, current_card.value)

def win_check(players: "list[Player]"):
    first_player_to_slap = players[0]
    if len(first_player_to_slap.hand) == 0:
        # NOTE delete this print statement
        print(f"{first_player_to_slap.name} won!")
        return True
    else:
        return False

def increase_counter(game_state, player_list):                                              #counter function
    #"""Increments counter and returns (rank, player_index)"""
    #game_state['counter'] = 0
    game_state['counter'] += 1
    current_count = game_state['counter']
    return (current_count % 13)+1, current_count % len(player_list)

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

# RESOLVE SLAPS
def resolve_slap(game_state, player_list: "list[Player]"):
    slap_list = game_state["slap_list"]

    current_count = game_state["counter"]
    current_card_value = game_state["current_card"].get_value()

    # Shuffle the played cards to add to the player hand
    random.shuffle(game_state["played_cards"])
    
    # Default player for testing
    loser = player_list[0]  # delete this for the final submission

    valid_slap = (current_card_value == current_count)

    if valid_slap:
        if win_check(game_state["slap_list"]):
            winner = game_state["slap_list"][0].get_name()
            return winner, game_state
        elif len(slap_list) < len(player_list) - 1:
            # Uncomment this for final submisson
            # return 
            return loser, game_state # delete this for final submission
        else:
            loser = next(player for player in player_list if player not in slap_list)
    else:
        loser = slap_list[0]

    for card in game_state["played_cards"]:
        loser.add_card(card)

    # Reset the GAME_STATE variable
    game_state["played_cards"].clear()
    game_state["slap_list"].clear()
    game_state["slap_in_progress"] = False

    # UNCOMMENT FOR FINAL SUBMISSION
    # return game_state

    # Return statement for tests, to be deleted in final submission - but keep game_state
    return loser, game_state

    