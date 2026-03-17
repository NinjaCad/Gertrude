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
      1) Call the current player's hide_card() for the chosen card.
      2) Prompt the next player to choose a card.

    Args:
        players: Players in turn order.
        current_player_index: Index into `players` for the current player.
        chosen_card_index: Which card the *current* player selected (0-based).
        input_fn: Injectable input function to keep this testable.
        print_fn: Injectable print function to keep this testable.

    Returns:
        (next_player_index, next_player_chosen_card_index)

    Raises:
        ValueError: if players is empty.
        IndexError: if current_player_index is out of range.
    """

    if not players:
        raise ValueError("players must be a non-empty list")

    if current_player_index < 0 or current_player_index >= len(players):
        raise IndexError(f"current_player_index out of range: {current_player_index}")

    current_player = players[current_player_index]
    current_player.hide_card(chosen_card_index)

    next_player_index = (current_player_index + 1) % len(players)
    next_player = players[next_player_index]

    # Prompt until valid.
    while True:
        raw = input_fn(
            f"{next_player.name}, choose a card (1-{len(next_player.hand)}): "
        ).strip()

        try:
            choice_1_based = int(raw)
        except ValueError:
            print_fn("Please enter a number.")
            continue

        choice_idx = choice_1_based - 1
        if 0 <= choice_idx < len(next_player.hand):
            return next_player_index, choice_idx

        print_fn(f"Choice must be between 1 and {len(next_player.hand)}.")
