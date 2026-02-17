from testing_base import *

deck = Deck()
dealer = Dealer(deck)

# Create a player
players = {}
players["testDummy"] = Player("testDummy")

# Create a custom hand to give player
customSetHand = []
for i in range(5):
    card = deck.getCard()
    customSetHand.append(card)

# Give the player the hand
print()
try:
    players["testDummy"].setHand(customSetHand, True)
    print("Succeeded in giving the player a set hand")
except:
    print("Failed to give player a set hand")
print()

# Print the player's hand
print("Player's hand:")
players["testDummy"].showHand()