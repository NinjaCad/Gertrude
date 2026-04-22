from testing_base import *


def _make_card(value, suit="Spades"):
    image = [" _____ ", "|     |", "|     |", "|     |", "|     |", "|_____|"]
    card_back = [" _____ ", "|/////|", "|/////|", "|/////|", "|/////|", "|_____|"]
    return Card(suit, value, image, card_back)


def test_card_thievery_two_players_skips_target_prompt(monkeypatch):
    game = Games()
    host = Player("Host")
    opponent = Player("Opponent")
    host.isTurn = True

    opponent.addCard(_make_card(1, "Hearts"))  # Ace available to steal

    prompt_calls = []

    def fake_input(prompt):
        prompt_calls.append(prompt)
        if "Choose player to steal from" in prompt:
            raise AssertionError("Should not prompt for target player in 2-player game.")
        if "Choose card type you wish to steal" in prompt:
            return "aces"
        raise AssertionError(f"Unexpected prompt: {prompt}")

    monkeypatch.setattr("builtins.input", fake_input)

    did_steal = game.card_thievery([host, opponent], host)

    assert did_steal is True
    assert len(host.hand) == 1
    assert len(opponent.hand) == 0
    assert any("Choose card type you wish to steal" in p for p in prompt_calls)
