# Snake Game Projects Overview

This repository contains two Snake game projects implemented using the Arcade library in Python. Each project offers a unique gameplay experience and features various game elements.

## Snake Game with AI

### Description
This Snake game features an AI-controlled snake that tries to eat apples spawned randomly on the game screen. The snake's movement is determined by an AI algorithm, and it aims to maximize its score by eating as many apples as possible without colliding with itself or the game boundaries.

### Features
- AI-controlled snake movement
- Collision detection with apples
- Score tracking

### Files
- `snake.py`: Contains the Snake class and its methods for controlling the snake's behavior.
- `foods.py`: Defines classes for different types of food items such as apples.
- `main_ai.py`: Entry point for the game. Initializes the game window and runs the game loop.

## Enhanced Snake Game

### Description
This Snake game offers an enhanced gaming experience with additional features and challenges. In addition to apples, the game introduces new food items such as pears and 'shits.' The player controls the snake using arrow keys or WASD keys, aiming to eat as much food as possible while avoiding collisions with itself, the game boundaries, and 'shits.'

### Features
- Player-controlled snake movement
- Multiple types of food items with different effects
- Collision detection with pears, apples, and 'shits'
- Game over conditions including collisions with boundaries and the snake itself

### Files
- `snake.py`: Contains the Snake class and its methods for controlling the snake's behavior.
- `foods.py`: Defines classes for different types of food items such as apples, pears, and 'shits.'
- `main.py`: Entry point for the game. Initializes the game window and runs the game loop.

## Getting Started
To run any of these Snake game projects, make sure you have Python installed on your system. You'll also need to install the Arcade library. You can install it via pip:

```bash
pip install arcade
```
