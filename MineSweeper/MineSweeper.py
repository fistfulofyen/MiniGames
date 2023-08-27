import random

class board():
    def __init__(self,dim_size, num_bomb) -> None:
        self.dim_size = dim_size
        self.num_bomb = num_bomb
        # true: covered false: dugged/bomb
        self.status_board = [[ False for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        self.board = self.make_new_board()
        self.assign_value_to_board()
        self.covered_board = [['@' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        self.status = 'alive'
        #duged location
        self.dug = set()
    
    #make board and plant bombs
    def make_new_board(self):
        
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bomb_planted = 0
        while bomb_planted < self.num_bomb:
            #find a location on the board, *square board
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] != '*':
                board[row][col] = '*'
                self.status_board[row][col] = True
                bomb_planted += 1

        return board

    def assign_value_to_board(self):
        rows = len(self.board)
        cols = len(self.board[0])
        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == None:
                    count = 0
                    for dx, dy in directions:
                        new_row, new_col = row + dx, col + dy
                        if is_valid(new_row, new_col) and self.board[new_row][new_col] == '*':
                            count += 1
                    self.board[row][col] = count

    def __str__(self) -> str:
        
        for row in self.board:
            for element in row:
                print(element, end=" ")
            print()

    def print_game(self):
        for row in self.covered_board:
            for element in row:
                print(element, end=" ")
            print()


    # def dig(self,row,col):
    #     #case 3: if number in cell is 0, keep digging surrounding area
    #     #do the same with above ...
    #     rows = len(self.board)
    #     cols = len(self.board[0])
    #     directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

    #     def is_valid(x, y):
    #         return 0 <= x < rows and 0 <= y < cols
        
    #     self.covered_board[row][col] = self.board[row][col]

    #     if self.board[row][col] == 0:
    #         for dx, dy in directions:
    #             new_row, new_col = row + dx, col + dy
    #             if is_valid(new_row, new_col) and (new_row, new_col) not in self.dug:
    #                 self.dig(new_row, new_col)  # Recursive call to dig the surrounding cell
    #     elif self.board[row][col] == '*':
    #         self.status = 'dead'

    #     self.dug.add((row, col))  # Remember that we dug this cell to avoid duplicate digs

    def dig(self, row, col):
        rows = len(self.board)
        cols = len(self.board[0])
        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        if not is_valid(row, col) or (row, col) in self.dug:
            return

        if self.covered_board[row][col] == 'f':
            return
        
        self.dug.add((row, col))
        self.covered_board[row][col] = self.board[row][col]
        self.status_board[row][col] = True

        if self.board[row][col] == 0:
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                self.dig(new_row, new_col)  # Recursive call to dig the surrounding cell
        elif self.board[row][col] == '*':
                self.status = 'dead'
                print('you are dead')
                self.__str__()

    def place_flag(self,row,col):
        self.covered_board[row][col] = 'f'

    #aka pressing both mouse button at once
    def reveal(self,row,col):
        rows = len(self.board)
        cols = len(self.board[0])
        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        #dont work when cell is not already dug
        if self.board[row][col] == 0 or self.covered_board[row][col] == 'f':
            print('invalid move')
            return
        #dont work when number of flag surrending the selected cell dont match with cell number
        count = 0
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if is_valid(new_row, new_col) and self.covered_board[new_row][new_col] == 'f':
                count += 1
        if count < self.board[row][col]:
            print('invalid move')
            return
        #dig surrending cell
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            self.dig(new_row, new_col)


def play(difficulty='Beginner'):
    if difficulty == 'Beginner':
        dim_size = 10
        num_bombs = 10
    elif difficulty == 'Intermediate':
        dim_size = 20
        num_bombs = 50
    elif difficulty == 'Expert':
        dim_size = 30
        num_bombs = 150
    elif difficulty == 'Test':
        dim_size = 3
        num_bombs = 1


    game = board(dim_size,num_bombs)
    game.__str__()
    print('------------------')
    while game.status == 'alive':
        game.print_game()
        user_input = input('enter move: ').split()
        if user_input == ['rule']:
            print(
                '''
                To choose cell to dig, enter row and column value saparated by space.
                eg. 1 2
                to place flag, add 'f' at the end of cell value
                eg. 1 2 f
                to simultaneously on a revealed cell or 'chord', add r at the end of cell value
                eg. 1 2 r
                '''

            )
            continue
        
        row, col = user_input[0], user_input[1]

        if len(user_input) == 3:
            if user_input[2] == 'f':
                game.place_flag(int(row),int(col))
                continue
            elif user_input[2] == 'r':
                game.reveal(int(row),int(col))
        game.dig(int(row),int(col))
        if all(cell == True for row in game.status_board for cell in row):
            print('You Win')
            game.__str__()
            break    




if __name__ == '__main__':
    play('Test')


