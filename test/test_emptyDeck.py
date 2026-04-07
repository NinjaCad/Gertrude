from testing_base import *

def test_empty_deck_turns():
    #create game
    game = Games()
    players = [Player("zack"), Player("gary")]
    
    #we empty the deck manually - 0 cards
    game.dealer.deck.cards = []
    print(f"Initial deck size: {len(game.dealer.deck.cards)}")

    #one round of turns
    for player in players:
        player.isTurn = True
        print(f"\n{player.name}'s turn (isTurn={player.isTurn})")
        drawn = None
        #draw a card
        if len(game.dealer.deck.cards) == 0:
            print("Draw pile is empty. Cannot pick up new cards.")
        else:
            card = game.dealer.deck.getCard()
            player.hand.append(card)

        player.isTurn = False
        print(f"End of turn (isTurn={player.isTurn})")
        
        assert drawn is None
        assert player.hand == []
