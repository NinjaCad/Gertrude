import sys
import sys
from pathlib import Path

# Add project root to sys.path when running tests directly
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cardgames.Card_Compare import Card
from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Games import Games
from cardgames.Player import Player
from declare_winner import declare_winner


def getCard( suit, value):
    deck = Deck()
    my_card = Card( suit.capitalize(), value, None, None)
    for card in deck.cards:
      if card == my_card:
        return card
    return None