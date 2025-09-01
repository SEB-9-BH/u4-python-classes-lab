class Game:
    """A class representing a Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize the game state."""
        self.turn = 'X'  # Current player's turn ('X' or 'O')
        self.tie = False  # Boolean indicating if the game ended in a tie
        self.winner = None  # Store the game winner (None, 'X', or 'O')
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        """Main game loop that controls the flow of the game."""
        print("*** Welcome to Tic-Tac-Toe! ***")
        print("Players will take turns. Enter moves like 'a1', 'b2', 'c3', etc.")
        print()

        # Continue playing until there's a winner or tie
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()

        # Render final game state
        self.render()

    def print_board(self):
        """Print the current state of the game board."""
        b = self.board
        print(f"""
    A   B   C
1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
    ---------
2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
    ---------
3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
""")

    def print_message(self):
        """Print messages about the current game status."""
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        """Render the current game state (board and messages)."""
        self.print_board()
        self.print_message()

    def get_move(self):
        """Handle player input and validate moves."""
        while True:
            # Prompt user for input
            move = input("Enter a valid move (example: A1): ").lower()

            # Validate input
            if self.is_valid_move(move):
                # Update the board and break the loop
                self.board[move] = self.turn
                break
            else:
                print("Invalid move! Please try again.")

    def is_valid_move(self, move):
        """Check if a move is valid."""
        # Check if move corresponds to a key on the board
        if move not in self.board:
            return False

        # Check if the specified board space is currently unoccupied
        if self.board[move] is not None:
            return False

        return True

    def check_for_winner(self):
        """Check if there's a winner by examining all possible winning combinations."""
        board = self.board

        # Check rows
        if board['a1'] and board['a1'] == board['b1'] == board['c1']:
            self.winner = board['a1']
        elif board['a2'] and board['a2'] == board['b2'] == board['c2']:
            self.winner = board['a2']
        elif board['a3'] and board['a3'] == board['b3'] == board['c3']:
            self.winner = board['a3']

        # Check columns
        elif board['a1'] and board['a1'] == board['a2'] == board['a3']:
            self.winner = board['a1']
        elif board['b1'] and board['b1'] == board['b2'] == board['b3']:
            self.winner = board['b1']
        elif board['c1'] and board['c1'] == board['c2'] == board['c3']:
            self.winner = board['c1']

        # Check diagonals
        elif board['a1'] and board['a1'] == board['b2'] == board['c3']:
            self.winner = board['a1']
        elif board['c1'] and board['c1'] == board['b2'] == board['a3']:
            self.winner = board['c1']

    def check_for_tie(self):
        """Check if the game ended in a tie."""
        # The board is entire: All spaces are filled, with no positions marked as None
        board_full = all(value is not None for value in self.board.values())

        # No winner has been declared
        no_winner = self.winner is None

        # If both conditions are met, set the tie attribute to True
        if board_full and no_winner:
            self.tie = True

    def switch_turn(self):
        """Switch the current player's turn."""
        # Using a simple conditional to alternate between 'X' and 'O'
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'


# Create and run the game
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()