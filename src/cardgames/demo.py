from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Player:
    def __init__ (self, name: str):
        self.name = name

player_list = []

def unique_name_generator(name: str, player_list: list) -> str:
    existing_names = [player.name for player in player_list]
    if name not in existing_names:
        return name
    
    else:
        name_counter = 2
        while f"{name}_#{name_counter}" in existing_names:
            name_counter += 1
        return f"{name}_#{name_counter}"
    

@app.route("/")
def home():
    return render_template("page_1.html")

@app.route("/join", methods=["POST"])
def join():
    name = request.form["player_name"].strip()
    unique_name = unique_name_generator(name, player_list)
    new_player = Player(unique_name)
    player_list.append(new_player)
    return redirect(url_for("page_2.html"))

@app.route("/page_2")
def waiting_room():
    names = [player.name for player in player_list]
    return f"Players in waiting room: {', '.join(names)}"

if __name__ == "__main__":
    app.run(debug=True)
