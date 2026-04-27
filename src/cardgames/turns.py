from __future__ import annotations

from typing import Callable

from cardgames.Player import Player


def switch_turn(
    *,
    players: list[Player],
    current_player_index: int,
    chosen_card_index: int,
    input_fn: Callable[[str], str] = input,
    print_fn: Callable[[str], None] = print,
) -> tuple[int, int]:
    """Switch to the next player's turn.

    Responsibilities (per Sprint 2):
      1) Hide the current player's chosen card.
      2) Prompt the next player to choose a card.
    """

    if not players:
        raise ValueError("players must be a non-empty list")

    if not (0 <= current_player_index < len(players)):
        raise IndexError(f"current_player_index out of range: {current_player_index}")

    current_player = players[current_player_index]
    current_player.hide_card(chosen_card_index)

    next_player_index = (current_player_index + 1) % len(players)
    next_player = players[next_player_index]

    if not next_player.hand:
        raise ValueError(f"{next_player.name} has no cards in hand")

    while True:
        raw = input_fn(
            f"{next_player.name}, choose a card (1-{len(next_player.hand)}): "
        ).strip()

        try:
            choice_idx = int(raw) - 1
        except ValueError:
            print_fn("Please enter a number.")
            continue

        if 0 <= choice_idx < len(next_player.hand):
            return next_player_index, choice_idx

        print_fn(f"Choice must be between 1 and {len(next_player.hand)}.")
