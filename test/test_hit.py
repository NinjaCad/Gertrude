from testing_base import *
import pytest
from unittest.mock import Mock, MagicMock
def test_hit_with_cards_in_deck():
    # Test successful hit when deck has cards
    player = Mock()
    player.addCard = Mock()
    deck = Mock()
    deck.size = 5
    card = Mock()
    deck.getCard = Mock(return_value=card)
    
    result = player.hit(deck, isKnown=True)
    
    assert result == card
    deck.getCard.assert_called_once()
    player.addCard.assert_called_once_with(card, True)


def test_hit_with_empty_deck():
    # Test hit when deck is empty
    player = Mock()
    player.addCard = Mock()
    deck = Mock()
    deck.size = 0
    
    result = player.hit(deck)
    
    assert result is None
    player.addCard.assert_not_called()


def test_hit_with_isknown_false():
    # Test hit with isKnown=False
    player = Mock()
    player.addCard = Mock()
    deck = Mock()
    deck.size = 3
    card = Mock()
    deck.getCard = Mock(return_value=card)
    
    result = player.hit(deck, isKnown=False)
    
    assert result == card
    player.addCard.assert_called_once_with(card, False)


def hit_test(card):
    pass

def hit_test(card):
# test for if and test for else by calling hit function and inputing a card value and seeing if it runs the function