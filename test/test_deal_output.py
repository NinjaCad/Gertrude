from testing_base import *


def test_deal_output_order():
    game = Games()
    players = [
        Player("Tim"),
        Player("Tom"),
        Player("Tam"),
    ]

    turn_list = game.start_game(players)

    print("=== Dealt Hands (turn order) ===")
    for idx, player in enumerate(turn_list, start=1):
        sorted_hand = sorted(player.hand, key=lambda c: c.value)
        cards_str = ", ".join(str(card) for card in sorted_hand)
        print(f"{idx}. {player.name}: {cards_str}")
