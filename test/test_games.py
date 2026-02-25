from testing_base import *

game = Games()
players = []
players.append(Player("Bob"))
players.append(Player("Bobby"))
players.append(Player("Bobette"))
players.append(Player("Bombadino"))

game.round(players)