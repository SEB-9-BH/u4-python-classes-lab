class Game:

    def __init__(self):
        # 'X' always starts
        self.turn = 'X'
        self.tie = False
        self.winner = None
        # Board as a dict keyed by coordinates; None means empty
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        # all winning lines: 3 rows, 3 cols, 2 diagonals
        self.winning_lines = [
            ('a1', 'b1', 'c1'), ('a2', 'b2', 'c2'), ('a3', 'b3', 'c3'),  # rows
            ('a1', 'a2', 'a3'), ('b1', 'b2', 'b3'), ('c1', 'c2', 'c3'),  # cols
            ('a1', 'b2', 'c3'), ('c1', 'b2', 'a3')                       # diagonals
        ]

    # ---------- Rendering ----------
    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)

    def print_message(self):
        """Print game status message: turn, winner, or tie."""
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        """Combined rendering for convenience."""
        self.print_board()
        self.print_message()

    # ---------- Input & Validation ----------
    def _is_valid_key(self, key: str) -> bool:
        """Return True if key is a valid board coordinate like 'a1'..'c3'."""
        return key in self.board

    def get_move(self):
        """
        Prompt the current player for a move until a valid, empty cell is given.
        Accepts input in forms like A1, b2, C3 (case-insensitive).
        """
        while True:
            move = input("Enter a valid move (example: A1): ").strip().lower()
            if not self._is_valid_key(move):
                print("Invalid format. Use A1, B2, C3, etc.")
                continue
            if self.board[move] is not None:
                print("That cell is already taken. Try again.")
                continue
            # Place piece and return
            self.board[move] = self.turn
            return

    # ---------- Game State Checks ----------
    def check_for_winner(self):
        """Set self.winner if the current board has a winning line."""
        for a, b, c in self.winning_lines:
            v1, v2, v3 = self.board[a], self.board[b], self.board[c]
            # all filled and equal
            if v1 and v1 == v2 == v3:
                self.winner = v1
                return

    def check_for_tie(self):
        """Set self.tie True if board full and no winner."""
        if self.winner:
            return
        # Tie if no None values remain
        if all(v is not None for v in self.board.values()):
            self.tie = True

    def switch_turn(self):
        """Alternate player turns between 'X' and 'O'."""
        self.turn = 'O' if self.turn == 'X' else 'X'

    # ---------- Main Loop ----------
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Coordinates are A-C for columns and 1-3 for rows (e.g., B2).")
        # Loop until there is a winner or tie
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            # After a valid move, re-render and evaluate game state
            self.render()
            # Check winner, then tie
            self.check_for_winner()
            self.check_for_tie()
            # Only switch if game not over
            if not self.winner and not self.tie:
                self.switch_turn()
        # Final render and message at end
        self.render()
        print("Thanks for playing!")

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
