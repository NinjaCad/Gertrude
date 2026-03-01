import random
from cardgames.Player import Player

# Proof of concept
# FUTURE FEATURES:
# -limit number of players

# Player creation
def create_players(num_players, player_names):
     # List of Players
    positions = random.sample(range(num_players), num_players)
    players = []
    for i in range(num_players):
        angle = positions[i] * (360/num_players)
        players.append(Player(player_names[i], angle))

    # Remaining amount of cards after dealing to all players
    # This will be placed into the overall deck eventually
    cards_left = 52 % num_players

    return players, cards_left

# Game initialization loop
def start_game():
    print("Welcome to HEART ATTACK!")
    num_players = ""
    # Loop to get a valid number of players from user input
    while True:
        try:
            num_players = int(input("How many players will be joining? "))
            if num_players < 2:
                print("You need at least 2 players.")
            else:
                break
        except ValueError:
            print("That's not a valid number.")

    player_names = []
    for i in range(num_players):
        name = input(f"Enter a player name ({i+1}/{num_players}): ")
        player_names.append(name)

    players, cards_left = create_players(num_players, player_names)

    return player_names, num_players

if __name__ == "__main__":
    start_game()