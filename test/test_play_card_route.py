from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_play_card(client):
    response = client.get("/play_card")
    assert response.status_code == 200

def test_play_card_route_data(client):
    response = client.get("/play_card")
    assert b'<form method="POST">' in response.data