from testing_base import *

def main():
    pass
"""
My functionality (begins 'finish summary' comment in main() of Games.py) 
    needs user input in order to run, so this test will require UI, instead of pytest

Goals and steps of this test file:

GOALS:
    1. ensure that the total money made or lost by each player is accurate 
        A. This will be seen by totalling the amount made or lost on each bet in every round per player
    2. ensure that the "Final Standings: " section is ordered properly
        B. That is, make sure the person who made the most is first, second most is second, etc
    3. ensure that if every player loses money, Gertrude's dialogue is as seen in 'special gertrude dialogue' comment

STEPS: 
(these steps will include variables that you, the tester, will need to keep track 
    of; all variables will begin with a dollar sign, telling you to add something on screen)


        1. Run the game by typing into terminal:
                        cd /app/src
                        python -m cardgames.Games
        2. Respond '3' to Question: How many people are playing?...
        3. Respond '1000' to Question: Enter the amount....

        4. For each of the name inputs, put in Matthew, Mark, Luke, respectively
        5. Respond '200' to Matthew's betting prompt
            A. Respond '50' to Matthew's perfect pairs betting prompt
        6. Respond '300' to Mark's betting prompt
            A. Respond '300' to Mark's perfect pairs betting prompt
        7. Respond '500' to Luke's betting prompt
            A. Respond '40' to Luke's perfect paris betting prompt
        8. IF insurance occurs, act however you prefer, but don't forget to add the money made or lost to each
            players diff variable
            - this test case will not address insurance
    
    Matthew's Turn: 
        9. hit or stand accordingly to get Matthew somewhere between the values of 13 and 20
                but try not to let him bust

    Mark's Turn:
        10. hit until Mark busts

    Luke's Turn:
        11. hit/stand however you prefer (but play like you're trying to win)

    Matthew's bet results:
        12. If Matthew Loses:
            A. $matthewDiff = -200, new total should say $800
            B. If Matthew had perfect pairs: $matthewDiff += 50, new total should say $850
            C. If Matthew didn't have perfect pairs: $matthewDiff -= 50, new total should say $750
        13. If Matthew Wins:
            A. $matthewDiff = 200, new total should say $1200
            B. If Matthew had perfect pairs: $matthewDiff += 50, new total should say $1250
            C. If Matthew didn't have perfect pairs: $matthewDiff -= 50, new total should say $1150
        14. If Matthew Ties:
            A. $matthewDiff = 0
            B. If Matthew had perfect pairs: $matthewDiff += 50, new total should say $1050
            C. If Matthew didn't have perfect pairs: $matthewDiff -= 50, new total should say $950
    
    Mark's bet results:
        15. If Dealer didn't bust:
            A. $markDiff = -300, new total should say $700
            B. If Mark had perfect pairs: $markDiff += 300, new total should say $1000
            C. If Mark didn't have perfect pairs: $markDiff -= 300, new total should say $400
        16. If Dealer did bust, 14 should still have occurred
    
    Luke's bet results:
        17. If Luke busted, or lost to dealer:
            A. $lukeDiff = -500, new total should say $500
            B. If Luke had perfect pairs: $lukeDiff += 40, new total should say $540
            C. If Luke didn't have perfect pairs: $lukeDiff -= 40, new total should say $460
        18. If tie with dealer:
            A. $lukeDiff = 0
            B. If Luke had perfect pairs, $lukeDiff += 40, new total should say 1040
            C. If Luke didn't have perfect pairs, $lukeDiff -= 40, new total should say $960
        19. If Luke Wins:
            A. $lukeDiff = 500, new total should say $1500
            B. If Luke had perfect pairs, $lukeDiff += 40, new total should say $1540
            C. If Luke didn't have perfect pairs, $lukeDiff -= 40, new total should say $1460
    
        20. Respond 'n' to question: Play another round...
            A. If you would like, you can press 'y', but don't forget to += in the steps 12-19 instead of =, this will 
                allow you to keep track of the whole games diff variable changes

        
    Total money made or lost:
        21. ASSERT Matthew's outputted money made or lost equals $matthewDiff
        22. ASSERT Mark's outputted money lost equals $markDiff
        23. ASSERT Luke's outputted money made or lost equals $lukeDiff
            C. For 21-23, if a player broke even, ensure "No change in money!" is outputted

    Final Standings:
        24. ASSERT each player's final money is equal to 1000 + their diff variable
        25. ASSERT the final standings are in order from most money to least
        26. If 1st place made less than $1000, ASSERT Gertrude says "the house always wins" special dialogue
        27. end test

    To test other cases of this functionality, use this same test format,
      but change the values you use in steps 5-7, and thus in the remaing steps
    
"""