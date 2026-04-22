import pytest

from cardgames.Games import Games
from cardgames.Player import Player
from cardgames.turns import switch_turn
from cardgames.Card_Compare import Card


def test_playthrough_with_fixed_choices_sets_chosen_cards_and_winner():
    game = Games()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    result = game.playthrough(
        players=[player1, player2],
        cards_per_player=3,
        chosen_indices=[0, 1],
        print_fn=lambda _: None,
    )

    assert len(player1.hand) == 3
    assert len(player2.hand) == 3
    assert player1.chosen_card == player1.hand[0]
    assert player2.chosen_card == player2.hand[1]
    assert player1.knownCards[0] is False
    assert result["winner"] in {"Player 1", "Player 2", "It's a tie!"}


def test_playthrough_rejects_invalid_choice_indices_shape():
    game = Games()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    with pytest.raises(ValueError, match="exactly two values"):
        game.playthrough(
            players=[player1, player2],
            cards_per_player=3,
            chosen_indices=[0],
            print_fn=lambda _: None,
        )


def test_switch_turn_hides_current_players_card_and_returns_next_choice():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1.setHand(
        [
            Card("Spades", 1, [], []),
            Card("Hearts", 2, [], []),
            Card("Clubs", 3, [], []),
        ],
        isKnown=True,
    )
    player2.setHand(
        [
            Card("Diamonds", 4, [], []),
            Card("Spades", 5, [], []),
            Card("Hearts", 6, [], []),
        ],
        isKnown=True,
    )

    inputs = iter(["3"])

    def fake_input(_prompt: str) -> str:
        return next(inputs)

    next_idx, choice_idx = switch_turn(
        players=[player1, player2],
        current_player_index=0,
        chosen_card_index=1,
        input_fn=fake_input,
        print_fn=lambda _: None,
    )

    assert player1.knownCards == [True, False, True]
    assert next_idx == 1
    assert choice_idx == 2
