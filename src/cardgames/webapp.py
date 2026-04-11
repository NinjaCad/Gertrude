from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from cardgames.Card_Compare import Card
from cardgames.Dealer import Dealer
from cardgames.Deck import Deck
from cardgames.Games import Games, HighCardDrawInstructions, declare_winner
from cardgames.Player import Player
from cardgames.turns import switch_turn


app = FastAPI(title="CardGames Web API", version="1.0")


VALUE_NAMES = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King",
}


def card_label(card: Card) -> str:
    value = VALUE_NAMES.get(card.value, str(card.value))
    return f"{value} of {card.suit}"


@dataclass
class GameSession:
    game_id: str
    players: list[Player]
    dealer: Dealer
    phase: Literal["waiting_player1", "waiting_player2", "complete"] = "waiting_player1"
    player1_choice_idx: int | None = None
    player2_choice_idx: int | None = None
    winner: str | None = None


class NewGameRequest(BaseModel):
    player1_name: str = Field(default="PlayerX", min_length=1, max_length=50)
    player2_name: str = Field(default="PlayerY", min_length=1, max_length=50)


class ChooseCardRequest(BaseModel):
    card_index: int = Field(ge=0)


_SESSIONS: dict[str, GameSession] = {}
_PLAYER_PROFILES: dict[str, dict[str, int]] = {}
_GLOBAL_STATS = {"ties": 0}
_BACKEND_GAME_STATS: dict[tuple[str, str], dict] = {}


def _get_profile(name: str) -> dict[str, int]:
    if name not in _PLAYER_PROFILES:
        _PLAYER_PROFILES[name] = {"wins": 0, "redraw_tokens": 0}
    return _PLAYER_PROFILES[name]


@app.get("/")
def index():
    html_path = Path(__file__).resolve().parent / "web" / "index.html"
    return FileResponse(html_path)


def _serialize_game(session: GameSession) -> dict:
    current_player = None
    if session.phase == "waiting_player1":
        current_player = 0
    elif session.phase == "waiting_player2":
        current_player = 1

    def player_state(player: Player, player_idx: int) -> dict:
        mask_entire_hand = current_player is not None and player_idx != current_player

        cards = []
        for idx, card in enumerate(player.hand):
            known = True
            if idx < len(player.knownCards):
                known = player.knownCards[idx]

            if mask_entire_hand:
                known = False

            cards.append(
                {
                    "index": idx,
                    "known": known,
                    "label": card_label(card),
                    "display": card_label(card) if known else "Hidden card",
                }
            )

        chosen_label = None
        if player.chosen_card is not None and getattr(player.chosen_card, "suit", None):
            chosen_label = card_label(player.chosen_card)

        return {
            "name": player.name,
            "redraw_tokens": player.redraw_tokens,
            "cards": cards,
            "chosen_card": chosen_label,
        }

    winner_index = None
    if session.winner is not None:
        for i, p in enumerate(session.players):
            if session.winner == p.name:
                winner_index = i
                break

    player_names = (session.players[0].name, session.players[1].name)
    backend_stats = _BACKEND_GAME_STATS.get(player_names)

    return {
        "game_id": session.game_id,
        "phase": session.phase,
        "current_player_index": current_player,
        "winner": session.winner,
        "winner_index": winner_index,
        "backend_stats": backend_stats,
        "stats": {
            "ties": _GLOBAL_STATS["ties"],
            "players": {
                p.name: _get_profile(p.name)["wins"]
                for p in session.players
            },
        },
        "players": [player_state(p, i) for i, p in enumerate(session.players)],
    }


