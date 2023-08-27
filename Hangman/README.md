# Hangman Game

![Hangman](https://t4.ftcdn.net/jpg/05/17/38/33/360_F_517383341_8nWEFfM1KL3K5LNTjUDrne3x0kZiuxuj.jpg)

A classic Hangman game implemented in Python. Players have a limited number of attempts to guess a secret word. For each incorrect guess, a part of a hangman figure is drawn. The game continues until the player guesses the word correctly or runs out of attempts.

## Table of Contents

- [Features](#features)
- [How to Play](#how-to-play)
- [Word List](#word-list)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive command-line interface.
- Randomly selects a word from a predefined word list.
- Tracks the number of incorrect guesses (lives).
- Provides visual feedback in the form of a hangman drawing.
- Informs the player about guessed letters, remaining lives, and the current state of the word.
- Ends the game when the player wins by guessing the word or loses by running out of lives.

## How to Play

1. Run the `hangman.py` script to start the game.
2. The game will generate a random word from the word list.
3. Guess a letter (only one letter at a time) and press Enter.
4. If the guessed letter is incorrect, a part of the hangman figure is drawn, and you lose a life.
5. Continue guessing letters until you guess the entire word or run out of lives.
6. The game will display the current state of the word, guessed letters, remaining lives, and the hangman drawing.
7. If you guess the word correctly, you win; otherwise, you lose.

## Word List

The game selects words from a predefined list, including words like "apple," "banana," "carrot," and more. You can customize the word list by modifying the `word_list` variable in the code.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request.

1. Fork the repository.
2. Create your feature/bugfix branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License
