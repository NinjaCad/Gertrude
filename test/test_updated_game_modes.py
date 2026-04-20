from cardgames.Game_modes import Games
from cardgames.Player import Player


# =========================
# TEST 1: cards per turn rule
# =========================
def test_cards_per_turn_fixed_to_3():
    game = Games()

    game.players = [Player("P1"), Player("P2")]
    game.cards_per_turn = 3

    assert game.cards_per_turn == 3


# =========================
# TEST 2: best-of validation
# =========================
def test_best_of_values_valid():
    game = Games()

    valid_modes = [1, 3, 5]

    for mode in valid_modes:
        game.num_rounds = mode
        assert game.num_rounds == mode


# =========================
# TEST 3: initial state check
# =========================
def test_games_initial_state():
    game = Games()

    assert game.deck is not None
    assert game.dealer is not None
    assert game.players == []

    assert game.num_rounds == 1
    assert game.cards_per_turn == 3
    assert game.mode_locked is False

    #pytest test/test_updated_game_modes.py --html=report.html --self-contained-html