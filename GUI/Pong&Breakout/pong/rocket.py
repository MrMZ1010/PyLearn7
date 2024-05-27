##### MohammadAli Mirzaei #####

import arcade  # Import the arcade module for graphics and game development

class Rocket(arcade.Sprite):  # Define a class named Rocket that inherits from arcade.Sprite
    def __init__(self, width, height, color, name):  # Initialize the Rocket class
        super().__init__()  # Call the parent class's constructor
        self.center_x = width  # Set the initial x position of the rocket
        self.center_y = height  # Set the initial y position of the rocket
        self.change_x = 0  # Initialize the change in x position of the rocket
        self.change_y = 0  # Initialize the change in y position of the rocket
        self.speed = 4  # Set the speed of the rocket
        self.color = color  # Set the color of the rocket
        self.width = 10  # Set the width of the rocket
        self.height = 60  # Set the height of the rocket
        self.name = name  # Set the name of the rocket
        self.score = 0  # Initialize the score of the rocket

    def move(self, ball, game):  # Define a method to move the rocket
        if self.center_y > game.height - self.height:  # If the rocket is at the top boundary
            self.center_y = game.height - self.height  # Keep the rocket within the top boundary

        if self.center_y < 60:  # If the rocket is at the bottom boundary
            self.center_y = 60  # Keep the rocket within the bottom boundary

        if self.center_y > ball.center_y:  # If the rocket is below the ball
            self.change_y = -1  # Set the change in y direction to move up

        if self.center_y < ball.center_y:  # If the rocket is above the ball
            self.change_y = 1  # Set the change in y direction to move down

        self.center_y += self.change_y * self.speed  # Update the y position of the rocket based on direction and speed

    def draw(self):  # Define a method to draw the rocket
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)  # Draw the rocket as a filled rectangle
