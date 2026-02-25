from testing_base import *

game = Games()
players = []
players.append(Player("Bob"))
players.append(Player("Bobby"))

game.round(players)
# test case 1:
# prints: "Bob's hand: "
# input: "stand" -> prints: "stand"
# prints: "Bobby's hand: "
# input: "stand" -> prints: "stand"
#
# test case 2:
# prints: "Bob's hand: "
# input: "hit" -> prints: "stand"
# prints: "Bob's hand: "hit
# input: "stand" -> prints: "stand"
# prints: "Bobby's hand: "
# input: "hit" -> prints: "hit"
# prints: "Bobby's hand: "
# input: "stand" -> prints: "stand"