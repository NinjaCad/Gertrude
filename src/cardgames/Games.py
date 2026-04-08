from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.page_1 import *
from cardgames.page_2 import *
from cardgames.page_3 import *
import random
import time
from flask import Flask, render_template, url_for, Response, request, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "c78w93q2byaVYV9feab9dha7892vbgdsaooOGVDUGGIafd70Bhn1"

#The player objects will be appended to this list. 
player_list = []
GAME_STATE: Dict[str, Any] = {
    "current_card": None,
    "current_player": None,
    "played_cards": [],
    "slap_dict": {},
    "slap_in_progress": False,
    "slap_start_time": None,
    "counter": 0
}

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("page_1.html")
    elif request.method == 'POST':
        name = request.form.get("player_name")
        session['name'] = name
        player_list.append(Player(name))
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
    if request.method == "POST":
        # Don't let them play a card when a slap has happened
        if GAME_STATE["slap_in_progress"]:
            return
        card, new_state = global_card_change(GAME_STATE)
        GAME_STATE = new_state

    return render_template("page_3.html", card=card)

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            yield "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE
    return Response(event_stream(), mimetype="text/event-stream")


# @app.route("/play_card", methods=["GET", "POST"])
# def play_card():
#     card = ""
#     if request.method == "POST":
#         card = global_card_change(GAME_STATE)

# COLLECT SLAPS
@app.route("/slap", methods=["POST"])
def slap():
    global GAME_STATE
    player_name = session.get("name")
    timestamp = float(request.form.get("timestamp", 0))

    # Start slap phase if first slap
    if not GAME_STATE["slap_in_progress"]:
        GAME_STATE["slap_in_progress"] = True
        GAME_STATE["slap_start_time"] = time.time()

    # Record slap
    GAME_STATE["slap_dict"][player_name] = {"time": timestamp}

    # Don't redirect yet
    return ("", 204)  

# CHECK IF ENOUGH TIME HAS PASSED TO RESOLVE SLAPS (2 seconds)
@app.route("/check_slap")
def check_slap():
    global GAME_STATE
    if GAME_STATE["slap_in_progress"]:
        elapsed = time.time() - GAME_STATE["slap_start_time"]

        if elapsed >= 2:
            new_state, _, _ = resolve_slap(GAME_STATE, player_list)
            GAME_STATE = new_state
            return {"status": "resolved"}

        return {"status": "waiting"}

    return {"status": "idle"}

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


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

