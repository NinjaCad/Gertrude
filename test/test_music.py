import sys

import pytest

from testing_base import Games


def test_choose_music_track_weighting(monkeypatch):
    game = Games()
    monkeypatch.setattr("cardgames.Games.random.random", lambda: 0.10)
    assert game.choose_music_track().name == game.COCONUT_MALL_TRACK

    monkeypatch.setattr("cardgames.Games.random.random", lambda: 0.99)
    assert game.choose_music_track().name == game.FINAL_COUNTDOWN_TRACK


def test_choose_music_playback_mode():
    game = Games()
    assert game.choose_music_playback_mode(lambda _: "1") == game.TEN_SECOND_TEST
    assert game.choose_music_playback_mode(lambda _: "2") == game.FULL_TEST
    assert game.choose_music_playback_mode(lambda _: "3") == game.REPEAT_FOREVER
    assert game.choose_music_playback_mode(lambda _: "") == game.REPEAT_FOREVER


def test_choose_music_playback_mode_reprompts_until_valid():
    game = Games()
    answers = iter(["x", "4", "2"])
    assert game.choose_music_playback_mode(lambda _: next(answers)) == game.FULL_TEST


def test_play_background_music_repeat_forever_uses_pygame(monkeypatch, tmp_path):
    class FakeMusic:
        def __init__(self):
            self.loaded = None
            self.play_args = None
            self.stop_called = False

        def load(self, path):
            self.loaded = path

        def play(self, loops):
            self.play_args = loops

        def stop(self):
            self.stop_called = True

    class FakeTime:
        def __init__(self):
            self.wait_ms = None

        def wait(self, ms):
            self.wait_ms = ms

    class FakeMixer:
        def __init__(self):
            self.initialized = False
            self.music = FakeMusic()

        def get_init(self):
            return (44100, -16, 2) if self.initialized else None

        def init(self):
            self.initialized = True

    class FakePygame:
        def __init__(self):
            self.mixer = FakeMixer()
            self.time = FakeTime()

    fake_pygame = FakePygame()
    monkeypatch.setitem(sys.modules, "pygame", fake_pygame)

    game = Games()
    game.assets_dir = tmp_path
    track_path = tmp_path / game.COCONUT_MALL_TRACK
    track_path.write_bytes(b"placeholder")
    monkeypatch.setattr(game, "choose_music_track", lambda: track_path)

    selected = game.play_background_music()
    assert selected == track_path
    assert fake_pygame.mixer.initialized is True
    assert fake_pygame.mixer.music.loaded == str(track_path)
    assert fake_pygame.mixer.music.play_args == -1
    assert fake_pygame.mixer.music.stop_called is False
    assert fake_pygame.time.wait_ms is None


def test_play_background_music_ten_second_mode_waits_and_stops(monkeypatch, tmp_path):
    class FakeMusic:
        def __init__(self):
            self.loaded = None
            self.play_args = None
            self.stop_called = False

        def load(self, path):
            self.loaded = path

        def play(self, loops):
            self.play_args = loops

        def stop(self):
            self.stop_called = True

    class FakeTime:
        def __init__(self):
            self.wait_ms = None

        def wait(self, ms):
            self.wait_ms = ms

    class FakeMixer:
        def __init__(self):
            self.initialized = False
            self.music = FakeMusic()

        def get_init(self):
            return (44100, -16, 2) if self.initialized else None

        def init(self):
            self.initialized = True

    class FakePygame:
        def __init__(self):
            self.mixer = FakeMixer()
            self.time = FakeTime()

    fake_pygame = FakePygame()
    monkeypatch.setitem(sys.modules, "pygame", fake_pygame)

    game = Games()
    game.assets_dir = tmp_path
    track_path = tmp_path / game.COCONUT_MALL_TRACK
    track_path.write_bytes(b"placeholder")
    monkeypatch.setattr(game, "choose_music_track", lambda: track_path)

    selected = game.play_background_music(game.TEN_SECOND_TEST)
    assert selected == track_path
    assert fake_pygame.mixer.music.play_args == 0
    assert fake_pygame.time.wait_ms == 10000
    assert fake_pygame.mixer.music.stop_called is True


def test_real_music_playback_smoke():
    pygame = pytest.importorskip("pygame")
    game = Games()
    track_path = game.assets_dir / game.COCONUT_MALL_TRACK
    if not track_path.exists():
        pytest.skip(f"Missing audio file: {track_path}")

    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
    except Exception as exc:
        pytest.skip(f"Unable to initialize audio mixer: {exc}")

    pygame.mixer.music.load(str(track_path))
    pygame.mixer.music.play(0)
    pygame.time.wait(10000)
    pygame.mixer.music.stop()
    assert True


def test_goldfish_music_playback_smoke():
    pygame = pytest.importorskip("pygame")
    game = Games()
    track_path = game.assets_dir / game.GOLDFISH_TRACK
    if not track_path.exists():
        pytest.skip(f"Missing audio file: {track_path}")

    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
    except Exception as exc:
        pytest.skip(f"Unable to initialize audio mixer: {exc}")

    pygame.mixer.music.load(str(track_path))
    pygame.mixer.music.play(0)
    pygame.time.wait(2000)
    pygame.mixer.music.stop()
    assert True


def test_final_countdown_music_playback_smoke():
    pygame = pytest.importorskip("pygame")
    game = Games()
    track_path = game.assets_dir / game.FINAL_COUNTDOWN_TRACK
    if not track_path.exists():
        pytest.skip(f"Missing audio file: {track_path}")

    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
    except Exception as exc:
        pytest.skip(f"Unable to initialize audio mixer: {exc}")

    pygame.mixer.music.load(str(track_path))
    pygame.mixer.music.play(0)
    pygame.time.wait(2000)
    pygame.mixer.music.stop()
    assert True


def test_smooth_jazz_infinite_loop_smoke():
    pygame = pytest.importorskip("pygame")
    game = Games()
    track_path = game.assets_dir / game.SMOOTH_JAZZ_TRACK
    if not track_path.exists():
        pytest.skip(f"Missing audio file: {track_path}")

    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
    except Exception as exc:
        pytest.skip(f"Unable to initialize audio mixer: {exc}")

    pygame.mixer.music.load(str(track_path))
    pygame.mixer.music.play(-1)
    pygame.time.wait(2000)
    pygame.mixer.music.stop()
    assert True
