
# -- EXPECTED RESULT --
# You should ONLY see ActiveGuyWinnerDude take a turn
# BrokeGuyLoserDude should NOT appear at all when taking a turn
# BrokeGuyLoserDude has 0 dollars and ActiveWinnerDude has 20 dollars


from testing_base import *

def test_broke_player_not_playing():
    game = Games()

    # fake players
    dealer = Gertrude("GERTRUDE")
    broke = Player("BrokeGuyLoserDude")
    active = Player("ActiveGuyWinnerDude")

    game.playerList = [dealer, broke, active]

    broke.money = 0
    broke.active = False  

    active.money = 20
    active.active = True

    deck = Deck()
    game.dealer = Dealer(deck)

    broke.addCard(deck.getCard(), True)
    broke.addCard(deck.getCard(), True)

    active.addCard(deck.getCard(), True)
    active.addCard(deck.getCard(), True)

    dealer.addCard(deck.getCard(), True)
    dealer.addCard(deck.getCard(), False)

    print("\n--- STARTING ROUND ---")

    game.round()

test_broke_player_not_playing()

