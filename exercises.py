class Game:
    def __init__(self):
        # Initial state
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    # render the board
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

    # render messages
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    # Combined render function
    def render(self):
        self.print_board()
        self.print_message()

    # Handle player input
    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move! Please try again...")

    # Check for winner
    def check_for_winner(self):
        b = self.board
        wins = [
            ['a1','b1','c1'], ['a2','b2','c2'], ['a3','b3','c3'], 
            ['a1','a2','a3'], ['b1','b2','b3'], ['c1','c2','c3'], 
            ['a1','b2','c3'], ['a3','b2','c1']                    
        ]
        for combo in wins:
            if b[combo[0]] and (b[combo[0]] == b[combo[1]] == b[combo[2]]):
                self.winner = b[combo[0]]

    # Check tie
    def check_for_tie(self):
        if all(v is not None for v in self.board.values()) and not self.winner:
            self.tie = True

    # Switch turns
    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    #  Manage gameplay
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        # last render that show end state
        self.render()


# start the game
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()