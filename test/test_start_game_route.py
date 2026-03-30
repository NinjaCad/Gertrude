from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

#test status_code
def test_start_game_route(client):
    response = client.get("/start_game")
    assert response.status_code == 200

#test correct data in response
def test_start_game_route_data(client):
    #referenced https://stackoverflow.com/questions/69370708/how-can-i-use-pytest-to-test-routes-created-using-flask for help with creating this test
    response = client.get("/start_game")
    assert b'<button type="submit">Play Card</button>' in response.data