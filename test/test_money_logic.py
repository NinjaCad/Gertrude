from testing_base import *


def test_starting_money_manually():
    # Test Starting Money
    # When prompted Enter: 
    # 2
    # 150
    # John
    # Pork

    game = Games()
    players = game.startGame()

    print("\nCreated players:")
    for p in players:
        if hasattr(p, "money"):
            print(f"{p.name} with ${p.money}")
        else:
            print(f"{p.name} with no dealer money")

    print("\nExpected:")
    print("GERTRUDE: no dealer money")
    print("John: $150")
    print("Pork: $150")

def test_calculate_winner_manual():
    # Test Calcualte Winner with new modifications

    game = Games()

    # Scenario: When Player Wins
    dealer = Gertrude("GERTRUDE")
    winner = Player("Winner")
    winner.money = 100
    winner.bets["standard"] = 20

    # dealer hand has 17
    dealer.addCard(getCard("S", 10)) 
    dealer.addCard(getCard("D", 7))
    # Player hand has 18
    winner.addCard(getCard("H", 10))
    winner.addCard(getCard("C", 8))

    print("\nWin case before: player wins")
    print(f"{winner.name}: money={winner.money}, bet={winner.bets['standard']}")
    game.calculateWinner([dealer, winner])
    print("Win case after: player wins")
    print(f"{winner.name}: money={winner.money}, bet={winner.bets['standard']}")
    print("Expected: Winner should have $120 and bet should be 0")

    # Scenario: When Player Loses
    dealer = Gertrude("GERTRUDE")
    loser = Player("Loser")
    loser.money = 100
    loser.bets["standard"] = 20

    # dealer hand has 17
    dealer.addCard(getCard("S", 10)) 
    dealer.addCard(getCard("D", 7))
    # Player hand has 24
    loser.addCard(getCard("H", 10))
    loser.addCard(getCard("C", 9))
    loser.addCard(getCard("D", 5))

    print("\nLose case before: player wins")
    print(f"{loser.name}: money={loser.money}, bet={loser.bets['standard']}")
    game.calculateWinner([dealer, loser])
    print("Lose case after: player loses")
    print(f"{loser.name}: money={loser.money}, bet={loser.bets['standard']}")
    print("Expected: loser should have $80 and bet should be 0")

    dealer = Gertrude("GERTRUDE")
    push = Player("Pusher")
    push.money = 100
    push.bets["standard"] = 20

    # dealer hand has 18
    dealer.addCard(getCard("S", 10)) 
    dealer.addCard(getCard("D", 8))
    # Player hand has 18
    push.addCard(getCard("H", 9))
    push.addCard(getCard("C", 9))

    print("\n Push case before: player pushes")
    print(f"{push.name}: money={push.money}, bet={push.bets['standard']}")
    game.calculateWinner([dealer, push])
    print("Push  case after: player pushes")
    print(f"{push.name}: money={push.money}, bet={push.bets['standard']}")
    print("Expected: pusher should have $100 and bet should be 0")

def test_main():
    test_starting_money_manually()
    test_calculate_winner_manual()

test_main()