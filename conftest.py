import pytest


@pytest.fixture(autouse=True)
def _noninteractive_input(monkeypatch):
    """Provide deterministic input for legacy interactive tests."""

    def _fake_input(prompt: str = "") -> str:
        if "Press 's'" in prompt:
            return "s"
        return ""

    monkeypatch.setattr("builtins.input", _fake_input)


def pytest_collection_modifyitems(items):
    """Skip imported stdlib self-test accidentally collected by pytest."""
    for item in items:
        if item.nodeid.endswith("test/test_mid_screen.py::test"):
            item.add_marker(pytest.mark.skip(reason="stdlib ctypes.util.test is not a project test"))
