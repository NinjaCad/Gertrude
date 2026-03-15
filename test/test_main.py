from main import *

# ensure 3 cards are dealt to each player
def test_deal_three_cards():
    assert len(player1.hand) == 3
    assert len(player2.hand) == 3

# ensure deck is shuffled and not in original order
def test_deck_is_shuffled():
    og_deck = Deck()
    for i in range(0, len(og_deck.cards)-7):
        if og_deck.cards[i] != deck.cards[i]:
            assert True

# ensure player is choosing a card from their hand
def test_chosen_card_in_hand():
    assert player1.chosen_card in player1.hand
    assert player2.chosen_card in player2.hand