def _get_session_or_404(game_id: str) -> GameSession:
    session = _SESSIONS.get(game_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return session


def _setup_new_session(player1_name: str, player2_name: str) -> GameSession:
    deck = Deck()
    deck.shuffle()
    dealer = Dealer(deck)

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    # Carry profile state across rounds for same player names.
    player1.redraw_tokens = _get_profile(player1_name)["redraw_tokens"]
    player2.redraw_tokens = _get_profile(player2_name)["redraw_tokens"]

    ok = dealer.dealCards(3, [player1, player2])
    if not ok:
        raise HTTPException(status_code=500, detail="Unable to deal cards")

    return GameSession(game_id=str(uuid4()), players=[player1, player2], dealer=dealer)


@app.post("/api/games")
def create_game(request: NewGameRequest):
    session = _setup_new_session(request.player1_name, request.player2_name)
    _SESSIONS[session.game_id] = session
    return _serialize_game(session)


@app.get("/api/games/{game_id}")
def get_game(game_id: str):
    session = _get_session_or_404(game_id)
    return _serialize_game(session)


@app.post("/api/games/{game_id}/player1-choice")
def player1_choice(game_id: str, request: ChooseCardRequest):
    session = _get_session_or_404(game_id)
    if session.phase != "waiting_player1":
        raise HTTPException(status_code=409, detail="Game is not waiting for player 1")

    player1 = session.players[0]
    if request.card_index >= len(player1.hand):
        raise HTTPException(status_code=400, detail="card_index out of range for player 1")

    session.player1_choice_idx = request.card_index
    session.phase = "waiting_player2"
    return _serialize_game(session)


@app.post("/api/games/{game_id}/player2-choice")
def player2_choice(game_id: str, request: ChooseCardRequest):
    session = _get_session_or_404(game_id)
    if session.phase != "waiting_player2":
        raise HTTPException(status_code=409, detail="Game is not waiting for player 2")

    player2 = session.players[1]
    if request.card_index >= len(player2.hand):
        raise HTTPException(status_code=400, detail="card_index out of range for player 2")

    if session.player1_choice_idx is None:
        raise HTTPException(status_code=500, detail="Missing player 1 choice")

    # Reuse Sprint 2 logic exactly: hide current player's card + prompt next player.
    next_player_idx, p2_idx = switch_turn(
        players=session.players,
        current_player_index=0,
        chosen_card_index=session.player1_choice_idx,
        input_fn=lambda _prompt: str(request.card_index + 1),
        print_fn=lambda _msg: None,
    )

    session.player2_choice_idx = p2_idx
    session.players[0].chosen_card = session.players[0].hand[session.player1_choice_idx]
    session.players[next_player_idx].chosen_card = session.players[next_player_idx].hand[p2_idx]

    session.winner = declare_winner(session.players[0], session.players[1])

    # Track backend stats using existing Games.get_game_stats logic.
    p1_name = session.players[0].name
    p2_name = session.players[1].name
    pair_key = (p1_name, p2_name)
    current_backend_stats = _BACKEND_GAME_STATS.get(pair_key)
    _BACKEND_GAME_STATS[pair_key] = Games().get_game_stats(
        session.winner,
        [p1_name, p2_name],
        game_stats=current_backend_stats,
    )

    # Keep profile stats/tokens across rounds by player name.
    if session.winner == session.players[0].name:
        profile = _get_profile(session.players[0].name)
        profile["wins"] += 1
        profile["redraw_tokens"] += 1
        session.players[0].record_round_win()
    elif session.winner == session.players[1].name:
        profile = _get_profile(session.players[1].name)
        profile["wins"] += 1
        profile["redraw_tokens"] += 1
        session.players[1].record_round_win()
    else:
        _GLOBAL_STATS["ties"] += 1

    session.phase = "complete"

    return _serialize_game(session)


@app.get("/api/instructions/topics")
def get_instruction_topics():
    return {"topics": HighCardDrawInstructions.topics()}


@app.get("/api/instructions/{topic}")
def get_instruction(topic: str):
    try:
        return {"topic": topic, "text": HighCardDrawInstructions.get(topic)}
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex)) from ex


@app.post("/api/stats/reset")
def reset_stats():
    _PLAYER_PROFILES.clear()
    _BACKEND_GAME_STATS.clear()
    _GLOBAL_STATS["ties"] = 0
    return {"ok": True}


@app.post("/api/games/{game_id}/redraw-current")
def redraw_current_player(game_id: str):
    session = _get_session_or_404(game_id)
    if session.phase == "complete":
        raise HTTPException(status_code=409, detail="Round already complete")

    current_idx = 0 if session.phase == "waiting_player1" else 1
    player = session.players[current_idx]

    ok = session.dealer.redraw_three_card_options(player)
    if not ok:
        raise HTTPException(status_code=400, detail="No redraw token available or deck issue")

    # Persist token consumption to profile state.
    _get_profile(player.name)["redraw_tokens"] = player.redraw_tokens

    return _serialize_game(session)
