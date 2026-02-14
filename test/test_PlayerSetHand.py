from testing_base import *
import pytest
def test_correctCards(): # correct hand is added
    player = Player("bob")
    sample_image = ["line1", "line2", "line3", "line4", "line5", "line6"]
    new_cards = [Card("Spades", 1, sample_image, sample_image), Card("Heart", 2, sample_image, sample_image)]
    player.setHand(new_cards)
    assert new_cards == player.hand

def test_isNotKnownDef(): # added cards default to not shown
    player = Player("bob")
    sample_image = ["line1", "line2", "line3", "line4", "line5", "line6"]
    new_cards = [Card("Spades", 1, sample_image, sample_image), Card("Heart", 2, sample_image, sample_image)]
    player.setHand(new_cards)
    assert player.knownCards == [False, False]

def test_replaceOldCards(): # new hand overrides old hand
    player = Player("bob")
    sample_image = ["line1", "line2", "line3", "line4", "line5", "line6"]
    curr_cards = [Card("Spades", 1, sample_image, sample_image), Card("Heart", 2, sample_image, sample_image)]
    player.setHand(curr_cards)
    new_cards = [Card("Clubs", 1, sample_image, sample_image), Card("Heart", 2, sample_image, sample_image)]
    player.setHand(new_cards)
    assert new_cards == player.hand