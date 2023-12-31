# Minesweeper Game - wip

This is a Python implementation of the classic Minesweeper game, which you can play in the terminal. The game features various difficulty levels, including Beginner, Intermediate, Expert, and a Test mode for experimentation. The code is organized into a `board` class that manages the game's mechanics and interactions.

## Table of Contents

- [Getting Started](#getting-started)
- [Game Features](#game-features)
- [Class Methods](#class-methods)
- [How to Play](#how-to-play)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

1. Clone this repository or copy the code provided into your Python environment.
2. Run the Python script `minesweeper.py`.
3. Select a difficulty level (Beginner, Intermediate, Expert, or Test) to start the game.

## Game Features

- The Minesweeper game is played in the terminal.
- Different difficulty levels offer varying grid sizes and mine counts.
- You can dig cells, place flags on potential mines, and perform chord actions (simultaneously clicking both mouse buttons on a revealed cell).
- The goal is to uncover all safe cells without hitting a mine.
- When you dig a numbered cell, it reveals the count of neighboring mines.
- Chording a numbered cell automatically uncovers the remaining unrevealed cells if the number of flagged cells around it matches the number.

## Class Methods

- `make_new_board()`: Initializes the game board and plants mines in random locations.
- `assign_value_to_board()`: Calculates and assigns the values (number of neighboring mines) to each cell.
- `print_game()`: Displays the current state of the covered board.
- `dig(row, col)`: Uncovers a cell, potentially revealing mines and numbers.
- `place_flag(row, col)`: Places a flag on a cell to mark it as a potential mine.
- `reveal(row, col)`: Reveals cells when chording a numbered cell.

## How to Play

1. Choose a difficulty level at the beginning of the game (Beginner, Intermediate, Expert, or Test).
2. To uncover a cell, enter its row and column coordinates, e.g., `1 2`.
3. To place a flag on a cell, add 'f' at the end of the input, e.g., `1 2 f`.
4. To chord a numbered cell, add 'r' at the end of the input, e.g., `1 2 r`. This will reveal all non-flagged cells around the numbered cell if the flag count matches the number.
5. If you need a reminder of the rules, you can type `rule` during your turn.

## Contributing

Contributions to this Minesweeper implementation are welcome. You can contribute by adding new features, improving code quality, enhancing the user interface, or fixing bugs. To contribute, create a pull request with your changes.

## License

This project is licensed under the MIT License.

Enjoy the nostalgia of playing Minesweeper and test your logic skills as you uncover cells while avoiding hidden mines!