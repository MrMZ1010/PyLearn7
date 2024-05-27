##### MohammadAli Mirzaei #####

import arcade  # Import the arcade module for game development

# Define the Block class, inheriting from arcade.Sprite
class Block(arcade.Sprite):
    def __init__(self, center_x, center_y, color):
        super().__init__()  # Call the parent class constructor
        self.width = 50  # Set the width of the block
        self.height = 20  # Set the height of the block
        self.center_x = center_x  # Set the initial horizontal position of the block
        self.center_y = center_y  # Set the initial vertical position of the block
        self.color = color  # Set the color of the block

    # Define the method to draw the block
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)  # Draw the block as a filled rectangle
