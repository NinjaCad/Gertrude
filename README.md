# Gertrude (cardgames)

A simple terminal-based card game project written in **Python**.

> Fact check: although the GitHub repo description mentions JavaScript, the current code in this repository is primarily Python (see `pyproject.toml`, `requirements.txt`, and `src/cardgames/*.py`).

## What’s in this repo

- **Game code**: `src/cardgames/`
  - `Games.py` — entrypoint that starts the game
  - `Deck.py`, `Card.py` — card/deck logic
  - `Player.py`, `Dealer.py` — player/dealer behavior
  - `playing_cards.txt` — data file used by the game
- **Tests**: `test/`
- **Python packaging**: `pyproject.toml`
- **Dependencies**: `requirements.txt`
- **Docker**: `Dockerfile`

## Requirements

- Python **3.10.x** (the Docker image uses `python:3.10.16`).

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run locally

From the repository root:

```bash
python -m src.cardgames.Games
```

If that does not work in your environment (module path issues), run the file directly:

```bash
python src/cardgames/Games.py
```

## Run with Docker

Build:

```bash
docker build -t gertrude .
```

Run:

```bash
docker run --rm -it gertrude
```

## Run tests

```bash
pytest
```

Optional (HTML report, if configured/desired):

```bash
pytest --html=test-reports/report.html
```

## Notes / known mismatches

- The repository description says “blackjack using JavaScript”, but the current implementation in `dev_gertrude` is Python.
  - Safest verification step: open `src/cardgames/Games.py` and confirm the game being implemented.
