from cardgames.Card import Card
from cardgames.Dealer import Dealer
from cardgames.Player import Player


CARDS_PER_PLAYER = 3
MIN_CARDS_FOR_ROUND = 6


def safe_high_card_round(dealer: Dealer, players: list):
    """Run a single high-card round safely, with basic checks."""
    
    # Basic setup checks
    if dealer is None or not hasattr(dealer, "deck") or dealer.deck.size < MIN_CARDS_FOR_ROUND:
        print(f"Dealer not ready or not enough cards (need {MIN_CARDS_FOR_ROUND}).")
        return None
    if len(players) != 2:
        print("This game requires exactly two players.")
        return None

    # Deal cards
    dealer.resetDeck()
    dealer.dealCards(players)
    for player in players:
        if len(player.hand) != CARDS_PER_PLAYER:
            print(f"{player.name} did not receive {CARDS_PER_PLAYER} cards.")
            return None

    chosen_cards = {}

    # Prompt each player for a card
    for player in players:
        while True:
            choice = input(f"{player.name}, choose a card (1-{CARDS_PER_PLAYER}): ").strip()
            if not choice.isdigit():
                print("Input must be a number.")
                continue
            choice = int(choice)
            if choice < 1 or choice > CARDS_PER_PLAYER:
                print(f"Choice must be between 1 and {CARDS_PER_PLAYER}.")
                continue
            if choice > len(player.hand):
                print(f"{player.name} only has {len(player.hand)} cards.")
                continue
            chosen_cards[player.name] = player.hand[choice - 1]
            break

    # Validate chosen cards
    for player_name, card in chosen_cards.items():
        if not hasattr(card, "value") or card.value is None:
            print(f"{player_name} chose an invalid card.")
            return None
        if not isinstance(card.value, int):
            print(f"{player_name}'s card value is not a number.")
            return None

    # Determine winner
    p1, p2 = players
    c1, c2 = chosen_cards[p1.name], chosen_cards[p2.name]
    if c1.value == c2.value:
        print("It's a tie!")
        winner = "tie"
    else:
        winner = p1.name if c1.value > c2.value else p2.name
        print(f"{winner} wins!")

    # Reset players
    for player in players:
        player.clearHand()

    return winner