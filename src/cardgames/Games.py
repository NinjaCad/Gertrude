from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
import random
from flask import Flask, render_template, url_for, Response

player_list = ["Rose", "Joseph", "Daniel"] #PLACEHOLDER TO BE REMOVED

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>PLACEHOLDER</h1>"

@app.route("/lobby")
def lobby():
    return render_template("Page_2.html", playerList=player_list)

@app.route("/game")
def game():
    return "<h1>PLACEHOLDER</h1>"

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            yield "<h1>PLACEHOLDER</h1>"
    return Response(event_stream(), mimetype="text/event-stream")

def win_check(players: "list[Player]"):
    first_player_to_slap = players[0]
    if len(first_player_to_slap.hand) == 0:
        print(f"{first_player_to_slap.name} won!")
        return True
    else:
        return False

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)