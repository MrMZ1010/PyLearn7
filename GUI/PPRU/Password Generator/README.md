# Number Puzzle Game

This project implements a simple number puzzle game using PySide6, a Python binding for the Qt framework. The game presents a 4x4 grid of numbers from 1 to 15 arranged randomly, with one empty cell. The player's objective is to arrange the numbers in ascending order by sliding them into the empty cell.

## Features

- Randomized arrangement of numbers on each game start.
- User interface built with PySide6, providing a visually appealing grid layout.
- Interactive gameplay where the player can slide numbers into the empty cell to rearrange them.
- Win detection to notify the player upon successfully arranging the numbers in ascending order.

## File Structure

- `main.py`: Contains the main logic for the game, including the `MainWindow` class and event handling.
- `main_ui.py`: UI file generated by Qt Designer and converted to Python code using `pyside6-uic`.
- `main_ui.ui`: UI file created with Qt Designer, defining the layout and widgets of the main window.
- `README.md`: This file, providing an overview of the project.

## Requirements

- Python 3.x
- PySide6

## Usage

1. Ensure you have Python and PySide6 installed on your system.
2. Run the `main.py` script to start the game.
3. Click on the numbered buttons to slide them into the empty cell.
4. Continue rearranging the numbers until they are in ascending order.
5. Once you have arranged the numbers correctly, a message box will appear, indicating that you have won.

## Contributing

Contributions to improve the game's features, user interface, or code structure are welcome. Please feel free to submit issues or pull requests.


