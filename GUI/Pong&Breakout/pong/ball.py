##### MohammadAli Mirzaei #####

import random  # Import the random module to generate random numbers
import arcade  # Import the arcade module for graphics and game development

class Ball(arcade.Sprite):  # Define a class named Ball that inherits from arcade.Sprite

    def __init__(self, game):  # Initialize the Ball class with a game parameter
        super().__init__()  # Call the parent class's constructor
        self.width = 5  # Set the width of the ball
        self.height = 5  # Set the height of the ball
        self.center_x = game.width // 2  # Set the initial x position to the center of the game width
        self.center_y = game.height // 2  # Set the initial y position to the center of the game height
        self.change_x = random.choice([1, -1])  # Randomly choose an initial x direction (1 for right, -1 for left)
        self.change_y = random.choice([1, -1])  # Randomly choose an initial y direction (1 for up, -1 for down)
        self.radius = 15  # Set the radius of the ball
        self.color = arcade.color.WHITE  # Set the color of the ball to white
        self.speed = 5  # Set the speed of the ball

    def move(self):  # Define a method to move the ball
        self.center_x += self.change_x * self.speed  # Update the x position based on direction and speed
        self.center_y += self.change_y * self.speed  # Update the y position based on direction and speed

    def draw(self):  # Define a method to draw the ball
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)  # Draw the ball as a filled circle
