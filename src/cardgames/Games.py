from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.page_1 import *
from cardgames.page_2 import *
from cardgames.page_3 import *


import json
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
    "current_art": "",
    "match_rank": 1,
    "current_player": None,
    "played_cards": [],
    "slap_list": [],
    "slap_in_progress": False,
    "counter": 0,
    "game_started": False,
    "game_won": False,
    "winner": None
}
last_player_joined = None

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("page_1.html")
    
    elif request.method == 'POST':
        name = request.form.get("player_name", "").strip()

        # length check
        if not (1 <= len(name) <= 12):
            return render_template("page_1.html", error="Name must be 1 to 12 characters.")
        
        # uniqueness check (case-insensitive)
        if any(p.name.lower() == name.lower() for p in player_list):
            return render_template("page_1.html", error="Name is already taken.")

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
    global GAME_STATE, player_list

    if not player_list:
        return redirect(url_for('home'))

    if not GAME_STATE["game_started"]:
        GAME_STATE["game_started"] = True
        dealer = Dealer(Deck())
        dealer.deal_cards(player_list)

    if not GAME_STATE.get("current_player") and player_list:
        GAME_STATE["current_player"] = player_list[0]

    current_turn_player = GAME_STATE["current_player"]

    if request.method == "POST":
        user_name = session.get('name')
        current_turn_player = GAME_STATE["current_player"]

        #stop players from playing when not their turn
        if user_name != current_turn_player.get_name():
            return redirect(url_for('game'))


        is_match = (GAME_STATE["current_card"] is not None and 
                    str(GAME_STATE["current_card"].value) == str(GAME_STATE["match_rank"]))
        #stop players from playing when slap possible
        if is_match or GAME_STATE["slap_in_progress"]: # check naming if issues
            return redirect(url_for('game'))

        art, new_state = global_card_change(GAME_STATE)
        rank_to_match, next_idx = increase_counter(GAME_STATE, player_list)

        GAME_STATE = new_state
        GAME_STATE["current_art"] = art
        GAME_STATE['match_rank'] = rank_to_match
        GAME_STATE["current_player"] = player_list[next_idx]

    return render_template("page_3.html",
                        card=GAME_STATE.get("current_art", ""),
                        rank=GAME_STATE.get("match_rank", 1),
                        current_player=GAME_STATE["current_player"].get_name(),
                        current_turn_name=current_turn_player.get_name())
     
@app.route("/game-start-stream")
def game_start_stream():
    def stream():
        game_started_sent = False
        while not GAME_STATE["game_started"]:
            time.sleep(0.1)
        yield f"data: start\n\n"
    return Response(stream(), mimetype="text/event-stream")

@app.route("/game-update-stream")
def game_update_stream():
    def stream():
        last_card = None
        while True:
            current_card = GAME_STATE.get("current_card")
            if current_card != last_card:
                last_card = current_card
                yield "data: update\n\n"
            time.sleep(0.5)
    return Response(stream(), mimetype="text/event-stream")

@app.route("/game-sync-stream")
def game_sync_stream():
    def stream():
        while True:
            current_card_value = GAME_STATE["current_card"].get_value() if GAME_STATE["current_card"] else None
            sync_data = {
                "current_turn_name": GAME_STATE["current_player"].get_name() if GAME_STATE["current_player"] else "",
                "slap_in_progress": GAME_STATE["slap_in_progress"],
                "last_card_art": GAME_STATE.get("current_art", ""),
                "match_rank": GAME_STATE.get("match_rank", 1),
                "current_card_value": current_card_value
            }

            yield f"data: {json.dumps(sync_data)}\n\n"
            time.sleep(0.5)

    return Response(stream(), mimetype="text/event-stream")


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


# COLLECT SLAPS

# Route to check if page_3 needs to be changed
@app.route("/check_slap")
def check_slap():
    status = "waiting" if GAME_STATE["slap_in_progress"] else "active"
    return {"status": status}

@app.route("/slap", methods=["POST"])
def slap():
    global GAME_STATE, player_list
    player_name = session.get("name")

    slapper = next(player for player in player_list if player.get_name() == player_name)
    is_valid_slap = GAME_STATE["current_card"] and str(GAME_STATE["current_card"].value) == str(GAME_STATE["match_rank"])

    if not is_valid_slap:
        for card in GAME_STATE["played_cards"]:
            slapper.add_card(card)

        GAME_STATE["played_cards"].clear()
        GAME_STATE["current_card"] = None
        GAME_STATE["current_art"] = ""

        return ("", 204)

    # Start slap phase if first slap
    if not GAME_STATE["slap_in_progress"]:
        GAME_STATE["slap_in_progress"] = True
        GAME_STATE["slap_list"] = []
    
    # Append the player name to the slap list
    if slapper not in GAME_STATE["slap_list"]:
        GAME_STATE["slap_list"].append(slapper)

    if len(GAME_STATE["slap_list"]) == len(player_list):
        GAME_STATE, player = resolve_slap(GAME_STATE, player_list)
        if win_check(player_list):
            GAME_STATE["winner"] = player
            GAME_STATE["game_won"] = True
        else: 
            rank_to_match, next_idx = increase_counter(GAME_STATE, player_list)
            GAME_STATE["current_art"] = ""
            GAME_STATE["current_player"] = player_list[next_idx]
            GAME_STATE["match_rank"] = rank_to_match

    return ("", 204)

@app.route("/win_stream")
def game_is_won():
    def stream():
        while GAME_STATE["game_started"]:
            if GAME_STATE["game_won"]:
                yield "data: win\n\n"
                break
            time.sleep(0.1)
        return Response(stream(), mimetype='text/event-stream')  

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
    GAME_STATE, winner_name = resolve_slap(GAME_STATE, player_list)
    return render_template("page_4.html", winner=GAME_STATE["winner"])

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, threaded=True, debug = True)
    #remove the debug before merge

