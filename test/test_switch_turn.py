from testing_base import *

from cardgames.turns import switch_turn


def test_switch_turn_hides_current_players_card_and_prompts_next_player():
    playerX = Player("PlayerX")
    playerY = Player("PlayerY")

    # Give each player predictable cards.
    playerX.setHand([getCard("spades", 1), getCard("hearts", 2), getCard("clubs", 3)], isKnown=True)
    playerY.setHand([getCard("diamonds", 4), getCard("spades", 5), getCard("hearts", 6)], isKnown=True)

    # PlayerX chooses their 2nd card (index 1). Then we switch to PlayerY,
    # and PlayerY chooses "3" (index 2).
    inputs = iter(["3"])

    def fake_input(prompt: str) -> str:
        return next(inputs)

    next_idx, playerY_choice_idx = switch_turn(
        players=[playerX, playerY],
        current_player_index=0,
        chosen_card_index=1,
        input_fn=fake_input,
        print_fn=lambda _: None,
    )

    assert playerX.knownCards == [True, False, True]
    assert next_idx == 1
    assert playerY_choice_idx == 2
