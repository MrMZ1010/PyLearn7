##### MohammadAli Mirzaei #####

import arcade  # Import the arcade module for game development

# Define the Rocket class, inheriting from arcade.Sprite
class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__()  # Call the parent class constructor
        self.width = 80  # Set the width of the rocket
        self.height = 20  # Set the height of the rocket
        self.center_x = game.width // 2  # Set the initial horizontal position of the rocket to the middle of the game window
        self.center_y = 30  # Set the initial vertical position of the rocket
        self.change_x = 0  # Initialize the horizontal movement to 0
        self.change_y = 0  # Initialize the vertical movement to 0 (not used in this case)
        self.color = arcade.color.RED  # Set the color of the rocket to red
        self.speed = 3  # Set the speed of the rocket
        self.score = 0  # Initialize the score to 0
        self.health = 3  # Initialize the health to 3

    # Define the method to draw the rocket
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)  # Draw the rocket as a filled rectangle

    # Define the method to move the rocket
    def move(self):
        self.center_x += self.change_x * self.speed  # Update the rocket's horizontal position based on its speed and direction

