from testing_base import *


def test_rerun_if_tie():
    player1 = Player("P1")
    player1.hand = [Card("Clubs", 10, ["image"], ["back"])]
    player2 = Player("P2")
    player2.hand = [Card("Clubs", 10, ["image"], ["back"])]

    print("\nChosen cards are =, so result should be a tie.")
    display_winner = input("\nPress [Enter] to display the winner: ")
    if display_winner == "":
        # display winner
        winner = declare_winner(player1, player2)
        while winner == "It's a tie!":
            print("If this prints, it means there's a tie!, and script should repeat.")
            Games().handle_ties([player1, player2])
            winner = declare_winner(player1, player2)
