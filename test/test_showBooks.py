from testing_base import *
import random

def manual_test_showBooks_basic():
    print("Running test_showBooks_Basic()")
    players = [Player("1"), Player("2"), Player("3"), Player("4")]
    values = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "Eights", "Nines", "Tens", "Jacks", "Queens", "Kings"]

    # Picks user defined amount of books with no duplicates for each player, output should show the appropriate amount of books
    totalNumBooks = []
    booksLeft = 13
    for player in players:
        while True:
            numBooks = int(input(f"Enter up to {booksLeft} books to give player {player.name}: "))
            if numBooks <= booksLeft:
                totalNumBooks.append(numBooks)
                booksLeft -= numBooks
                break
            print(f"Number must be less than or equal to {booksLeft}")

    for playerNum, player in enumerate(players):
        for i in range(totalNumBooks[playerNum]):
            player.books.append(values.pop(random.randint(0, len(values) - 1)))
        print(f'Player {player.name}\'s books:')
        player.showBooks()
        print()

def test_showBooks_no_value():
    print("Running test_showBooks_no_value()")
    players = [Player("1"), Player("2"), Player("3"), Player("4")]

    # All players start with no books, so there should be nothing printed without crashing
    for player in players:
        print(f'Player {player.name}\'s books:')
        player.showBooks()
        print()

def test_showBooks_isolated():
    print("Running test_showBooks_isolated()")
    players = [Player("1")]
    players[0].books = ["Aces"]

    # This test passes if the value of person.books stays consistent before and after running
    beforeBooks = players[0].books
    players[0].showBooks()
    assert beforeBooks == players[0].books
    print("\nAssertion Test Passed \n")

def test_showBooks_error():
    print("Running test_showBooks_error()")
    players = [Player("1")]
    players[0].books = ["Incorrect Key"]

    # This test should output an error without crashing the program
    players[0].showBooks()

if __name__ == "__main__":
    manual_test_showBooks_basic()
    test_showBooks_no_value()
    test_showBooks_isolated()
    test_showBooks_error()