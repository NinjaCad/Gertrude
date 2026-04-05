from flask import Flask, render_template, request
from cardgames.Games import GAME_STATE
from global_card_change import global_card_change 
from cardgames.Games import players_list 
def get_button_status(local_player, game_state, last_said_value):
    is_my_turn = (game_state.get("current_player") == local_player)
    is_match = False
    if game_state.get("current_card") is not None:
        # Assuming last_said_value is the rank to match
        is_match = (game_state["current_card"].value == last_said_value)
    return (not is_my_turn) or is_match
@app.route("/play_card", methods=["GET", "POST"])
def play_card():
    me = players_list[0] 
    announced_rank = GAME_STATE.get('last_said', None) 
    if request.method == "POST":
        global_card_change()
    disabled = get_button_status(me, GAME_STATE, announced_rank)
    return render_template("page_3.html", 
                           card=GAME_STATE["current_card"], 
                           is_disabled=disabled)