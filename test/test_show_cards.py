import pytest
from testing_base import *
from cardgames.Card import Card

def show_cards(card: Card):
    face_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    card_name = face_names.get(card.value, card.value)
    
    display_text = f"--- {card_name} of {card.suit} ---\n"
    
    for line in card.image:
        display_text += line + "\n"
        
    return display_text

def test_show_cards_output():
    image = [" _____ ", "|A .  |", "| /.\\ |", "|(_._)|", "|  |  |", "|____V|"]
    back = ["XXXXX"] * 6

    test_ace = Card("Spades", 1, image, back)
    test_five = Card("Diamonds", 5, image, back)

    ace_output = show_cards(test_ace)
    five_output = show_cards(test_five)

    assert "--- Ace of Spades ---" in ace_output, "Failed to name the ace correctly."
    assert "--- 5 of Diamonds ---" in five_output, "Failed to name the card correctly."
    assert "|(_._)|" in ace_output, "Failed to include the image lines."