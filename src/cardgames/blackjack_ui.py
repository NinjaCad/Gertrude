import tkinter as tk
from tkinter import ttk, messagebox

from cardgames.Player import Player, Gertrude
from cardgames.Dealer import Dealer
from cardgames.Deck import Deck


SUIT_SYMBOLS = {
    "S": "♠",
    "H": "♥",
    "D": "♦",
    "C": "♣",
}
VALUE_LABELS = {
    1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
    8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"
}


def fmt(amount):
    if isinstance(amount, float) and amount.is_integer():
        return str(int(amount))
    return str(amount)


def card_label(card):
    value = VALUE_LABELS.get(card.value, str(card.value))
    suit = SUIT_SYMBOLS.get(card.suit, card.suit)
    return f"{value}{suit}"


def card_lines(card, known=True, short=False):
    if not known:
        return list(card.cardBack)
    if short and hasattr(card, "shortImage"):
        return list(card.shortImage)
    return list(card.image)


def hand_to_ascii(player, compress=False):
    if not player.hand:
        return "(no cards)"

    rows = []
    for row_idx in range(6):
        row = []
        for i, card in enumerate(player.hand):
            known = player.knownCards[i] if i < len(player.knownCards) else True
            use_short = compress and i < len(player.hand) - 1
            lines = card_lines(card, known=known, short=use_short)
            row.append(lines[row_idx] if row_idx < len(lines) else "")
        rows.append("".join(row))
    return "\n".join(rows)


class UiGameAdapter:
    """
    Small adapter so Player.split(game) works from the UI.
    Your newest Player.split expects a game object with:
    - game.playerList
    - game.dealer
    """
    def __init__(self, players, dealer):
        self.playerList = players
        self.dealer = dealer


class HandPanel(ttk.LabelFrame):
    def __init__(self, parent, title):
        super().__init__(parent, text=title, padding=8)
        self.columnconfigure(0, weight=1)

        self.header_var = tk.StringVar(value=title)
        self.info_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value="")

        ttk.Label(self, textvariable=self.header_var).grid(row=0, column=0, sticky="w")
        ttk.Label(self, textvariable=self.info_var).grid(row=1, column=0, sticky="w", pady=(2, 0))
        ttk.Label(self, textvariable=self.status_var).grid(row=2, column=0, sticky="w", pady=(2, 4))

        self.hand_text = tk.Text(self, height=8, width=48, wrap="none")
        self.hand_text.grid(row=3, column=0, sticky="nsew")
        self.hand_text.configure(state="disabled", font=("Courier New", 10))


class BlackjackUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gertrude Blackjack UI")
        self.root.geometry("1500x950")

        self.players = []
        self.current_player_index = 1
        self.game_started = False
        self.betting_mode = False
        self.round_active = False
        self.starting_money = 100

        self.deck = None
        self.dealer = None
        self.player_panels = []

        self.side_bets_included = {
            "insurance": tk.BooleanVar(value=False),
            "perfect pairs": tk.BooleanVar(value=False),
            "21+3": tk.BooleanVar(value=False),
            "tipping": tk.BooleanVar(value=False),
        }

        self.setup_styles()
        self.setup_ui()

    def setup_styles(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("Current.TLabelframe", borderwidth=3)
        style.configure("Current.TLabelframe.Label", font=("TkDefaultFont", 10, "bold"))

    def setup_ui(self):
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(1, weight=1)

        top = ttk.Frame(self.root, padding=10)
        top.grid(row=0, column=0, columnspan=2, sticky="ew")
        top.columnconfigure(1, weight=1)

        ttk.Label(top, text="Players (1-7):").grid(row=0, column=0, sticky="w")
        self.num_players_var = tk.StringVar(value="2")
        ttk.Entry(top, textvariable=self.num_players_var, width=8).grid(row=0, column=1, sticky="w", padx=(8, 0))
        ttk.Button(top, text="Build name fields", command=self.build_name_fields).grid(row=0, column=2, padx=(10, 0))

        ttk.Label(top, text="Starting money:").grid(row=0, column=3, sticky="w", padx=(16, 0))
        self.starting_money_var = tk.StringVar(value="100")
        ttk.Entry(top, textvariable=self.starting_money_var, width=10).grid(row=0, column=4, sticky="w", padx=(8, 0))

        self.names_frame = ttk.Frame(top)
        self.names_frame.grid(row=1, column=0, columnspan=5, sticky="ew", pady=(8, 0))
        self.name_vars = []

        side_frame = ttk.LabelFrame(top, text="Optional side features", padding=8)
        side_frame.grid(row=2, column=0, columnspan=5, sticky="ew", pady=(8, 0))

        ttk.Checkbutton(side_frame, text="Insurance", variable=self.side_bets_included["insurance"]).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(side_frame, text="Perfect Pairs", variable=self.side_bets_included["perfect pairs"]).grid(row=0, column=1, sticky="w", padx=(12, 0))
        ttk.Checkbutton(side_frame, text="21+3", variable=self.side_bets_included["21+3"]).grid(row=0, column=2, sticky="w", padx=(12, 0))
        ttk.Checkbutton(side_frame, text="Tipping", variable=self.side_bets_included["tipping"]).grid(row=0, column=3, sticky="w", padx=(12, 0))

        ttk.Button(top, text="Start game", command=self.start_game).grid(row=3, column=0, columnspan=5, sticky="ew", pady=(8, 0))

        left = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        left.grid(row=1, column=0, sticky="nsew")
        left.columnconfigure(0, weight=1)
        left.rowconfigure(1, weight=1)

        right = ttk.Frame(self.root, padding=(0, 0, 10, 10))
        right.grid(row=1, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(3, weight=1)

        self.status_var = tk.StringVar(value="Set up players, then start the game.")
        ttk.Label(left, textvariable=self.status_var, wraplength=850).grid(row=0, column=0, sticky="ew", pady=(0, 10))

        self.table_container = ttk.Frame(left)
        self.table_container.grid(row=1, column=0, sticky="nsew")
        self.table_container.columnconfigure(0, weight=1)
        self.table_container.columnconfigure(1, weight=1)
        self.table_container.columnconfigure(2, weight=1)
        self.table_container.rowconfigure(1, weight=1)

        self.dealer_panel = HandPanel(self.table_container, "Gertrude")
        self.dealer_panel.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 10))

        self.players_grid = ttk.Frame(self.table_container)
        self.players_grid.grid(row=1, column=0, columnspan=3, sticky="nsew")
        for c in range(3):
            self.players_grid.columnconfigure(c, weight=1)

        control_box = ttk.LabelFrame(right, text="Controls", padding=10)
        control_box.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        control_box.columnconfigure(1, weight=1)

        ttk.Label(control_box, text="Standard bet:").grid(row=0, column=0, sticky="w")
        self.standard_bet_var = tk.StringVar(value="5")
        ttk.Entry(control_box, textvariable=self.standard_bet_var).grid(row=0, column=1, sticky="ew", padx=(8, 0))

        ttk.Label(control_box, text="Pairs bet:").grid(row=1, column=0, sticky="w")
        self.pairs_bet_var = tk.StringVar(value="0")
        ttk.Entry(control_box, textvariable=self.pairs_bet_var).grid(row=1, column=1, sticky="ew", padx=(8, 0), pady=(4, 0))

        ttk.Label(control_box, text="21+3 bet:").grid(row=2, column=0, sticky="w")
        self.twentyone_bet_var = tk.StringVar(value="0")
        ttk.Entry(control_box, textvariable=self.twentyone_bet_var).grid(row=2, column=1, sticky="ew", padx=(8, 0), pady=(4, 0))

        ttk.Label(control_box, text="Insurance bet:").grid(row=3, column=0, sticky="w")
        self.insurance_bet_var = tk.StringVar(value="0")
        ttk.Entry(control_box, textvariable=self.insurance_bet_var).grid(row=3, column=1, sticky="ew", padx=(8, 0), pady=(4, 0))

        self.place_bet_btn = ttk.Button(control_box, text="Place bet", command=self.place_bet)
        self.place_bet_btn.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        self.hit_btn = ttk.Button(control_box, text="Hit", command=self.hit_current, state="disabled")
        self.hit_btn.grid(row=5, column=0, sticky="ew", pady=(8, 0))

        self.stand_btn = ttk.Button(control_box, text="Stand", command=self.stand_current, state="disabled")
        self.stand_btn.grid(row=5, column=1, sticky="ew", padx=(8, 0), pady=(8, 0))

        self.split_btn = ttk.Button(control_box, text="Split", command=self.split_current, state="disabled")
        self.split_btn.grid(row=6, column=0, sticky="ew", pady=(8, 0))

        self.double_btn = ttk.Button(control_box, text="Double Down", command=self.double_current, state="disabled")
        self.double_btn.grid(row=6, column=1, sticky="ew", padx=(8, 0), pady=(8, 0))

        self.help_btn = ttk.Button(control_box, text="Show help", command=self.show_help, state="disabled")
        self.help_btn.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        self.next_round_btn = ttk.Button(control_box, text="Next round", command=self.next_round, state="disabled")
        self.next_round_btn.grid(row=8, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        score_box = ttk.LabelFrame(right, text="Scoreboard", padding=10)
        score_box.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        score_box.columnconfigure(0, weight=1)

        self.score_text = tk.Text(score_box, height=14, wrap="word")
        self.score_text.grid(row=0, column=0, sticky="ew")
        self.score_text.configure(state="disabled")

        note_box = ttk.LabelFrame(right, text="Active rules", padding=10)
        note_box.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        self.rules_var = tk.StringVar(value="21 locks the player. 21 pays 2.5x only if the player wins.")
        ttk.Label(note_box, textvariable=self.rules_var, wraplength=520).grid(row=0, column=0, sticky="w")

        log_box = ttk.LabelFrame(right, text="Game log", padding=10)
        log_box.grid(row=3, column=0, sticky="nsew")
        log_box.columnconfigure(0, weight=1)
        log_box.rowconfigure(0, weight=1)

        self.log_text = tk.Text(log_box, wrap="word")
        self.log_text.grid(row=0, column=0, sticky="nsew")
        self.log_text.configure(state="disabled")

        self.build_name_fields()

    def log(self, message=""):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def set_text(self, widget, value):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", value)
        widget.configure(state="disabled")

    def set_panel_text(self, panel, value):
        panel.hand_text.configure(state="normal")
        panel.hand_text.delete("1.0", "end")
        panel.hand_text.insert("1.0", value)
        panel.hand_text.configure(state="disabled")

    def build_name_fields(self):
        for child in self.names_frame.winfo_children():
            child.destroy()
        self.name_vars.clear()

        try:
            count = int(self.num_players_var.get())
        except ValueError:
            count = 2

        count = max(1, min(7, count))
        self.num_players_var.set(str(count))

        for i in range(count):
            ttk.Label(self.names_frame, text=f"Player {i + 1} name:").grid(row=i, column=0, sticky="w", pady=2)
            var = tk.StringVar(value=f"Player {i + 1}")
            ttk.Entry(self.names_frame, textvariable=var, width=24).grid(row=i, column=1, sticky="w", padx=(8, 0), pady=2)
            self.name_vars.append(var)

    def create_player_panels(self):
        for child in self.players_grid.winfo_children():
            child.destroy()
        self.player_panels = []

        for idx, player in enumerate(self.players[1:]):
            panel = HandPanel(self.players_grid, player.name)
            row = idx // 3
            col = idx % 3
            panel.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            self.players_grid.rowconfigure(row, weight=1)
            self.player_panels.append(panel)

    def get_enabled_side_bets(self):
        return {key: value.get() for key, value in self.side_bets_included.items()}

    def start_game(self):
        names = [v.get().strip() for v in self.name_vars]
        if any(not name for name in names):
            messagebox.showerror("Missing name", "Every player needs a name.")
            return
        if any("hand" in name.lower() for name in names):
            messagebox.showerror("Invalid name", "Player names cannot contain the word 'hand' because split hands use that word.")
            return

        try:
            starting_money = int(self.starting_money_var.get().strip())
        except ValueError:
            messagebox.showerror("Invalid money", "Starting money must be a whole number.")
            return

        if starting_money <= 5:
            messagebox.showerror("Invalid money", "Starting money must be more than $5.")
            return

        self.starting_money = starting_money
        self.deck = Deck()
        self.dealer = Dealer(self.deck)

        self.players = [Gertrude("GERTRUDE")]
        for name in names:
            player = Player(name)
            player.money = starting_money
            self.players.append(player)

        self.create_player_panels()
        self.game_started = True
        self.betting_mode = True
        self.round_active = False
        self.current_player_index = 1

        self.place_bet_btn.configure(state="normal")
        self.hit_btn.configure(state="disabled")
        self.stand_btn.configure(state="disabled")
        self.split_btn.configure(state="disabled")
        self.double_btn.configure(state="disabled")
        self.help_btn.configure(state="disabled")
        self.next_round_btn.configure(state="disabled")

        self.log("Welcome to Gertrude's BlackJack!")
        self.log(f"Players at the table: {', '.join(names)}")
        self.log(f"Starting money: ${starting_money}")
        self.status_var.set("Game started. Place bets for each active player.")
        self.refresh_all()
        self.show_current_betting_player()

    def refresh_scoreboard(self):
        if not self.players:
            self.set_text(self.score_text, "No players yet.")
            return

        lines = []
        for i, player in enumerate(self.players[1:], start=1):
            turn_marker = "  <-- current" if self.game_started and i == self.current_player_index else ""
            hand_value = player.check_cards() if player.hand else "-"
            active_label = "active" if player.active else "inactive"
            lines.append(
                f"{player.name}: ${fmt(player.money)} | "
                f"standard ${fmt(player.bets.get('standard', 0))} | "
                f"pairs ${fmt(player.bets.get('pairs', 0))} | "
                f"21+3 ${fmt(player.bets.get('21+3', 0))} | "
                f"insurance ${fmt(player.bets.get('insurance', 0))} | "
                f"hand {hand_value} | {active_label}{turn_marker}"
            )
        self.set_text(self.score_text, "\n".join(lines))

    def visible_score(self, player):
        total_score = 0
        num_aces = 0

        for i, card in enumerate(player.hand):
            known = player.knownCards[i] if i < len(player.knownCards) else True
            if not known:
                continue

            rank_index = card.value
            if rank_index == 1:
                val = 11
                num_aces += 1
            elif rank_index >= 11:
                val = 10
            else:
                val = rank_index
            total_score += val

        while total_score > 21 and num_aces > 0:
            total_score -= 10
            num_aces -= 1

        return total_score

    def update_dealer_panel(self):
        if not self.players:
            self.dealer_panel.header_var.set("Gertrude")
            self.dealer_panel.info_var.set("")
            self.dealer_panel.status_var.set("")
            self.set_panel_text(self.dealer_panel, "")
            return

        dealer = self.players[0]
        dealer_full = all(dealer.knownCards) if dealer.knownCards else False
        score = dealer.check_cards() if dealer_full and dealer.hand else self.visible_score(dealer)

        self.dealer_panel.header_var.set("Gertrude")
        self.dealer_panel.info_var.set(f"Hand value: {score if dealer.hand else '-'}")
        self.dealer_panel.status_var.set("Dealer turn complete" if dealer_full and dealer.hand else "One card hidden" if dealer.hand else "Waiting for round")
        self.set_panel_text(self.dealer_panel, hand_to_ascii(dealer, compress=True))

    def update_player_panels(self):
        self.create_player_panels()

        for idx, panel in enumerate(self.player_panels, start=1):
            player = self.players[idx]
            panel.configure(style="TLabelframe")

            hand_value = player.check_cards() if player.hand else "-"
            panel.header_var.set(player.name)
            panel.info_var.set(
                f"Money: ${fmt(player.money)} | "
                f"Standard: ${fmt(player.bets.get('standard', 0))} | "
                f"Pairs: ${fmt(player.bets.get('pairs', 0))} | "
                f"21+3: ${fmt(player.bets.get('21+3', 0))}"
            )

            if player.money < 5 and not player.hand:
                status = "Bankrupt"
            elif not player.hand:
                status = "Waiting for round"
            elif player.hand and player.check_cards() == 21:
                status = "21! Locked"
            elif player.hand and player.check_cards() > 21:
                status = "Bust"
            elif self.betting_mode and idx == self.current_player_index:
                status = "Place your bet"
            elif idx == self.current_player_index and player.active:
                status = "Your turn"
            elif player.hand and not player.active:
                status = "Stand"
            else:
                status = "Waiting"

            panel.status_var.set(status)

            if idx == self.current_player_index and (self.betting_mode or (player.hand and player.active)):
                panel.configure(style="Current.TLabelframe")

            self.set_panel_text(panel, hand_to_ascii(player, compress=False))

    def refresh_all(self):
        self.update_dealer_panel()
        self.update_player_panels()
        self.refresh_scoreboard()
        self.update_action_buttons()

    def update_action_buttons(self):
        player = self.current_player()

        can_act = (
            player is not None
            and self.round_active
            and not self.betting_mode
            and player.active
            and player.hand
        )

        self.hit_btn.configure(state="normal" if can_act else "disabled")
        self.stand_btn.configure(state="normal" if can_act else "disabled")
        self.help_btn.configure(state="normal" if can_act else "disabled")

        can_split = can_act and hasattr(player, "can_split") and player.can_split()
        can_double = can_act and hasattr(player, "can_double") and player.can_double()

        self.split_btn.configure(state="normal" if can_split else "disabled")
        self.double_btn.configure(state="normal" if can_double else "disabled")

    def show_current_betting_player(self):
        while self.current_player_index < len(self.players):
            player = self.players[self.current_player_index]
            if player.money >= 5:
                break
            player.active = False
            self.log(f"{player.name} has less than $5 and is skipped.")
            self.current_player_index += 1

        if self.current_player_index >= len(self.players):
            self.begin_round()
            return

        player = self.players[self.current_player_index]
        self.standard_bet_var.set("5")
        self.pairs_bet_var.set("0")
        self.twentyone_bet_var.set("0")
        self.insurance_bet_var.set("0")

        self.status_var.set(f"{player.name}: enter bets and click Place bet.")
        self.refresh_all()

    def read_bet_value(self, var, label):
        try:
            value = int(var.get().strip())
        except ValueError:
            raise ValueError(f"{label} must be a whole number.")
        if value < 0:
            raise ValueError(f"{label} cannot be negative.")
        return value

    def place_bet(self):
        if not self.game_started or not self.betting_mode:
            return

        player = self.players[self.current_player_index]
        side_bets = self.get_enabled_side_bets()

        try:
            standard = self.read_bet_value(self.standard_bet_var, "Standard bet")
            pairs = self.read_bet_value(self.pairs_bet_var, "Pairs bet")
            twentyone = self.read_bet_value(self.twentyone_bet_var, "21+3 bet")
        except ValueError as exc:
            messagebox.showerror("Invalid bet", str(exc))
            return

        if standard < 5:
            messagebox.showerror("Invalid bet", "Standard bet must be at least $5.")
            return

        if not side_bets["perfect pairs"]:
            pairs = 0
        if not side_bets["21+3"]:
            twentyone = 0

        total = standard + pairs + twentyone
        if player.money - total < 0:
            messagebox.showerror("Invalid bet", "Player cannot bet more money than they have.")
            return

        player.bets["standard"] = float(standard)
        player.bets["pairs"] = float(pairs)
        player.bets["21+3"] = float(twentyone)
        player.bets["insurance"] = 0.0

        self.log(
            f"{player.name} bets standard ${fmt(player.bets['standard'])}, "
            f"pairs ${fmt(player.bets['pairs'])}, "
            f"21+3 ${fmt(player.bets['21+3'])}."
        )

        self.current_player_index += 1
        if self.current_player_index < len(self.players):
            self.show_current_betting_player()
        else:
            self.begin_round()

        self.refresh_all()

    def begin_round(self):
        self.betting_mode = False
        self.round_active = True

        for player in self.players:
            if player.money >= 5 or player.name == "GERTRUDE":
                player.active = True
            player.clearHand()

        dealt = self.dealer.dealCards(2, self.players)
        if dealt is False:
            messagebox.showerror("Deck error", "Not enough cards to deal.")
            return

        self.resolve_starting_side_bets()
        self.handle_insurance_if_needed()

        self.current_player_index = 1
        self.place_bet_btn.configure(state="disabled")
        self.next_round_btn.configure(state="disabled")

        self.log("")
        self.log("--- New round started ---")
        self.log("Initial cards dealt.")
        self.status_var.set(f"{self.players[self.current_player_index].name}'s turn.")
        self.refresh_all()
        self.advance_past_finished_players(initial=True)

    def resolve_starting_side_bets(self):
        side_bets = self.get_enabled_side_bets()
        dealer_up_card = self.players[0].hand[0] if self.players[0].hand else None

        for player in self.players[1:]:
            if not player.active:
                continue

            results = {}

            if side_bets["perfect pairs"]:
                results["pairs"] = player.perfectPairs()
            else:
                player.bets["pairs"] = 0.0

            if side_bets["21+3"]:
                results["21+3"] = player.twentyone(dealer_up_card)
            else:
                player.bets["21+3"] = 0.0

            if results:
                self.resolve_bets_no_prompt(player, results, label="side bet")

    def handle_insurance_if_needed(self):
        side_bets = self.get_enabled_side_bets()
        dealer = self.players[0]

        if not side_bets["insurance"]:
            return
        if not dealer.hand or dealer.hand[0].value != 1:
            return

        self.log("Gertrude shows an Ace. Insurance is available.")

        for player in self.players[1:]:
            if player.active:
                max_insurance = int(player.bets["standard"] // 2)
                if max_insurance > 0:
                    self.log(f"{player.name} can place up to ${max_insurance} insurance before their turn.")

    def current_player(self):
        if 1 <= self.current_player_index < len(self.players):
            return self.players[self.current_player_index]
        return None

    def hit_current(self):
        player = self.current_player()
        if player is None:
            return

        card = player.hit(self.dealer)

        if card is None:
            score = player.check_cards()
            self.log(f"{player.name} cannot hit. Hand value: {score}.")
            self.advance_to_next_player()
            self.refresh_all()
            return

        self.log(f"{player.name} hits and draws {card_label(card)}.")

        score = player.check_cards()
        if score > 21:
            self.log(f"{player.name} busts with {score}.")
            self.log(self.players[0].trashTalk("bust"))
            self.advance_to_next_player()
        elif score == 21:
            self.log(f"{player.name} hits 21. Standard bet is now worth ${fmt(player.bets['standard'])} if they win.")
            self.advance_to_next_player()
        else:
            self.log(self.players[0].trashTalk("hit"))
            self.status_var.set(f"{player.name}'s turn. Hand value: {score}")

        self.refresh_all()

    def stand_current(self):
        player = self.current_player()
        if player is None:
            return

        player.stand()
        self.log(f"{player.name} stands with {player.check_cards()}.")
        self.log(self.players[0].trashTalk("stand"))
        self.advance_to_next_player()
        self.refresh_all()

    def split_current(self):
        player = self.current_player()
        if player is None:
            return

        if not player.can_split():
            messagebox.showinfo("Cannot split", "This player cannot split right now.")
            return

        old_count = len(self.players)
        adapter = UiGameAdapter(self.players, self.dealer)
        player.split(adapter)
        self.players = adapter.playerList

        if len(self.players) != old_count:
            self.log(f"{player.name} split their hand.")
            self.log(self.players[0].trashTalk("split"))
        else:
            self.log(f"{player.name} attempted to split.")

        self.refresh_all()

    def double_current(self):
        player = self.current_player()
        if player is None:
            return

        if not player.can_double():
            messagebox.showinfo("Cannot double down", "This player cannot double down right now.")
            return

        player.double_down(self.dealer)
        self.log(f"{player.name} doubles down. Standard bet is now ${fmt(player.bets['standard'])}.")
        self.log(self.players[0].trashTalk("double down"))

        score = player.check_cards()
        if score > 21:
            self.log(f"{player.name} busts with {score}.")
            self.log(self.players[0].trashTalk("bust"))
        elif score == 21:
            self.log(f"{player.name} reaches 21. Standard bet is now worth ${fmt(player.bets['standard'])} if they win.")

        self.advance_to_next_player()
        self.refresh_all()

    def advance_past_finished_players(self, initial=False):
        while True:
            player = self.current_player()
            if player is None:
                self.finish_players_phase()
                return

            if not player.active and not player.hand:
                self.current_player_index += 1
                continue

            score = player.check_cards()
            if score == 21 and not player.active:
                self.log(f"{player.name} has 21. Standard bet is now worth ${fmt(player.bets['standard'])} if they win.")
                self.current_player_index += 1
                continue

            if score > 21 or not player.active:
                self.current_player_index += 1
                continue

            break

        if not initial:
            self.status_var.set(f"{self.players[self.current_player_index].name}'s turn.")
        self.refresh_all()

    def advance_to_next_player(self):
        self.current_player_index += 1
        self.advance_past_finished_players()

    def finish_players_phase(self):
        self.hit_btn.configure(state="disabled")
        self.stand_btn.configure(state="disabled")
        self.split_btn.configure(state="disabled")
        self.double_btn.configure(state="disabled")
        self.help_btn.configure(state="disabled")

        dealer = self.players[0]
        dealer.knownCards = [True for _ in dealer.knownCards]

        self.log("")
        self.log("--- Gertrude's turn ---")
        self.log(f"Gertrude reveals hidden card. Current value: {dealer.check_cards()}")
        final = dealer.gertTurn(self.dealer)
        dealer.knownCards = [True for _ in dealer.knownCards]
        self.log(f"Gertrude ends with {final}.")
        self.resolve_round()

    def resolve_round(self):
        dealer = self.players[0]
        dealer_score = dealer.check_cards()

        self.log("")
        self.log("--- Results ---")
        tipping_enabled = self.side_bets_included["tipping"].get()

        for player in self.players[1:]:
            if not player.hand:
                continue

            player_score = player.check_cards()
            standard_result = False

            if player_score > 21:
                standard_result = False
                self.log(f"{player.name} busts and loses ${fmt(player.bets['standard'])}.")
            elif dealer_score > 21:
                standard_result = True
                self.log(f"{player.name} wins ${fmt(player.bets['standard'])}. Dealer busts.")
            elif player_score > dealer_score:
                standard_result = True
                self.log(f"{player.name} wins ${fmt(player.bets['standard'])} with {player_score} against dealer {dealer_score}.")
            elif player_score < dealer_score:
                standard_result = False
                self.log(f"{player.name} loses ${fmt(player.bets['standard'])} with {player_score} against dealer {dealer_score}.")
            else:
                standard_result = False
                self.log(f"{player.name} pushes with dealer on {player_score}. Standard bet returned.")
                player.bets["standard"] = 0.0

            if "'s right hand" in player.name:
                left_player = self.players[self.players.index(player) - 1]
                split_bet = player.bets["standard"]
                left_player.bets["split"] = split_bet
                self.resolve_bets_no_prompt(left_player, {"split": standard_result}, label="split")
            else:
                insurance_result = player.insurance(dealer) if self.side_bets_included["insurance"].get() else False
                self.resolve_bets_no_prompt(
                    player,
                    {"standard": standard_result, "insurance": insurance_result},
                    label="round",
                    tipping_enabled=tipping_enabled
                )

            if "left hand" in player.name:
                player.name = player.name[:-12]

        self.remove_split_right_hands()
        self.round_active = False
        self.status_var.set("Round finished. Click Next round to play again.")
        self.next_round_btn.configure(state="normal")
        self.refresh_all()

    def resolve_bets_no_prompt(self, player, bet_results, label="", tipping_enabled=False):
        """
        UI-safe version of resolve_bet.
        Avoids console input from tipDealer(), because Tkinter should not block on terminal input.
        Matches Player.resolve_bet money logic.
        """
        for bet, won in bet_results.items():
            if bet not in player.bets:
                player.bets[bet] = 0.0

            amount = player.bets[bet]

            if won:
                if amount != 0:
                    player.money += amount
                    self.log(f"{player.name} made ${fmt(amount)} on {bet}. New total: ${fmt(player.money)}.")
                    if tipping_enabled and bet == "standard":
                        self.log("Tipping is enabled in the rules, but the UI skips terminal tip prompts.")
            else:
                player.money -= amount
                if amount != 0:
                    self.log(f"{player.name} lost ${fmt(amount)} on {bet}. New total: ${fmt(player.money)}.")

            player.bets[bet] = 0.0

        if hasattr(player, "checkBankrupt"):
            player.checkBankrupt()

    def remove_split_right_hands(self):
        for i in range(len(self.players) - 1, -1, -1):
            if "right hand" in self.players[i].name:
                del self.players[i]

    def next_round(self):
        for i in range(len(self.players) - 1, -1, -1):
            player = self.players[i]

            if "right hand" in player.name:
                del self.players[i]
                continue

            if player.name != "GERTRUDE" and player.money < 5:
                player.active = False
            else:
                player.active = True

            player.clearHand()

        self.deck.reset()
        self.deck.shuffle()

        self.betting_mode = True
        self.round_active = False
        self.current_player_index = 1

        self.place_bet_btn.configure(state="normal")
        self.hit_btn.configure(state="disabled")
        self.stand_btn.configure(state="disabled")
        self.split_btn.configure(state="disabled")
        self.double_btn.configure(state="disabled")
        self.help_btn.configure(state="disabled")
        self.next_round_btn.configure(state="disabled")

        if not any(player.money >= 5 for player in self.players[1:]):
            self.status_var.set("All players are out of money. Game over.")
            self.log("All players have run out of money. Game over.")
            self.place_bet_btn.configure(state="disabled")
            self.refresh_all()
            return

        self.log("")
        self.log("Prepare bets for the next round.")
        self.status_var.set("Place bets for each active player.")
        self.refresh_all()
        self.show_current_betting_player()

    def show_help(self):
        player = self.current_player()
        if player is None:
            return

        moves = ["hit", "stand"]
        if player.can_split():
            moves.append("split")
        if player.can_double():
            moves.append("double down")
        moves.append("help")

        messagebox.showinfo("Blackjack help", player.help(moves))


def main():
    root = tk.Tk()
    app = BlackjackUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
