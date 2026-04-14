from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.page_1 import *
from cardgames.page_2 import *
from cardgames.page_3 import *

import random
import time
from typing import Dict, Any
from flask import Flask, render_template, url_for, Response, request, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "c78w93q2byaVYV9feab9dha7892vbgdsaooOGVDUGGIafd70Bhn1"

#The player objects will be appended to this list. 
player_list = []
GAME_STATE: Dict[str, Any] = {
    "current_card": None,
    "current_player": None,
    "played_cards": [],
    "slap_list": [],
    "slap_in_progress": False,
    "counter": 0
}
last_player_joined = None

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("page_1.html")
    elif request.method == 'POST':
        name = request.form.get("player_name")
        session['name'] = name
        player_list.append(Player(name))
        global last_player_joined
        last_player_joined = name
        return redirect(url_for('lobby'))

@app.route("/lobby", methods=['GET', 'POST'])
def lobby():
    if 'name' not in session:
        return redirect(url_for('home'))
    return render_template("page_2.html", name=session['name'], player_list=player_list)

@app.route("/game", methods=["GET", "POST"])
def game():
    global GAME_STATE
    card = ""
    #global GAME_STATE
    global player_list
    #player_list = [Player('Prof Lee')]          #this line to make testing the play_card() route more straightfoward; can be deleted when we merge
    # if request.method == "POST":
    #     card = global_card_change(GAME_STATE)
    # rank, player_turn = increase_counter(GAME_STATE, player_list)
    
    #return render_template("page_3.html", card=card, counter=(rank, player_turn))              #return rank and person who turn it is
    if request.method == "POST":
        # Don't let them play a card when a slap has happened
        if GAME_STATE["slap_in_progress"]:
            return
        card, new_state = global_card_change(GAME_STATE)
        GAME_STATE = new_state

    return render_template("page_3.html", card=card)

@app.route("/player-list-stream")
def player_stream():
    name = session['name'] # ASSIGNS EACH SESSION A STREAM
    def player_list_stream(): #GENERATOR TO YIELD NEW HTML PAGES
        global last_player_joined
        last_player = last_player_joined # RESETTING LAST PLAYER JOINED TO UPDATE ON NEED BASE
        with app.app_context():
            html = render_template('player_list_partial.html', name=name, player_list=player_list) # RENDERS LIST AFTER INITIAL JOIN
        yield f"data: {html}\n\n".encode("utf-8") # YIELDS INITIAL LIST
        while True:
            if last_player != last_player_joined:
                last_player = last_player_joined # CHECKING FOR PLAYER JOIN
                with app.app_context():
                    html = render_template('player_list_partial.html', name=name, player_list=player_list) # RENDERS NEW LIST
                yield f"data: {html}\n\n".encode("utf-8") # YIELDS NEW LIST
            time.sleep(0.1) # BUFFER
    return Response(player_list_stream(), mimetype="text/event-stream", direct_passthrough=True) # RETURNING THE GENERATOR


# @app.route("/play_card", methods=["GET", "POST"])
# def play_card():
#     card = ""
#     if request.method == "POST":
#         card = global_card_change(GAME_STATE)

# COLLECT SLAPS
@app.route("/slap", methods=["POST"])
def slap():
    global GAME_STATE

    # Start slap phase if first slap
    if not GAME_STATE["slap_in_progress"]:
        GAME_STATE["slap_in_progress"] = True
    
    # Append the player name to the slap list
    player = next(player for player in player_list if player.get_name() == session.get("name"))
    # Just in case someone slaps again faster than the POST request to disable their slap button
    if player not in GAME_STATE["slap_list"]:
        GAME_STATE["slap_list"].append(player)

    # UNCOMMENT FOR FINAL SUBMISSION
    # GAME_STATE = resolve_slap(GAME_STATE, player_list)

    # Don't redirect yet
    return ("", 204)  


@app.route("/start_game", methods=["GET", "POST"])
def start_game():
    global player_list
    #if request.method == 'GET':
    #player_list = [Player('Prof Lee')]          #this line to make testing start_game() route more straightforward; can be deleted when we merge
    Dealer(Deck()).deal_cards(player_list)        #some players might get extra cards
    for i, player in enumerate(player_list):
        player.set_angle(360//len(player_list) * i)       #sets the angle of the player around the deck
    card = ""
    return render_template("page_3.html", players=player_list, card=card, counter=(1, 0))       #displays players, card, and counter--counter=(rank, player_index)

@app.route("/win_page")
def win_page():
    global player_list
    global GAME_STATE
    winner, GAME_STATE = resolve_slap(GAME_STATE, player_list)
    return render_template("page_4.html", winner=winner)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

