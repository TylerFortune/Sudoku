# Sudoku

## A Command-Line Sudoku Game in Python

This project is a Python-programmed simulation of the classic game Sudoku, designed to be played directly in your terminal. It offers an interactive experience where you can load existing puzzles, make your moves, and potentially save your game progress.

### Features

* **Interactive Gameplay:** Play Sudoku puzzles right in your command line interface.
* **Load Puzzles:** Easily load different Sudoku puzzles from external text files (e.g., `sudoku1.txt`) to start new games.
* **Save & Load Game State:** The game is set up to allow you to save your current progress and load a previously saved game, letting you pick up exactly where you left off.
* **Basic Game Mechanics:** Enter numbers into the grid, with the underlying logic handling rule validation and board updates.

### File Structure

* `sudoku.py`: This is the core Python script that runs the game. It contains all the logic for displaying the board, handling user input, enforcing Sudoku rules, and managing game states.
* `sudoku1.txt`: An example text file that holds a pre-defined Sudoku puzzle. You can modify this or create new `.txt` files to include different puzzles.
* `sudoku_save.txt`: This file is intended for storing and retrieving your saved game progress, allowing you to pause and resume games.

### How to Get Started

To run the Sudoku game on your local machine, follow these simple steps:

1.  **Clone the repository:** Open your terminal or command prompt and run:
    ```bash
    git clone [https://github.com/TylerFortune/Sudoku.git](https://github.com/TylerFortune/Sudoku.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Sudoku
    ```
3.  **Run the game:** Make sure you have Python (version 3.x is recommended) installed, then execute the main script:
    ```bash
    python sudoku.py
    ```
    The game will launch in your terminal, and you can follow the on-screen prompts to play.

---
