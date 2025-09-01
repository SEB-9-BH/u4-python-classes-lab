class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
                        'a1': None, 'b1': None, 'c1': None,
                        'a2': None, 'b2': None, 'c2': None,
                        'a3': None, 'b3': None, 'c3': None,
                        }
        self.records = {"X": 0, "O": 0, "ties": 0}
    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.render()

        if self.winner:
            self.records[self.winner] += 1
        elif self.tie:
            self.records["ties"] += 1
        self.show_records()
        choice = input("Play again? (y/n): ").lower()
        if choice == "y":
            self.reset_game()
            self.play_game()  
        else:
            print(" Thanks for playing!")

            
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
        ## If there is a tie: print("Tie game!")
        if self.tie == True:
            print("Tie game!")
        ## If there is a winner: print(f"{self.winner} wins the game!")
        elif self.winner != None:
            print(f"{self.winner} wins the game!")
        ## Otherwise: print(f"It's player {self.turn}'s turn!")
        else:
            print(f"It's player {self.turn}'s turn!")
    def render(self):
    # Call upon print_board
        self.print_board()
    ## Call upon print_message
        self.print_message()
    def get_move(self):
          while True:
    # prompt user for input
            move = input(f"Enter a valid move (example: A1): ").lower()
    # If the input is valid, update the board and break the loop
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
    # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
            else:
                print("Invalid move. Please try again.")
    def check_for_winner(self):
        b = self.board
        winning_combinations = [
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']                       
        ]
        for combination in winning_combinations:
            if b[combination[0]] == b[combination[1]] == b[combination[2]] and b[combination[0]] is not None:
                self.winner = b[combination[0]]
                return
    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and self.winner is None:
            self.tie = True
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
    def reset_game(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    def show_records(self):
        print(f"Scoreboard - X: {self.records['X']} | O: {self.records['O']} | Ties: {self.records['ties']}")


        

        
game_instance = Game()
game_instance.play_game()
