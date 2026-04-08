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
        self.root.geometry("1450x900")

        self.players = []
        self.current_player_index = 1
        self.game_started = False
        self.betting_mode = False

        self.deck = None
        self.dealer = None
        self.player_panels = []

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

        self.names_frame = ttk.Frame(top)
        self.names_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(8, 0))
        self.name_vars = []

        ttk.Button(top, text="Start game", command=self.start_game).grid(row=2, column=0, columnspan=3, sticky="ew", pady=(8, 0))

        left = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        left.grid(row=1, column=0, sticky="nsew")
        left.columnconfigure(0, weight=1)
        left.rowconfigure(1, weight=1)

        right = ttk.Frame(self.root, padding=(0, 0, 10, 10))
        right.grid(row=1, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(2, weight=1)

        self.status_var = tk.StringVar(value="Set up players, then start the game.")
        ttk.Label(left, textvariable=self.status_var, wraplength=800).grid(row=0, column=0, sticky="ew", pady=(0, 10))

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

        ttk.Label(control_box, text="Bet amount:").grid(row=0, column=0, sticky="w")
        self.bet_var = tk.StringVar(value="5")
        ttk.Entry(control_box, textvariable=self.bet_var).grid(row=0, column=1, sticky="ew", padx=(8, 0))

        self.place_bet_btn = ttk.Button(control_box, text="Place bet", command=self.place_bet)
        self.place_bet_btn.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        self.hit_btn = ttk.Button(control_box, text="Hit", command=self.hit_current, state="disabled")
        self.hit_btn.grid(row=2, column=0, sticky="ew", pady=(8, 0))

        self.stand_btn = ttk.Button(control_box, text="Stand", command=self.stand_current, state="disabled")
        self.stand_btn.grid(row=2, column=1, sticky="ew", padx=(8, 0), pady=(8, 0))

        self.help_btn = ttk.Button(control_box, text="Show help", command=self.show_help, state="disabled")
        self.help_btn.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        self.next_round_btn = ttk.Button(control_box, text="Next round", command=self.next_round, state="disabled")
        self.next_round_btn.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        score_box = ttk.LabelFrame(right, text="Scoreboard", padding=10)
        score_box.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        score_box.columnconfigure(0, weight=1)

        self.score_text = tk.Text(score_box, height=12, wrap="word")
        self.score_text.grid(row=0, column=0, sticky="ew")
        self.score_text.configure(state="disabled")

        log_box = ttk.LabelFrame(right, text="Game log", padding=10)
        log_box.grid(row=2, column=0, sticky="nsew")
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

    def start_game(self):
        names = [v.get().strip() for v in self.name_vars]
        if any(not name for name in names):
            messagebox.showerror("Missing name", "Every player needs a name.")
            return

        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = [Gertrude("GERTRUDE")] + [Player(name) for name in names]

        self.create_player_panels()
        self.game_started = True
        self.betting_mode = True
        self.current_player_index = 1

        self.place_bet_btn.configure(state="normal")
        self.hit_btn.configure(state="disabled")
        self.stand_btn.configure(state="disabled")
        self.help_btn.configure(state="disabled")
        self.next_round_btn.configure(state="disabled")

        self.log("Welcome to Gertrude's BlackJack!")
        self.log(f"Players at the table: {', '.join(names)}")
        self.status_var.set("Game started. Place bets for each player.")
        self.refresh_all()
        self.show_current_betting_player()

    def refresh_scoreboard(self):
        if not self.players:
            self.set_text(self.score_text, "No players yet.")
            return

        lines = []
        for i, player in enumerate(self.players[1:], start=1):
            turn_marker = ""
            if self.game_started and i == self.current_player_index:
                turn_marker = "  <-- current"
            hand_value = player.check_cards() if player.hand else "-"
            lines.append(f"{player.name}: ${player.money} | bet: ${player.bets['standard']} | hand value: {hand_value}{turn_marker}")
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
        for idx, panel in enumerate(self.player_panels, start=1):
            player = self.players[idx]
            panel.configure(style="TLabelframe")

            hand_value = player.check_cards() if player.hand else "-"
            panel.header_var.set(player.name)
            panel.info_var.set(f"Money: ${player.money} | Bet: ${player.bets['standard']} | Hand value: {hand_value}")

            if not player.hand:
                status = "Waiting for round"
            elif self.betting_mode and idx == self.current_player_index:
                status = "Place your bet"
            elif idx == self.current_player_index and player.active:
                status = "Your turn"
            elif player.hand and player.check_cards() > 21:
                status = "Bust"
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

    def show_current_betting_player(self):
        if self.current_player_index >= len(self.players):
            self.begin_round()
            return

        player = self.players[self.current_player_index]
        self.bet_var.set(str(10 if player.money >= 10 else 5))
        self.status_var.set(f"{player.name}: enter a bet and click Place bet.")
        self.refresh_all()

    def place_bet(self):
        if not self.game_started or not self.betting_mode:
            return

        player = self.players[self.current_player_index]

        try:
            bet = int(self.bet_var.get().strip())
        except ValueError:
            messagebox.showerror("Invalid bet", "Please enter a whole number.")
            return

        if bet < 5:
            messagebox.showerror("Invalid bet", "Bet must be at least $5.")
            return

        if player.money - bet < -100:
            messagebox.showerror("Invalid bet", "This player cannot go more than $100 into debt.")
            return

        player.bets["standard"] = bet
        self.log(f"{player.name} bets ${bet}.")
        self.current_player_index += 1

        if self.current_player_index < len(self.players):
            self.show_current_betting_player()
        else:
            self.begin_round()

        self.refresh_all()

    def begin_round(self):
        self.betting_mode = False

        for player in self.players:
            player.active = True
            player.clearHand()

        self.dealer.dealCards(2, self.players)

        self.current_player_index = 1
        self.place_bet_btn.configure(state="disabled")
        self.hit_btn.configure(state="normal")
        self.stand_btn.configure(state="normal")
        self.help_btn.configure(state="normal")
        self.next_round_btn.configure(state="disabled")

        self.log("")
        self.log("--- New round started ---")
        self.log("Initial cards dealt.")
        self.status_var.set(f"{self.players[self.current_player_index].name}'s turn.")
        self.refresh_all()
        self.advance_past_finished_players(initial=True)

    def current_player(self):
        if 1 <= self.current_player_index < len(self.players):
            return self.players[self.current_player_index]
        return None

    def hit_current(self):
        player = self.current_player()
        if player is None:
            return

        card = player.hit(self.dealer)
        value = VALUE_LABELS.get(card.value, str(card.value))
        suit = SUIT_SYMBOLS.get(card.suit, card.suit)
        self.log(f"{player.name} hits and draws {value}{suit}.")

        score = player.check_cards()
        if score > 21:
            self.log(f"{player.name} busts with {score}.")
            self.log(player.trashTalk())
            self.advance_to_next_player()
        else:
            self.status_var.set(f"{player.name}'s turn. Hand value: {score}")

        self.refresh_all()

    def stand_current(self):
        player = self.current_player()
        if player is None:
            return

        player.stand()
        self.log(f"{player.name} stands with {player.check_cards()}.")
        self.advance_to_next_player()
        self.refresh_all()

    def advance_past_finished_players(self, initial=False):
        while True:
            player = self.current_player()
            if player is None:
                self.finish_players_phase()
                return

            score = player.check_cards()
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
        self.help_btn.configure(state="disabled")

        dealer = self.players[0]
        dealer.knownCards = [True for _ in dealer.knownCards]

        self.log("")
        self.log("--- Gertrude's turn ---")
        self.log(f"Gertrude reveals hidden card. Current value: {dealer.check_cards()}")
        final = dealer.gertTurn(self.dealer)
        self.log(f"Gertrude ends with {final}.")
        self.resolve_round()

    def resolve_round(self):
        dealer = self.players[0]
        dealer_score = dealer.check_cards()

        self.log("")
        self.log("--- Results ---")

        for player in self.players[1:]:
            player_score = player.check_cards()

            if player_score > 21:
                won = False
                self.log(f"{player.name} busts and loses ${player.bets['standard']}.")
            elif dealer_score > 21:
                won = True
                self.log(f"{player.name} wins. Dealer busts.")
            elif player_score > dealer_score:
                won = True
                self.log(f"{player.name} wins with {player_score} against dealer {dealer_score}.")
            elif player_score < dealer_score:
                won = False
                self.log(f"{player.name} loses with {player_score} against dealer {dealer_score}.")
            else:
                won = False
                self.log(f"{player.name} pushes with dealer on {player_score}. Current code treats push as no win.")

            player.resolve_bet({"standard": won})

        self.status_var.set("Round finished. Click Next round to play again.")
        self.next_round_btn.configure(state="normal")
        self.refresh_all()

    def next_round(self):
        for player in self.players:
            player.active = True
            player.clearHand()

        self.deck.reset()
        self.deck.shuffle()

        self.betting_mode = True
        self.current_player_index = 1

        self.place_bet_btn.configure(state="normal")
        self.hit_btn.configure(state="disabled")
        self.stand_btn.configure(state="disabled")
        self.help_btn.configure(state="disabled")
        self.next_round_btn.configure(state="disabled")

        self.log("")
        self.log("Prepare bets for the next round.")
        self.status_var.set("Place bets for each player.")
        self.refresh_all()
        self.show_current_betting_player()

    def show_help(self):
        player = self.current_player()
        if player is None:
            return
        messagebox.showinfo("Blackjack help", player.help(["hit", "stand", "help"]))


def main():
    root = tk.Tk()
    app = BlackjackUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
