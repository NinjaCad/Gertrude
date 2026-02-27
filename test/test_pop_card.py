def test_pop_card_logic():
    # 1. Setup (Arrange)
    player = Player("Test")
    player.hand = ["Card1", "Card2", "Card3"]
    player.knownCards = [True, False, True]
    
    # 2. Action (Act)
    result = player.pop_card()
    
    # 3. Verification (Assert)
    # Check if it returned the LAST card
    assert result == "Card3", f"Expected Card3, but got {result}"
    
    # Check if hand size is correct
    assert len(player.hand) == 2, f"Hand should have 2 cards, has {len(player.hand)}"
    
    # Check if knownCards stayed in sync
    assert len(player.knownCards) == 2, "knownCards list was not updated"
    assert player.knownCards == [True, False], "knownCards values are misaligned"
    
def test_pop_card_on_empty():
    player = Player("Empty")
    player.hand = []
    player.knownCards = []
    
    result = player.pop_card()
    
    assert result is None, "Popping an empty hand should return None"

# Since card_counter uses input(), we usually can't 'assert' 
# it without a mock, but we can test the sequence logic itself:
def test_counter_sequence():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    
    # Verify the logic of your list
    assert ranks[0] == "Ace"
    assert ranks[-1] == "King"
    assert len(ranks) == 13

if __name__ == "__main__":
    # This allows you to run it as a normal script: python test_manual.py
    print("Running manual tests...")
    test_pop_card_logic()
    test_pop_card_on_empty()
    test_counter_sequence()
    print("All tests passed!")