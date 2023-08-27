# Sudoku Solver and Game

![Sudoku](https://jump.dev/JuMP.jl/stable/assets/partial_sudoku.png)

A Python program that solves Sudoku puzzles and allows users to play Sudoku games with different difficulty levels.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [Sudoku Solver](#sudoku-solver)
- [Sudoku Game](#sudoku-game)
- [Contributing](#contributing)
- [License](#license)

## Features

- Solves Sudoku puzzles using backtracking algorithm.
- Generates Sudoku puzzles with varying levels of difficulty: easy, medium, and hard.
- Allows users to play Sudoku games interactively.
- Validates user input for Sudoku game moves.
- Provides an option to reveal the complete solution for a Sudoku puzzle.

## How to Use

1. Run the `sudoku.py` script to start the program.
2. Choose the desired mode: Sudoku solver or Sudoku game.
3. Follow the prompts to enter Sudoku game moves or generate a puzzle solution.

## Sudoku Solver

The Sudoku solver employs a backtracking algorithm to find a solution for a given puzzle. It can handle empty cells (denoted by 0) and validates the correctness of the puzzle.

## Sudoku Game

1. Choose a difficulty level: easy, medium, or hard.
2. Play the Sudoku game interactively by entering row, column, and number for your moves.
3. To reveal the solution, type 'solve' during your turn.
4. The game will end when you either solve the puzzle correctly or choose to reveal the solution.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request.

1. Fork the repository.
2. Create your feature/bugfix branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License