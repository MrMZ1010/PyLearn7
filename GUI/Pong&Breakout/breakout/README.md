# Breakout Game

## Overview

This is a classic Breakout game built using Python and the Arcade library. The game features a paddle (rocket), a ball, and multiple blocks. The goal is to destroy all the blocks without letting the ball fall below the screen. The player controls the paddle to keep the ball in play and bounce it towards the blocks.

## Project Structure

The project consists of the following files:

- `main.py`: The main file that initializes and runs the game.
- `ball.py`: Defines the `Ball` class, representing the ball in the game.
- `block.py`: Defines the `Block` class, representing the blocks in the game.
- `rocket.py`: Defines the `Rocket` class, representing the player's paddle.

## Classes and Their Responsibilities

### Ball

The `Ball` class represents the ball in the game.

#### Attributes

- `width`: The width of the ball (not used in drawing).
- `height`: The height of the ball (not used in drawing).
- `center_x`: The x-coordinate of the ball's center.
- `center_y`: The y-coordinate of the ball's center.
- `change_x`: The change in x-coordinate per update (velocity in x direction).
- `change_y`: The change in y-coordinate per update (velocity in y direction).
- `radius`: The radius of the ball.
- `speed`: The speed of the ball.
- `color`: The color of the ball.

#### Methods

- `draw()`: Draws the ball on the screen.
- `move()`: Updates the ball's position based on its velocity.

### Block

The `Block` class represents the blocks that the ball will hit.

#### Attributes

- `width`: The width of the block.
- `height`: The height of the block.
- `center_x`: The x-coordinate of the block's center.
- `center_y`: The y-coordinate of the block's center.
- `color`: The color of the block.

#### Methods

- `draw()`: Draws the block on the screen.

### Rocket

The `Rocket` class represents the player's paddle.

#### Attributes

- `width`: The width of the rocket.
- `height`: The height of the rocket.
- `center_x`: The x-coordinate of the rocket's center.
- `center_y`: The y-coordinate of the rocket's center.
- `change_x`: The change in x-coordinate per update (velocity in x direction).
- `color`: The color of the rocket.
- `speed`: The speed of the rocket.
- `score`: The player's score.
- `health`: The player's health.

#### Methods

- `draw()`: Draws the rocket on the screen.
- `move()`: Updates the rocket's position based on its velocity.

### Game

The `Game` class manages the game state and handles the game loop.

#### Methods

- `__init__()`: Initializes the game window and game elements (player, ball, blocks).
- `on_draw()`: Renders all game elements on the screen.
- `on_update(delta_time)`: Updates the game state (positions of ball and rocket, collision detection).
- `on_key_press(symbol, modifiers)`: Handles key press events for player control.
- `on_mouse_motion(x, y, dx, dy)`: Handles mouse movement for player control.

## How to Run

1. Make sure you have Python and the Arcade library installed. You can install the Arcade library using pip:

    ```bash
    pip install arcade
    ```

2. Clone this repository or download the source code.

3. Run the `main.py` file:

    ```bash
    python main.py
    ```

## Controls

- Use the `A` or `Left Arrow` key to move the paddle left.
- Use the `D` or `Right Arrow` key to move the paddle right.
- You can also control the paddle using the mouse.

## Gameplay

- The ball bounces off the walls and the paddle.
- When the ball hits a block, the block is destroyed, and the player's score increases.
- If the ball falls below the screen, the player's health decreases, and a new ball is spawned.
- The game ends when the player's health reaches zero.

Enjoy playing the Breakout game!
