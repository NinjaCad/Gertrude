from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

#test status_code
def test_play_card(client):
    response = client.get("/play_card")
    assert response.status_code == 200

#test correct data in response
def test_play_card_route_data(client):
    #referenced https://stackoverflow.com/questions/69370708/how-can-i-use-pytest-to-test-routes-created-using-flask for help with creating this test
    response = client.get("/play_card")
    assert b'<form method="POST">' in response.data

#test to check that post requests work as intended, as requested by Daniel Sisay
def test_play_card_post(client):
    # referenced https://stackoverflow.com/questions/27004815/flask-test-response-to-post-request-incorrectly-returns-400 for help with creating this test
    response = client.post("/play_card")
    assert response.status_code == 200