from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_lobby(client):
    response = client.get("/lobby")
    assert response.status_code == 200

def test_game(client):
    response = client.get("/game")
    assert response.status_code == 200

def test_stream_response(client):
    response = client.get("/stream", buffered=False)
    assert response.status_code == 200

def test_stream(client):
    response = client.get("/stream", buffered=False)
    first = next(response.response)
    assert b"PLACEHOLDER" in first