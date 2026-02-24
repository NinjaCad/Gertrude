from testing_base import *


def test_create_players_with_id():
    game = Games()
    players = game.create_players()

    assert players is not None
    assert 2 <= len(players) <= 4

    print("Players:")
    for player in players:
        print(f"ID: {player.id}, Name: {player.name}")


if __name__ == "__main__":
    test_create_players_with_id()
