from testing_base import *

def test_stand():
    
    PlayerA = Player("Test")
    assert PlayerA.active == True
    
    PlayerA.stand()
    assert PlayerA.active == False
    
    PlayerA.stand()
    assert PlayerA.active == True


def main():
    
    test_stand()
    
    
if __name__ == "__main__":
    main()