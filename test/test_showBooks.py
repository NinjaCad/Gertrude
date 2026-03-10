from testing_base import *

def test_showBooks_basic():
    game = Games()
    players = [Player("1"), Player("2"), Player("3"), Player("4")]
    for player in players:
        player.books = ["Aces", "Twos", "Threes", "Queens"]
        player.showBooks()
        # Give random amount of books and random types

def test_showBooks_isolated():
    pass

def test_showBooks_error():
    pass #wrong key entered

if __name__ == "__main__":
    test_showBooks_basic()