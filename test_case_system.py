import pytest
from cardgames.card_system import card_art  # Ensure your function is in card_system.py

def test_card_width():
    """Verify all cards are exactly 11 characters wide (including 10s)."""
    # Testing edge cases: 'A' (1 char), '10' (2 chars), and 'K' (1 char)
    for suit in ['♠', '♥', '♦', '♣']:
        for rank in ['A', '10', 'K']:
            art = card_art(suit, rank)
            lines = art.split('\n')
            for line in lines:
                # Every line must match the border ┌─────────┐ (11 chars)
                assert len(line) == 11, f"Line length error on rank {rank}: '{line}' is {len(line)} chars"

def test_suit_and_rank_presence():
    """Ensure the suit and rank actually appear in the string."""
    result = card_art('♣', 'Q')
    assert '♣' in result
    assert 'Q' in result

def test_return_type():
    """Acceptance Criteria: Must return a string, not just print it."""
    assert isinstance(card_art('♦', '7'), str)

def test_card_structure():
    """Verify the card has the correct number of lines (7)."""
    result = card_art('♠', 'A')
    lines = result.split('\n')
    assert len(lines) == 7, "Card ASCII art should be exactly 7 lines tall"