from testing_base import *


def test_rerun_if_tie():
    # copying my code from Games.main() that surrounds handle_ties, except setting players' hands to be the same
    player1 = Player("P1")
    player1.hand = [Card("Clubs", 1, ["image"], ["back"])]
    player2 = Player("P2")
    player2.hand = [Card("Clubs", 1, ["image"], ["back"])]

    print("\nChosen cards are =, so result should be a tie.")
    display_winner = input("\nPress [Enter] to display the winner: ")
    if display_winner == "":
        # display winner
        winner = declare_winner(player1, player2)
        if winner == "It's a tie!":
            print("If this prints, it means there's a tie!, and script should repeat.")
            Games().handle_ties([player1, player2])
            winner = declare_winner(player1, player2)
            assert(winner == "It's a tie!")

def test_stop_if_winner():
    # copying my code from Games.main() that surrounds handle_ties, except setting players' hands to initially be the same
    player1 = Player("P1")
    print(" \nSTARTING TEST 2\n")
    player1 = Player("P1")
    player1.hand = [Card("Clubs", 1, ["image"], ["back"])]
    player2 = Player("P2")
    player2.hand = [Card("Clubs", 1, ["image"], ["back"])]

    print("There should be one input-prompt session since there is currently a tie.")
    winner = declare_winner(player1, player2)
    while winner == "It's a tie!":
        player2.hand = [Card("Clubs", 2, ["image"], ["back"])]
        Games().handle_ties([player1, player2])
        print("Now there is no tie, so winner should be displayed.")
        winner = declare_winner(player1, player2)
    print("\nWinner is: ", winner)
    print("\nThis should print because no tie.")
    assert(winner != "It's a tie!")

def test_allow_redraw_from_original_hand():
    print(" \nSTARTING TEST 3\n")
    player1 = Player("P1")
    player1.hand = [Card("Clubs", 1, ["image"], ["back"])]
    player2 = Player("P2")
    player2.hand = [Card("Clubs", 1, ["image"], ["back"])]
    Games().handle_ties([player1, player2])
    assert((player1.chosen_card in player1.hand) & (player2.chosen_card in player2.hand))
