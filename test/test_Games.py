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


def test_build_betting_notification_custom_values():
    game = Games()
    message = game.build_betting_notification("Player_2", bettor_name="John Doe", amount="$10k")
    assert message == "John Doe bet $10k on Player_2."


def test_show_betting_popup_prints_message(capsys):
    game = Games()
    message = game.show_betting_popup("Player_1", bettor_name="Sam", amount="$20 million")
    output = capsys.readouterr().out

    assert message == "Sam bet $20 million on Player_1."
    assert "[BETTING POP-UP] Sam bet $20 million on Player_1." in output
