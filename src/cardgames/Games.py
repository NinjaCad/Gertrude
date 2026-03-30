from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.page_1 import *
from cardgames.page_2 import *
from cardgames.page_3 import *
import random
from flask import Flask, render_template, url_for, Response, request, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "c78w93q2byaVYV9feab9dha7892vbgdsaooOGVDUGGIafd70Bhn1"

#The player objects will be appended to this list. 
player_list = []
GAME_STATE = {"current_card" : None, "current_player" : None, "counter" : 0}
slap_list = []          #This list appends the players in the order they slapped the deck (not yet implemented).

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
    global GAME_STATE
    global player_list
    player_list = [Player('Prof Lee')]          #this line to make testing the play_card() route more straightfoward; can be deleted when we merge
    if request.method == "POST":
        card = global_card_change(GAME_STATE)
    counter = increase_counter(GAME_STATE, player_list)
    
    return render_template("page_3.html", card=card, counter=counter)              #return rank and person who turn it is

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

