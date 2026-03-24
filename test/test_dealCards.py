from testing_base import *

def test_deck_empty():
    deck = Deck()
    dealer = Dealer(deck)
    player_list = [Player("Daniel"), Player("Joseph"), Player("Rose"), Player("Faith"), Player("Eli"), Player("David")]

    dealer.deal_cards(player_list)

    assert deck.size == 0

def test_player_hands():
    deck = Deck()
    dealer = Dealer(deck)
    player_list = [Player("Daniel"), Player("Joseph"), Player("Rose"), Player("Faith"), Player("Eli"), Player("David")]

    expected_hand_amount = 52//len(player_list)
    expected_players_with_extra = 52 % len(player_list)

    dealer.deal_cards(player_list)

    test_var = True
    players_with_extra = 0
    for player in player_list:
        if len(player.hand) == expected_hand_amount:
            continue
        elif len(player.hand) == expected_hand_amount + 1:
            players_with_extra += 1
            continue
        else:
            test_var = False
    if players_with_extra != expected_players_with_extra:
        test_var = False
    
    assert test_var

def test_too_many_players():
    deck = Deck()
    dealer = Dealer(deck)
    player_list = [Player("David") for _ in range(53)]

    assert dealer.deal_cards(player_list) == False