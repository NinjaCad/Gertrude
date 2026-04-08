from flask import Flask, render_template, request, session
from global_card_change import global_card_change 
from cardgames.Games import players_list 
def get_button_status(local_player, game_state, last_said_value):
    is_my_turn = (game_state.get("current_player") == local_player)
    is_match = False
    if game_state.get("current_card") is not None:
        is_match = (game_state["current_card"].value == last_said_value)
    return (not is_my_turn) or is_match
@app.route("/play_card", methods=["GET", "POST"])
def play_card(game_state): # Pass game_state in as a variable
    player_id = session.get('player_id', 0) 
    me = players_list[player_id] 
    announced_rank = game_state.get('last_said', None) 
    if request.method == "POST":
        global_card_change()
    disabled = get_button_status(me, game_state, announced_rank)
    return render_template("page_3.html", 
                           card=game_state["current_card"], 
                           is_disabled=disabled)