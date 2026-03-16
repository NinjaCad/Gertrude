
from flask import Flask, render_template, request
from global_card_change import global_card_change

app = Flask(__name__)

@app.route("/play_card", methods=["GET", "POST"])
def play_card():
    card = ""
    if request.method == "POST":
        card = global_card_change()

    return render_template("page_3.html", card=card)