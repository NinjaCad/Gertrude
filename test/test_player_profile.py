from testing_base import *
import pytest


def test_profile_defaults_for_nickname_level_and_xp():
    player = Player("Alice")

    assert player.nickname == "Alice"
    assert player.level == "Beginner"
    assert player.get_xp() == 0


def test_profile_keeps_custom_nickname_and_valid_level():
    player = Player("Alice", nickname="Ace", level="Advanced")

    assert player.nickname == "Ace"
    assert player.level == "Advanced"


def test_profile_invalid_level_falls_back_to_beginner():
    player = Player("Alice", level="Pro")

    assert player.level == "Beginner"


def test_profile_display_name_uses_nickname_when_different():
    player = Player("Alice", nickname="Ace")

    assert player.profile_display_name() == "Alice (Ace)"


def test_profile_display_name_uses_name_when_same_as_nickname():
    player = Player("Alice", nickname="Alice")

    assert player.profile_display_name() == "Alice"


def test_add_xp_increments_value():
    player = Player("Alice")

    player.add_xp()
    player.add_xp(2)

    assert player.get_xp() == 3


def test_add_xp_rejects_negative_values():
    player = Player("Alice")

    with pytest.raises(ValueError):
        player.add_xp(-1)
