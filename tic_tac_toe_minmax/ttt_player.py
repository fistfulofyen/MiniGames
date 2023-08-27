'''
   0 | 1 | 2
   ---------
   3 | 4 | 5
   ---------
   6 | 7 | 8

Horizontal Rows:
   Winning combinations: 
   - (0, 1, 2)
   - (3, 4, 5)
   - (6, 7, 8)

   Vertical Columns:
   Winning combinations: 
   - (0, 3, 6)
   - (1, 4, 7)
   - (2, 5, 8)
Diagonals:
   Winning combinations: 
   - (0, 4, 8)
   - (2, 4, 6)
'''
import math
import random

class player():
   def __init__(self,letter):
      self.letter = letter
   
   def get_move(self,game):
      pass

class computerPlayer(player):
   def __init__(self,letter):
      super().__init__(letter)

   def get_move(self,game):
      #find a valid loc for the next move
      square = random.choice(game.available_moves())
      return square


class humanPlayer(player):
   def __init__(self,letter):
      super().__init__(letter)

   def get_move(self,game):
      #keep asking user input until a valid squire
      while True:
         print("currently availiable square ", game.available_moves())
         square = input(self.letter + '\'s turn. Input move (0-8):')
         # if int(square) in game.availiable_move():
         #    return square
         # else:
         #    print("invalid input")

         try:
            val = int(square)
            if val not in game.available_moves():
               raise ValueError
            return val
         except ValueError:
            print("invalid input")
         
class SmartComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'o' if player == 'x' else 'x'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best