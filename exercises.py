class Game:
    def __init__(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            "a1": None, "b1": None, "c1": None,
            "a2": None, "b2": None, "c2": None,
            "a3": None, "b3": None, "c3": None,
        }

    def play_game(self):
        print("Welcome to the Game!!!")
        while not self.tie and self.winner is None:
            self.render()
            self.get_move()
            self.check_winner()
            self.check_for_tie()
            # Only switch turns if the game hasn't ended
            if not self.tie and self.winner is None:
                self.switch_turn()
        self.render()

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b["a1"] or " "} | {b["b1"] or " "} | {b["c1"] or " "}
                ----------
            2)  {b["a2"] or " "} | {b["b2"] or " "} | {b["c2"] or " "}
                ----------
            3)  {b["a3"] or " "} | {b["b3"] or " "} | {b["c3"] or " "}
            """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner is not None:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: B2): ").lower().strip()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                return
            print("Invalid move. Try again!")

    def check_winner(self):
        b = self.board
        win_combos = [
            ["a1", "a2", "a3"],
            ["b1", "b2", "b3"],
            ["c1", "c2", "c3"],
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"],
            ["a3", "b3", "c3"],
            ["a1", "b2", "c3"],
            ["a3", "b2", "c1"],
        ]
        for combo in win_combos:
            v1, v2, v3 = b[combo[0]], b[combo[1]], b[combo[2]]
            if v1 is not None and v1 == v2 == v3:
                self.winner = v1
                return

    def check_for_tie(self):
        if self.winner is None and all(v is not None for v in self.board.values()):
            self.tie = True

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"


if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
