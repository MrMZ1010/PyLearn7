##### MohammadAli Mirzaei #####

import random  # Import the random module to use its functions for randomness
import arcade  # Import the arcade module for game development

# Define the Ball class, inheriting from arcade.Sprite
class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()  # Call the parent class constructor
        self.width = 10  # Set the width of the ball
        self.height = 10  # Set the height of the ball
        self.center_x = game.width // 2  # Set the ball's initial horizontal position to the middle of the game window
        self.center_y = 300  # Set the ball's initial vertical position
        self.change_x = random.choice([1, -1])  # Randomly choose the horizontal direction of the ball's movement
        self.change_y = -1  # Set the initial vertical direction of the ball's movement
        self.radius = 12  # Set the radius of the ball
        self.speed = 5  # Set the speed of the ball
        self.color = arcade.color.YELLOW  # Set the color of the ball to yellow

    # Define the method to draw the ball
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)  # Draw the ball as a filled circle

    # Define the method to move the ball
    def move(self):
        self.center_x += self.change_x * self.speed  # Update the ball's horizontal position based on its speed and direction
        self.center_y += self.change_y * self.speed  # Update the ball's vertical position based on its speed and direction
