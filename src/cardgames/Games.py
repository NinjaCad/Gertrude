from cardgames.Deck import Deck
from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player
import random
from flask import Flask

class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        print('First 5 cards in standard 52-card deck:')
        for card in self.deck.cards[:5]:
            print(card)
        input('Press [Enter] to exit.')

def win_check(players: "list[Player]"):
    first_player_to_slap = players[0]
    if len(first_player_to_slap.hand) == 0:
        print(f"{first_player_to_slap.name} won!")
        return True
    else:
        return False

if __name__ == "__main__":
    game = Games()
    game.main()