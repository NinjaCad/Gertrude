import sys
sys.path.append("../")

from src.Card import Card
from src.Deck import Deck
from src.Dealer import Dealer
from src.Games import Games
from src.Player import Player

def getCard( suit, value):
    deck = Deck()
    my_card = Card( suit.capitalize(), value, None, None)
    for card in deck.cards:
      if card == my_card:
        return card
    return None