from testing_base import *
import random

def test_showBooks_basic():
    game = Games()
    players = [Player("1"), Player("2"), Player("3"), Player("4")]
    values = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "Eights", "Nines", "Tens", "Jacks", "Queens", "Kings"]

    # Picks random number of books with no duplicates for each player, output should show appropriate
    for player in players:
        for i in range(random.randint(0,len(values) - 1)):
            player.books.append(values.pop(random.randint(0, len(values) - 1)))
        print(f'Player {player.name}\'s books:')
        player.showBooks()
        print()

def test_showBooks_no_value():
    game = Games()
    players = [Player("1"), Player("2"), Player("3"), Player("4")]

    # All players start with no books, so there should be nothing printed without crashing
    for player in players:
        print(f'Player {player.name}\'s books:')
        player.showBooks()
        print()

def test_showBooks_isolated():
    game = Games()
    players = [Player("1")]
    players[0].books = ["Aces"]

    # This test passes if the value of person.books stays consistent before and after running
    beforeBooks = players[0].books
    players[0].showBooks()
    assert beforeBooks == players[0].books
    print("\nAssertion Test Passed \n")

def test_showBooks_error():
    game = Games()
    players = [Player("1")]
    players[0].books = ["Incorrect Key"]

    # This test should output an error without crashing the program
    players[0].showBooks()

if __name__ == "__main__":
    test_showBooks_basic()
    test_showBooks_no_value()
    test_showBooks_isolated()
    test_showBooks_error()