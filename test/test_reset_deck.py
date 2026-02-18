from testing_base import *

def test_reset_deck():
    deck = Deck()

    for i in range(5):
        deck.getCard()
        
    assert deck.size == 47

    deck.reset()

    assert deck.size == 52
    
def main():
    test_reset_deck()
    
if __name__ == "__main__":
    main()