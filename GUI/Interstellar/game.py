##### MohammadAli Mirzaei #####

import random  # Import the random module for generating random numbers
import arcade  # Import the arcade module for creating games
from spaceship import Spaceship  # Import the Spaceship class from spaceship module
from enemy import Enemy  # Import the Enemy class from enemy module

class Game(arcade.Window):  # Define a new class 'Game' that inherits from 'arcade.Window'
    def __init__(self):  # Define the initializer (constructor) for the 'Game' class
        super().__init__(width=800, height=600, title="Interstellar")  # Initialize the parent class (arcade.Window) with width, height, and title
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")  # Load the background image texture
        self.me = Spaceship(self)  # Create an instance of the Spaceship class and assign it to self.me
        self.doshman = Enemy(self)  # Create an instance of the Enemy class and assign it to self.doshman

    def on_draw(self):  # Define the method to handle drawing the game screen
        arcade.start_render()  # Start the render process
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )  # Draw the background texture to cover the entire window
        self.me.draw()  # Draw the spaceship (self.me) on the screen
        self.doshman.draw()  # Draw the enemy (self.doshman) on the screen
        arcade.finish_render()  # Finish the render process

    def on_key_press(self, symbol: int, modifiers: int):  # Define the method to handle key press events
        if symbol == arcade.key.A:  # Check if the 'A' key was pressed
            self.me.center_x -= self.me.speed  # Move the spaceship left by subtracting its speed from its x-coordinate
        elif symbol == arcade.key.D:  # Check if the 'D' key was pressed
            self.me.center_x += self.me.speed  # Move the spaceship right by adding its speed to its x-coordinate
            
    def on_update(self, delta_time: float):  # Define the method to update the game state
        self.doshman.center_x -= self.doshman.speed  # Move the enemy left by subtracting its speed from its x-coordinate
