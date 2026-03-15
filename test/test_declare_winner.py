from testing_base import *
def test_expected_winner():
    bob = Player("bob")
    bob.chosen_card = Card("Spades", 1, [], [])
    alice = Player("alice")
    alice.chosen_card = Card("Hearts", 13, [], [])
    declare_winner(bob, alice)
    assert declare_winner(bob, alice) == alice

def test_expected_tie():
    bob = Player("bob")
    bob.chosen_card = Card("Spades", 1, [], [])
    alice = Player("alice")
    alice.chosen_card = Card("Spades", 1, [], [])
    assert isinstance(declare_winner(bob, alice), tuple)

def test_handle_missing_cards():
    bob = Player("bob")
    alice = Player("alice")
    assert declare_winner(bob, alice) == None

def test_handle_missing_card():
    bob = Player("bob")
    bob.chosen_card = Card("Spades", 1, [], [])
    alice = Player("alice")
    assert declare_winner(bob, alice) == None