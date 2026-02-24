import random
from cardgames.Player import Player

# Proof of concept
# TO BE ADDED: 
# -list of player objects
# -limit number of players

# Game initialization loop
def start_game():
    print("Welcome to HEART ATTACK!")
    numPlayers = ""
    # Loop to get a valid number of players from user input
    while True:
        try:
            numPlayers = int(input("How many players will be joining? "))
            if numPlayers < 2:
                print("You need at least 2 players.")
            else:
                break
        except ValueError:
            print("That's not a valid number.")

    # List of Players
    positions = random.sample(range(numPlayers), numPlayers)
    players = []
    for i in range(numPlayers):
        name = input(f"Enter a player name ({i+1}/{numPlayers}): ")
        # Angle for display location when HTML is set up
        angle = positions[i] * (360/numPlayers)
        players.append(Player(name, angle))

    # This will be placed into the overall deck eventually
    cardsLeft = 52 % numPlayers

    for p in players:
        print(f"{p.name}: {p.angle}")
    print(f"Card to be added to Deck: {cardsLeft}")

start_game()