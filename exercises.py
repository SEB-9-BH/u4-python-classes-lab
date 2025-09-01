class Game:
    def __init__(self):
        self.reset_game()
        self.stats = {'X': 0, 'O': 0, 'Ties': 0}
    
    def reset_game(self):
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
    
    def print_stats(self):
        print("Current Statistics:")
        print(f"X Wins: {self.stats['X']}")
        print(f"O Wins: {self.stats['O']}")
        print(f"Ties: {self.stats['Ties']}")
        print()
    
    def render(self):
        self.print_board()
        self.print_message()
    
    def get_move(self):
        valid_moves = [key for key, value in self.board.items() if value is None]
        
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            
            if move in valid_moves:
                return move
            elif move in self.board:
                print("That space is already taken! Try again.")
            else:
                print("Invalid move! Please enter a letter (A-C) followed by a number (1-3).")
    
    def check_for_winner(self):
        b = self.board
        
        # Check rows
        for i in range(1, 4):
            if (b[f'a{i}'] == self.turn and 
                b[f'b{i}'] == self.turn and 
                b[f'c{i}'] == self.turn):
                self.winner = self.turn
                return
        
        # Check columns
        for col in ['a', 'b', 'c']:
            if (b[f'{col}1'] == self.turn and 
                b[f'{col}2'] == self.turn and 
                b[f'{col}3'] == self.turn):
                self.winner = self.turn
                return
        
        # Check diagonals
        if (b['a1'] == self.turn and b['b2'] == self.turn and b['c3'] == self.turn):
            self.winner = self.turn
            return
        
        if (b['a3'] == self.turn and b['b2'] == self.turn and b['c1'] == self.turn):
            self.winner = self.turn
            return
    
    def check_for_tie(self):
        if not any(value is None for value in self.board.values()) and not self.winner:
            self.tie = True
    
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
    
    def update_stats(self):
        if self.winner:
            self.stats[self.winner] += 1
        elif self.tie:
            self.stats['Ties'] += 1
    
    def ask_play_again(self):
        while True:
            response = input("Would you like to play again? (y/n): ").lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'.")
    
    def play_game(self):
        #Main game loop
        print("Welcome to Tic-Tac-Toe!")
        print("Players will take turns placing X's and O's on the board.")
        print("The first player to get three in a row wins!")
        
        play_again = True
        
        while play_again:
            self.reset_game()
            
            while not self.winner and not self.tie:
                self.render()
                move = self.get_move()
                self.board[move] = self.turn
                self.check_for_winner()
                self.check_for_tie()
                self.switch_turn()
            
            # Final render to show the end state
            self.render()
            
            # Update and display statistics
            self.update_stats()
            self.print_stats()
            
            # Ask if the player wants to play again
            play_again = self.ask_play_again()
        
        print("Thanks for playing!")


# Create and start the game
if __name__ == "__main__":
    game = Game()
    game.play_game()
