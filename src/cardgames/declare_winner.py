from cardgames.Player import Player


def declare_winner(player1, player2):
    card1 = player1.chosen_card
    card2 = player2.chosen_card

    def _is_missing(card):
        if card is None:
            return True
        return getattr(card, "value", None) in (None, 0) or getattr(card, "suit", "") in (None, "")

    if _is_missing(card1) or _is_missing(card2):
        print("Error: Both players must have chosen a card to declare a winner.")
        return None

    # Prefer compare() when available (Card_Compare.Card)
    if hasattr(card1, "compare"):
        result = card1.compare(card2)
    else:
        # Fallback for cardgames.Card.Card
        suit_rank = {"Clubs": 4, "Diamonds": 3, "Hearts": 2, "Spades": 1}
        if card1.value > card2.value:
            result = 1
        elif card1.value < card2.value:
            result = -1
        else:
            result = (suit_rank.get(card1.suit, 0) > suit_rank.get(card2.suit, 0)) - (
                suit_rank.get(card1.suit, 0) < suit_rank.get(card2.suit, 0)
            )

    if result == 1:
        return player1
    if result == -1:
        return player2
    return (player1, player2)
