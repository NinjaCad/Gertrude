from cardgames.Deck import Deck

def blank(game_state, player_list):                                              #counter function
    """Increments counter and returns (rank, player_index)"""
    game_state['counter'] += 1
    current_count = game_state['counter']
    return current_count % 13, current_count % len(player_list)                  #return rank and person who turn it is


if __name__ == "__main__":
    deck = Deck()
    players = ['Joseph', 'Rose', 'David', 'Faith', 'Eli', 'Daniel']
    game_state = {'counter': 0}