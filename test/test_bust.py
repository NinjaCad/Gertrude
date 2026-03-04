from testing_base import *

def test_bust():
    
    PlayerA = Player("Test")
    assert PlayerA.active
    
    PlayerA.bust()
    assert not PlayerA.active

def main():
    
    test_bust()

    
if __name__ == "__main__":
    main()