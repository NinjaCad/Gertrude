import pytest

from testing_base import *
from cardgames.Games import HighCardDrawInstructions

# Tests for NEW FEATURE (Sprint 1): HighCardDrawInstructions in Games.py


def test_instructions_sections_contains_expected_keys():
    topics = HighCardDrawInstructions.topics()
    assert topics == sorted(topics)
    assert "overview" in topics
    assert "winning" in topics


def test_instructions_get_overview_contains_game_name():
    text = HighCardDrawInstructions.get("overview")
    assert "HIGH_CARD_DRAW" in text  # title line is uppercased
    assert "2-player" in text or "2 player" in text


def test_instructions_get_winning_mentions_tie_behavior():
    text = HighCardDrawInstructions.get("winning")
    assert "WINNING" in text
    assert "tie" in text.lower()


def test_instructions_unknown_section_raises_value_error():
    with pytest.raises(ValueError):
        HighCardDrawInstructions.get("not_a_real_topic")


def test_instructions_formatting_includes_bar_and_body():
    text = HighCardDrawInstructions.get("overview")
    lines = text.splitlines()
    assert lines[0].startswith("=")  # bar
    assert "OVERVIEW" in lines[1]
    assert "Each player" in text
