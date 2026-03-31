from testing_base import *

def endGameState(players):
        nameScorePairs = {p.name: p.numBooks for p in players}
        mostBooks = max(nameScorePairs.values())
        mostBooksHolders = [name for name, score in nameScorePairs.items() if score == mostBooks]
        #in case of tie:
        if len(mostBooksHolders) > 1:
            print(f"It's a tie between {' and '.join(mostBooksHolders)} with {mostBooks} books each!")
        #sigle winner:
        else:
            winner = mostBooksHolders[0]
            print(f"{winner} wins with {mostBooks} books!")
        #scoreboard/lists all player's scores
        print("\nFinal scores:")
        for player in players:
            if player.numBooks == 0:
                print(f"{player.name} has 0 books.")
            elif player.numBooks == 1:
                print(f"{player.name}: {player.numBooks} book.\nThey have the following book: {player.books}")
            else:
                print(f"{player.name}: {player.numBooks} books.\nThey have the following books: {player.books}")
        print()

# Create deck and dealer
deck = Deck()
dealer = Dealer(deck)

#Tie Scenario (A:6, B:6, C:1) This tests tie and player 3 tests the output if someone scores only 1 book.
def tieTest():
    players = []
    players.append(Player("Tim"))
    players.append(Player("Tom"))
    players.append(Player("Tam"))
    
    players[0].numBooks = 6
    players[1].numBooks = 6
    players[2].numBooks = 1

    players[0].books = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes"]
    players[1].books = ["Sevens", "Eights", "Nines", "Tens", "Jacks", "Queens"]
    players[2].books = ["Kings"]

    endGameState(players)

#Not a Tie Scenario (A:5, B:4, C:4) This is a basic scenario but also shows that if losers tie it still shows solo winner message.
def oneWinnerTest():
    players = []
    players.append(Player("Tim"))
    players.append(Player("Tom"))
    players.append(Player("Tam"))
    
    players[0].numBooks = 5
    players[1].numBooks = 4
    players[2].numBooks = 4

    players[0].books = ["Aces", "Twos", "Threes", "Fours", "Fives"]
    players[1].books = ["Sixes", "Sevens", "Eights", "Nines"]
    players[2].books = ["Tens", "Jacks", "Queens", "Kings"]

    endGameState(players)

#Make sure it works even if a player had 0 books and posts that message (A:7, B:6, C:0)
def testPlayerWithZeroBooksAtEnd():
    players = []
    players.append(Player("Tim"))
    players.append(Player("Tom"))
    players.append(Player("Tam"))
    
    players[0].numBooks = 7
    players[1].numBooks = 6
    players[2].numBooks = 0

    players[0].books = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens"]
    players[1].books = ["Eights", "Nines", "Tens", "Jacks", "Queens", "Kings"]
    players[2].books = []

    endGameState(players)

tieTest()
oneWinnerTest()
testPlayerWithZeroBooksAtEnd()