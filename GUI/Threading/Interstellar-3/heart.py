##### Mohammad Ali Mirzaei #####

import arcade

class Heart(arcade.Sprite):
    def __init__(self, location):
        # Initialize the Heart sprite with the image of a heart
        super().__init__("heart.jpg")
        # Set the initial position of the heart sprite based on its location
        self.center_x = 20 + location * 30
        self.center_y = 20
        # Set the width and height of the heart sprite
        self.width = 30
        self.height = 30