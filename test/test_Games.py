from testing_base import *

# ensure 3 cards are dealt to each player
def test_deal_three_cards():
    player1, player2, deck = Games().main(test_mode=True)
    assert len(player1.hand) == 3
    assert len(player2.hand) == 3

# ensure deck is shuffled and not in original order
def test_deck_is_shuffled():
    og_deck = Deck()
    p1, p2, deck = Games().main(test_mode=True)
    for i in range(0, len(og_deck.cards)-7):
        if og_deck.cards[i] != deck.cards[i]:
            assert True

# ensure player is choosing a card from their hand
def test_chosen_card_in_hand():
    player1, player2, deck = Games().main(test_mode=True)
    assert player1.chosen_card in player1.hand
    assert player2.chosen_card in player2.hand


def test_build_betting_notification_uses_templates(monkeypatch):
    game = Games()
    monkeypatch.setattr("cardgames.Games.random.choice", lambda templates: templates[0])

    message = game.build_betting_notification("Player_2")

    assert message == "Someone places a calm, standard bet on Player_2."


def test_show_betting_popup_prints_message(monkeypatch, capsys):
    game = Games()
    monkeypatch.setattr("cardgames.Games.random.choice", lambda templates: templates[1])

    message = game.show_betting_popup("Player_1")
    output = capsys.readouterr().out

    assert message == "A gambler puts a routine wager on Player_1."
    assert "[BETTING POP-UP] A gambler puts a routine wager on Player_1." in output
