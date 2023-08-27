# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The game is played on a 3x3 grid, and players take turns to place their marks ('x' or 'o') on the board. The first player to get three of their marks in a row, column, or diagonal wins the game. If the board is filled without any winner, the game ends in a tie.

## Table of Contents

- [Introduction](#tic-tac-toe-game)
- [How to Play](#how-to-play)
  - [Board Representation](#board-representation)
  - [Player Types](#player-types)
  - [How SmartComputerPlayer Works](#how-smartcomputerplayer-works)
- [Getting Started](#getting-started)
- [Instructions](#instructions)
- [Example](#example)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## How to Play

To play the game, run the `ttt_game.py` script. The game allows a human player to play against a smart computer player that uses the minimax algorithm to make optimal moves. Edit main to change player type, in addition you can make computer player to compete againest each other.

### Board Representation

The board is represented as follows:

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

Each cell is numbered from 0 to 8, and players will choose a number to place their mark on the board.

### Player Types

There are three types of players:

1. `humanPlayer`: A human player who can interactively input their moves during the game.
2. `computerPlayer`: A computer player that makes random moves.
3. `SmartComputerPlayer`: A smart computer player that uses the minimax algorithm to make optimal moves and play strategically.

### How SmartComputerPlayer Works

The `SmartComputerPlayer` class uses the minimax algorithm to determine the best move it should make in a given state of the game. It evaluates all possible moves and selects the one that maximizes its chances of winning or forces a tie if the opponent plays optimally. This allows the smart computer player to be a challenging opponent.

## Getting Started

To run the game, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine:
   ```
   git clone https://github.com/your-username/tic-tac-toe.git
   ```
3. Navigate to the project directory:
   ```
   cd tic-tac-toe
   ```
4. Run the `ttt_game.py` script to start the game:
   ```
   python ttt_game.py
   ```

## Instructions

1. When prompted, input the position number where you want to place your mark ('x') on the board.
2. The computer player ('o') will automatically make its move using the minimax algorithm.
3. Continue taking turns with the computer player until the game ends in a win or tie.

## Example

```
-------------
| x | o | x |
-------------
|   | o |   |
-------------
| o | x |   |
-------------
o makes a move to 3

-------------
| x | o | x |
-------------
| x | o |   |
-------------
| o | x |   |
-------------
x makes a move to 5

-------------
| x | o | x |
-------------
| x | o |   |
-------------
| o | x | o |
-------------
o makes a move to 6

-------------
| x | o | x |
-------------
| x | o |   |
-------------
| o | x | o |
-------------
x makes a move to 8

x wins!
```

## Dependencies

This project has no external dependencies.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the game, feel free to open a pull request.

## License

MIT
