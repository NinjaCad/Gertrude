from testing_base import *

# Create deck and dealer
deck = Deck()
dealer = Dealer(deck)

# Create players
players = {}
while True:
    try:
        num_players = int(input("Enter player count: "))
        break
    except ValueError:
        print("Please enter number of players: ")
for i in range(1, num_players+1):
    name = input("Player {} name: ".format(i))
    players[name] = Player(name)

# Deal 5 cards to each player
dealer.deal_cards(5, list(players.values()))

# Show each player's hand
for player in players.values():
    print(f'{player.name}:')
    player.show_hand(True)
    print()
