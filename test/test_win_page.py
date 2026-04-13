from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_win_page_route(client):
    response = client.get("/win_page")
    assert response.status_code == 200

def test_win_page_data(client):
    response = client.get("/win_page")
    assert b'<button id="invisible_button"><a href="/home">Real Home Page</a></button>' in response.data