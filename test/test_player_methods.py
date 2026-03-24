from testing_base import *
from cardgames.Player import Player

#test if the angle defaults to 0 if not passed in
def test_default_angle_is_zero():
    player = Player("Prof Lee")
    assert player.angle == 0

#test if the angle is properly assigned the value passed in
def test_angle_is_not_zero():
    player = Player("Prof Lee", 30)
    assert player.angle == 30

#test if player.get_name() does get the player's name
def test_player_get_name():
    player = Player("Prof Lee")
    assert player.get_name() == player.name

#test if modifying player.get_name() does not modify player.name
def test_modified_get_name():
    player = Player("Prof Lee")
    player_name = player.get_name()
    player_name = player_name[:3]
    assert player_name != player.name

#test if player.set_name() does change the player's name
def test_player_set_name():
    player = Player("Prof Lee")
    player.set_name("John")
    assert player.name == "John"

#test if player.get_hand() works when player.hand is empty
def test_player_get_empty_hand():
    deck = Deck()
    player = Player("Prof Lee")
    assert player.get_hand() == player.hand

#test if player.get_hand() works when player.hand is not empty
def test_player_get_hand():
    deck = Deck()
    player = Player("Prof Lee")
    for i in range(5):
        player.add_card(deck.getCard())
    assert player.get_hand() == player.hand

#test if player.get_hand() works when player.hand has been modified more than once 
def test_player_get_modified_hand():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("Prof Lee")

    dealer.add_deck_to_hand(player)
    assert player.get_hand() == player.hand

    for i in range(7):
        player.hand.pop()
    assert player.get_hand() == player.hand

#test if modifying player.get_hand() modifies the original player.hand
def test_modified_get_hand():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("Prof Lee")
    player_hand = player.get_hand()
    for _ in range(26):
        player.add_card(deck.getCard())

    for i in range(26):
        player_hand.append(deck.getCard())
    assert player_hand != player.hand