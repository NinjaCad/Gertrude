from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_start_game_route(client):
    response = client.get("/start_game")
    assert response.status_code == 200