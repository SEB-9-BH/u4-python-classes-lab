
class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """.rstrip())

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game! 🎉")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input('Enter a valid move (example: A1): ').strip().lower()
            if move in self.board:
                if self.board[move] is None:
                    self.board[move] = self.turn
                    return
                else:
                    print("That cell is already taken. Try again.")
            else:
                print("Invalid input format. Use something like A1, B3, or c2.")

    def check_for_winner(self):
        lines = [
            ('a1', 'b1', 'c1'), ('a2', 'b2', 'c2'), ('a3', 'b3', 'c3'),
            ('a1', 'a2', 'a3'), ('b1', 'b2', 'b3'), ('c1', 'c2', 'c3'),
            ('a1', 'b2', 'c3'), ('c1', 'b2', 'a3'),
        ]
        for x, y, z in lines:
            v1, v2, v3 = self.board[x], self.board[y], self.board[z]
            if v1 and v1 == v2 == v3:
                self.winner = v1
                return True
        return False

    def check_for_tie(self):
        if not self.winner and all(v is not None for v in self.board.values()):
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Welcome to Tic-Tac-Toe! Let’s play")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            if self.check_for_winner():
                break
            if self.check_for_tie():
                break
            self.switch_turn()
        self.render()

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
