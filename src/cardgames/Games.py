from cardgames.Deck import Deck

class Games:

    def __init__(self, player_list):
        self.deck = Deck()
        self.player_list = player_list
        self.GAME_STATE = {'counter': 0}

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        print('First 5 cards in standard 52-card deck:')
        for card in self.deck.cards[:5]:
            print(card)
        input('Press [Enter] to exit.')

    def blank(self):                                                          #counter function
        self.GAME_STATE['counter'] += 1
        current_count = self.GAME_STATE['counter']
        return current_count % 13, current_count % len(self.player_list)      #return rank and person who turn it is


if __name__ == "__main__":
    players = ['Joseph', 'Rose', 'David', 'Faith', 'Eli', 'Daniel']
    game = Games(players)
    game.main()