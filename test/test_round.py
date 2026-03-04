from testing_base import *

game = Games()
players = []
players.append(Player("Bob"))
players.append(Player("Bobby"))
players.append(Player("Gertrude"))

game.round(players)

# test case 1:
# TRY: input: "stand" -> prints: "stand"
# Except: "Couldn't call stand()"
#
# test case 2:
# TRY: input: "hit" -> prints: "stand"
# EXCEPT: "Couldn't call hit()"
#
# test case 3:
# TRY: input: "hir" -> prints: "That is not a valid repsonse"
# EXCEPT: "Failed to accept else statement"