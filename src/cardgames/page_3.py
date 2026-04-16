from cardgames.Player import Player
import random

def global_card_change(game_state):
    current_player = game_state["current_player"]
    if current_player is None or not current_player.hand:
        return "No card to play", game_state
    
    
    current_card = current_player.hand.pop()
    game_state["played_cards"].append(current_card) 
    game_state["current_card"] = current_card

    art = card_art(current_card.get_value(), current_card.get_suit())

    return art, game_state

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

    suit_symbols = { "Spades": "♠", "Clubs": "♣" , "Hearts": "♥", "Diamonds": "♦"}
    suit_symbol = suit_symbols.get(suit, suit)
    
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
    line4 = f"│    {suit_symbol}    │"
    line5 = side
    line6 = f"│{rank_right}│"
    line7 = bottom
    return f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}"

def resolve_slap(game_state, player_list: "list[Player]"):
    slap_list = game_state["slap_list"]
    
    # Card value check with match_rank from GAME_STATE
    current_match_value = str(game_state['match_rank'])
    actual_card_value = str(game_state["current_card"].get_value())
    valid_slap = (actual_card_value == current_match_value)

    if valid_slap:
        if len(slap_list) >= len(player_list) - 1:
            loser = next((p for p in player_list if p not in slap_list), slap_list[-1])
        else:
            return game_state, None # Don't resolve until enough people slap
    else:
        loser = slap_list[0]

    for card in game_state["played_cards"]:
        loser.add_card(card)

    # clear the deck and re-enable the play button
    game_state["played_cards"].clear()
    game_state["slap_list"].clear()
    game_state["slap_in_progress"] = False # This is what makes the buttons work again
    game_state["current_card"] = None

    # always return just the state so the route updates
    return game_state, loser