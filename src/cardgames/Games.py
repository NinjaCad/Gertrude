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
GAME_STATE = {"current_card" : None, "current_player" : None}
last_player_joined = ""

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

@app.route("/game")
def game():
    return "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE

@app.route("/player-list-stream")
def player_stream():
    name = session['name']
    
    def player_list_stream():
        global last_player_joined
        last_player = last_player_joined

        with app.app_context():
            html = render_template('player_list_partial.html', name=name, player_list=player_list)
        yield f"data: {html}\n\n".encode("utf-8")

        while True:
            if last_player != last_player_joined:
                last_player = last_player_joined
                with app.app_context():
                    html = render_template('player_list_partial.html', name=name, player_list=player_list)
                yield f"data: {html}\n\n".encode("utf-8")
            time.sleep(0.1)
    return Response(player_list_stream(), mimetype="text/event-stream", direct_passthrough=True)

@app.route("/play_card", methods=["GET", "POST"])
def play_card():
    card = ""
    if request.method == "POST":
        card = global_card_change()

    return render_template("page_3.html", card=card)              #return rank and person who turn it is

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

