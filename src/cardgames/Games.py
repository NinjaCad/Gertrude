from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
import random
from flask import Flask, render_template, url_for, Response

app = Flask(__name__)

GAME_STATE = {"current_card" : None, "current_player" : None}

@app.route("/")
@app.route("/home")
def home():
    return "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE

@app.route("/lobby")
def lobby():
    return render_template("page_2.html", playerList=player_list)

@app.route("/game")
def game():
    return "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            yield "<h1>PLACEHOLDER</h1>" #REPLACE PLACEHOLDER WITH HTML PAGE
    return Response(event_stream(), mimetype="text/event-stream")

#The player objects will be appended to this list. 
players_list = []

def win_check(players: "list[Player]"):
    first_player_to_slap = players[0]
    if len(first_player_to_slap.hand) == 0:
        print(f"{first_player_to_slap.name} won!")
        return True
    else:
        return False

def blank(game_state, player_list):                                              #counter function
    """Increments counter and returns (rank, player_index)"""
    game_state['counter'] += 1
    current_count = game_state['counter']
    return current_count % 13, current_count % len(player_list)                  #return rank and person who turn it is

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)

