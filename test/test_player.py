from testing_base import *


pl = Player("John")

def test_check_cards():
    # Two Aces -> 11 + 11 = 22
    # Adjust one Ace from 11 to 1 -> total = 12
    assert pl.check_cards([0, 0]) == 12
    
def test_check_cards2():
    # 5 % 13 == 5 -> 6
    # 11 + 6 = 17 (no adjustment needed)  
    assert pl.check_cards([0,5]) == 17

def test_check_cards3():
    # 9 % 13 == 9 -> 10
    # 0 % 13 == 0 -> Ace (11)
    # 10 + 10 + 11 = 31
    # Adjust Ace from 11 to 1 -> total = 21
    assert pl.check_cards([9,9,0]) == 21

def test_check_cards4():
    # 0,0,0,0 -> four Aces -> 11*4 = 44
    # 14 % 13 == 1 -> 2
    # 44 + 2 = 46
    # Adjust Aces from 11 to 1 as needed:
    # 46 -> 36 -> 26 -> 16 (three adjustments)
    # Final total = 16 
    assert pl.check_cards([0,0,0,0,14]) == 16

def test_check_cards5():
    # 52, 65, 78 all % 13 == 0 -> three Aces -> 11*3 = 33 -> adjust -> 13
    assert pl.check_cards([52, 65, 78]) == 13

def test_check_cards6():
    # 12 % 13 == 12 -> King -> 10
    # 25 % 13 == 12 -> King -> 10
    # 38 % 13 == 12 -> King -> 10
    # 10 + 10 + 10 = 30 (bust)
    assert pl.check_cards([12, 25, 38]) == 30

def test_check_cards7():
    # 51 % 13 == 12 -> King -> 10
    # 39 % 13 == 0 -> Ace (11)
    # 10 + 11 = 21 (blackjack)
    assert pl.check_cards([51, 39]) == 21

def testTipDealer():
    pl.money = 100
    pl.tipDealer()
    print(f"{pl.name} has ${pl.money}")
    
    # to test this file:
    # cd into test ------->   cd test
    # run this file ------>   python -m test_player
    


    #instructions for test case #3
    #1. ASSERT "John, you have $100" is printed
    #2. ASSERT "Do you want to tip the dealer? (y/n)" is printed
    #3. Respond "yes" to the previous question
    #4. ASSERT "Not a valid answer, try again." is printed

    #instructions for test case #2
    #1. ASSERT "John, you have $100" is printed
    #2. ASSERT "Do you want to tip the dealer? (y/n)" is printed
    #3. Respond "n" to the previous question 
    #4. ASSERT "Gertrude looks at you blankly..." is printed
    #5. ASSERT "John has $100" is printed
    
    #instructions for test case #3
    #1. ASSERT "John, you have $100" is printed
    #2. ASSERT "Do you want to tip the dealer? (y/n)" is printed
    #3. Respond "y" to the previous question
    #4. ASSERT "How much do you want to tip? (integer value only)" is printed
    #5. Respond "one-hundred" to the previous question
    #6. ASSERT "That is not an integer value! Try again" is printed and
        #"How much do you want to tip..." is printed (from step 3)
    #7. Respond "150" to the previous question
    #8. ASSERT "You don't have that much money! Try again." is printed and
        #"How much do you want to tip..." is printed from step 3
    #9. Respond "100" to the previous question
    #10. ASSERT "Gertrude smiles warmly: Thanks for the tip sweetie!" is printed
    #11. ASSERT "John has $0" is printed

    
  

if __name__ == "__main__":
    testTipDealer()

    

