from ttt_player import computerPlayer, humanPlayer, SmartComputerPlayer

class tictactoe:
    def __init__(self) -> None:
        self.board = self.make_board()
        self.current_winner = None

    def print_board(self):
        print("-------------")
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + " | ".join(row) + ' |')
            print("-------------")
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    @staticmethod
    def print_board_number():
        print('''
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

                ''')
    
    def available_moves(self):
        return [i for i,loc in enumerate(self.board) if loc == " "]
    
    def empty_squares(self):
        #check this if something go wrong
        return self.board.count(" ")
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter

            #check for winner
            if self.winner(square,letter):
                self.current_winner = letter


            return True
        return False
    
    def winner(self, square, letter):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combination in win_combinations:
            if all(self.board[pos] == letter for pos in combination):
                return True

        return False



def lets_play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_number()
    
    letter = "x"
    while game.empty_squares():
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        print(game.board)
        #make_move return T/F, check condition and print
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('')

            #check winner
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            


            letter = "o" if letter == 'x' else 'x'

    if print_game:
        print("tie")    


if __name__ == '__main__':
    x_player = humanPlayer('x')
    o_player = SmartComputerPlayer('o')
    lets_play(tictactoe(),x_player,o_player,print_game = True)