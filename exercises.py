class Game:
    def __init__(self):
        # instance attributes like in your Dog class
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }

    # method to print the board (like __str__ in Dog)
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

    # method to print current message
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    # method to get a valid move from the player
    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move! Try again.")

    # method to check all winning combinations
    def check_for_winner(self):
        if self.board['a1'] and self.board['a1'] == self.board['b1'] == self.board['c1']:
            self.winner = self.turn
        elif self.board['a2'] and self.board['a2'] == self.board['b2'] == self.board['c2']:
            self.winner = self.turn
        elif self.board['a3'] and self.board['a3'] == self.board['b3'] == self.board['c3']:
            self.winner = self.turn
        elif self.board['a1'] and self.board['a1'] == self.board['a2'] == self.board['a3']:
            self.winner = self.turn
        elif self.board['b1'] and self.board['b1'] == self.board['b2'] == self.board['b3']:
            self.winner = self.turn
        elif self.board['c1'] and self.board['c1'] == self.board['c2'] == self.board['c3']:
            self.winner = self.turn
        elif self.board['a1'] and self.board['a1'] == self.board['b2'] == self.board['c3']:
            self.winner = self.turn
        elif self.board['c1'] and self.board['c1'] == self.board['b2'] == self.board['a3']:
            self.winner = self.turn

    # method to check for tie
    def check_for_tie(self):
        all_filled = True
        for key in self.board:
            if self.board[key] is None:
                all_filled = False
        if all_filled and not self.winner:
            self.tie = True

    # method to switch turns
    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    # main gameplay loop
    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        # final board and message
        self.print_board()
        self.print_message()


# run the game
game_instance = Game()
game_instance.play_game()
