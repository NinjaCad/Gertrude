from testing_base import *

def test_game_modes_dealing():
    game = Games()
    
#hyper mode
    
    game.dealer = Dealer(Deck())
    
    players_hyper = [Player("zack"), Player("gary")]
    print("\n--- Testing Hyper Mode ---")
    
    game.start_game(players_hyper, mode="hyper")
    
    for p in players_hyper:
        print(f"Player {p.name} hand size: {len(p.hand)}")
        assert len(p.hand) == 13, f"Hyper mode failed: {p.name} has {len(p.hand)} cards."

#speedy mode

    game.dealer = Dealer(Deck())

    players_speedy = [Player("mom"), Player("dad")]
    print("\n--- Testing Speedy Mode ---")
    
    game.start_game(players_speedy, mode="speedy")
    
    for p in players_speedy:
        print(f"Player {p.name} hand size: {len(p.hand)}")
        assert len(p.hand) == 10, f"Speedy mode failed: {p.name} has {len(p.hand)} cards."

#regular mode

    game.dealer = Dealer(Deck())

    players_reg = [Player("ron"), Player("dan"), Player("max")] 
    print("\n--- Testing Regular Mode (3 Players) ---")
    
    RegPlayers = game.start_game(players_reg, mode="regular")
    
    for p in RegPlayers:
        print(f"Player {p.name} hand size: {len(p.hand)}")
        assert len(p.hand) == 7, f"Regular (3p) failed: {p.name} has {len(p.hand)} cards."


if __name__ == "__main__":
    test_game_modes_dealing()