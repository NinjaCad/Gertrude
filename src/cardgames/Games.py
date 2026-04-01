from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.page_1 import *
from cardgames.page_2 import *

import random
from flask import Flask, render_template, url_for, Response, request, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "c78w93q2byaVYV9feab9dha7892vbgdsaooOGVDUGGIafd70Bhn1"

#The player objects will be appended to this list. 
# "counter":
# - increments each turn in play_card() (Games.py) and drives game flow
# - uses counter logic defined in page_3.py
player_list = []
GAME_STATE = {"current_card" : None, "current_player" : None, "counter" : 0}


# Temporary workaourd due to circular imports.
from cardgames.page_3 import *


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

@app.route("/game")
def game():
    return "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            yield "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE
    return Response(event_stream(), mimetype="text/event-stream")



@app.route("/play_card", methods=["GET", "POST"])
def play_card():
    card = ""
    rank = None

    if request.method == "POST" and player_list:
        rank, player_index = blank(GAME_STATE, player_list)
        GAME_STATE["current_player"] = player_list[player_index]
        card = global_card_change()

    current_player_name = GAME_STATE["current_player"].name if GAME_STATE["current_player"] else "No player"

    # return rank (of the global card), current player turn, and last card played
    return render_template("page_3.html", rank=rank, card=card, current_player=current_player_name)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

