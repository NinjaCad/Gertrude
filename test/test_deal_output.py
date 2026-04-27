from testing_base import *


def test_deal_output_order():
    game = Games()
    players = [
        Player("Tim"),
        Player("Tom"),
        Player("Tam"),
    ]

    turn_list = game.start_game(players, "regular")

    print("=== Dealt Hands (turn order) ===")
    for idx, player in enumerate(turn_list, start=1):
        player.sortHand()
        cards_str = ", ".join(str(card) for card in player.hand)
        print(f"{idx}. {player.name}: {cards_str}")
