from testing_base import *
import pytest
import flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_page_2_has_audio(client):
    response = client.post("/", data={"player_name": "Joey"}, follow_redirects=True)
    html = response.data.decode()
    assert '<audio id="sfx"' in html
    assert 'preload="auto"' in html

def test_play_sound_js_present_page_2(client):
    response = client.post("/", data={"player_name": "Joey"}, follow_redirects=True)
    html = response.data.decode()
    assert "function play_sound" in html
    assert "/static/sfx/" in html

def test_page_3_has_audio(client):
    response = client.post("/", data={"player_name": "Joey"}, follow_redirects=True)
    response = client.get("/game")
    html = response.data.decode()
    assert '<audio id="sfx"' in html
    assert 'preload="auto"' in html

def test_play_sound_js_present_page_3(client):
    response = client.post("/", data={"player_name": "Joey"}, follow_redirects=True)
    response = client.get("/game")
    html = response.data.decode()
    assert "function play_sound" in html
    assert "/static/sfx/" in html