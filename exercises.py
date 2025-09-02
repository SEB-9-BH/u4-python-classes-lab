
class Game:
    def __init__(self):
        self.turn = 'X'  # Start with player X
        self.tie = False  # Tie is false initially
        self.winner = None  # No winner initially
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    # function for the board
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

    # function for the win condition
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    # calls the board and win message
    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                return move
            print("Invalid move. Please try again.")

    # function to check for the winner
    def check_for_winner(self):
        b = self.board
        winning_combinations = [
            # Rows
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),
            # Columns
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),
            # Diagonals
            ('a1', 'b2', 'c3'),
            ('a3', 'b2', 'c1'),
        ]

        for combo in winning_combinations:
            if b[combo[0]] and b[combo[0]] == b[combo[1]] == b[combo[2]]:
                self.winner = b[combo[0]]
                return True
        return False

    # function to check for tie
    def check_for_tie(self):
        if all(self.board[pos] is not None for pos in self.board):
            self.tie = True
            return True
        return False
    
    # function to switch turns
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    # function to start the game
    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn
            if self.check_for_winner():
                self.render()
                break
            if self.check_for_tie():
                self.render()
                break
            self.switch_turn()

# Instantiate and play the game
game_instance = Game()
game_instance.play_game()
