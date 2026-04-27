#shuffle the deck upon initiation of game
#this means the deck has an ordered set, before any player draws a card the order is randomized

#game is initiated through Games.py, Deck.py
#we need the same number, the same cards, in a diff order

import sys
import sys
from pathlib import Path

#always(?) add project root to sys.path when running tests directly
ROOT = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(ROOT))

from cardgames.Deck import Deck
from cardgames.Games import Games


def test_shuffle_keeps_52_cards():
    deck = Deck()
    deck.shuffle()
    assert len(deck.cards) == 52 
#this will assert the length of the set of cards in the deck and it MUST be exactly 52



def test_shuffle_actually_shuffles():
    shuffled_deck = Deck()
    original_order = shuffled_deck.cards[:]
    shuffled_deck.shuffle()
    new_order = shuffled_deck.cards[:]
    assert original_order != new_order
#assume the shuffle changes the order, checks


def test_shuffle_keeps_same_cards():
    deck = Deck()
    original_cards = [str(card) for card in deck.cards]
    deck.shuffle()
    shuffled_cards = [str(card) for card in deck.cards]
    assert sorted(original_cards) == sorted(shuffled_cards)
#this test checks the same cards in the initial deck exists in the shuffled deck
