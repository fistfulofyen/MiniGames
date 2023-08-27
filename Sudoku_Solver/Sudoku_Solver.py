import random

def is_valid(board, row, col, num):
    # Check if 'num' can be placed in the given row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    # Check within the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty_location(board):
    # Find the next empty cell (cell with 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None  # No empty cells left

def solve_sudoku(board):
    row, col = find_empty_location(board)
    if row is None:  # No empty cell found, puzzle is solved
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):  # Recursively solve with the current placement
                return True

            board[row][col] = 0  # Backtrack if the current placement is incorrect

    return False  # No valid number could be placed, backtrack further

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def generate_sudoku(difficulty):
    # Create a completed Sudoku grid
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)  # Solve the board
    
    # Remove numbers based on difficulty level
    num_to_remove = [40, 35, 30]  # Number of clues for easy, medium, and hard
    for _ in range(81 - num_to_remove[difficulty]):
        while True:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                break
    
    return board


def play_sudoku():

    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = int(input("Enter the number of your choice: ")) - 1
    
    sudoku_board = generate_sudoku(difficulty)

    sample_sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Welcome to Sudoku!")
    print("Enter row, column, and number (e.g., '2 3 4') or 'solve' to see the solution.")
    
    while True:
        print_board(sudoku_board)
        user_input = input("Enter your move: ")
        
        if user_input.lower() == 'solve':
            if solve_sudoku(sudoku_board):
                print("Sudoku solved!")
                print_board(sudoku_board)
            else:
                print("No solution exists.")
            break
        
        try:
            row, col, num = map(int, user_input.split())
            if is_valid(sudoku_board, row-1, col-1, num):
                sudoku_board[row-1][col-1] = num
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row, column, and number.")
 


if __name__ == "__main__":
    play_sudoku()