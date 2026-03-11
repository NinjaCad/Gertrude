from testing_base import *

def turn_loop(turn_list, rounds = 1):
#Simulates the turn loop for testing purposes
 
    turn_order = []
    while rounds > 0:
        for player in turn_list:
            turn_order.append(player.name) 
            #every player in turn_list gets put into  turn_order's [] in original sequence
        rounds -= 1 #counts down each round
    return turn_order


def test_single_round_turn_order():
    turn_list = [Player("zack"), Player("jerry"), Player("lenny")]
    result = turn_loop(turn_list, rounds = 1)
    #1 turn with these players in the player turn list
    assert result == ["zack", "jerry", "lenny"]


def test_multiple_rounds_turn_order():
    turn_list = [Player("zack"), Player("jerry"), Player("lenny")]
    result = turn_loop(turn_list, rounds = 2)
    assert result == ["zack", "jerry", "lenny", "zack", "jerry", "lenny"]
    #this checks the order returns the original sequence of players
    assert result[0] == "zack"
    assert result[3] == "zack"
    #this returns zack's name, stating it comes around to zack at the beginning of each round