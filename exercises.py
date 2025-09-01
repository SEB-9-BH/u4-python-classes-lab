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
        """)
    
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")
    
    def render(self):
        self.print_board()
        self.print_message()
    
    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            
            if move not in self.board:
                print("Invalid move format! Please try again.")
                continue
            
            if self.board[move] is not None:
                print("That position is already taken! Please try again.")
                continue
            
            self.board[move] = self.turn
            break
    
    def check_for_winner(self):
        lines = [['a1','b1','c1'], ['a2','b2','c2'], ['a3','b3','c3'],  # row 
                 ['a1','a2','a3'], ['b1','b2','b3'], ['c1','c2','c3'],  # colm
                 ['a1','b2','c3'], ['a3','b2','c1']                     # diag
                 ]
        
        for line in lines:
            if self.board[line[0]] and self.board[line[0]] == self.board[line[1]] == self.board[line[2]]:
                self.winner = self.board[line[0]]
    
    def check_for_tie(self):
        if not self.winner and all(value is not None for value in self.board.values()):
            self.tie = True
    
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
    
    def play_game(self):
        print("Let's play fast Tic-Tac-Toe round!")
        
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        
        self.render()

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()