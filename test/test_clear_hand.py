import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cardgames.Player import Player
def test_clear_hand(): 
    player = Player("TestPlayer") 
    player.hand = ['2H', '3D', '5S']
    player.knownCards = ['2H', '3D']
    player.clearHand()
    
    assert player.hand == []
    assert player.knownCards == []


