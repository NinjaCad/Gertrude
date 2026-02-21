from testing_base import *
def expected_winner():
    bob = Player("bob")
    bob.chosen_card = Card("Ace of Spades", 1, [], [])
    alice = Player("alice")
    alice.chosen_card = Card("King of Hearts", 13, [], [])
    declare_winner(bob, alice)
    assert declare_winner(bob, alice) == alice

def expected_tie():
    bob = Player("bob")
    bob.chosen_card = Card("Ace of Spades", 1, [], [])
    alice = Player("alice")
    alice.chosen_card = Card("Ace of Spades", 1, [], [])
    declare_winner(bob, alice)
    assert declare_winner(bob, alice) == None

def handle_missing_cards():
    bob = Player("bob")
    alice = Player("alice")
    declare_winner(bob, alice)
    assert declare_winner(bob, alice) == None

def handle_missing_card():
    bob = Player("bob")
    bob.chosen_card = Card("Ace of Spades", 1, [], [])
    alice = Player("alice")
    declare_winner(bob, alice)
    assert declare_winner(bob, alice) == None