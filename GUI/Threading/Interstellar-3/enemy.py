##### MohammadAli Mirzaei #####

import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        # Initialize the Enemy sprite with the image of an orange player ship
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        # Set the initial position of the enemy ship randomly within the game width
        self.center_x = random.randint(0, game.width)
        # Set the initial vertical position just above the top of the game window
        self.center_y = game.height + 24
        # Set the width and height of the enemy ship
        self.width = 48
        self.height = 48
        # Set the initial angle of the enemy ship (180 degrees, pointing downwards)
        self.angle = 180
        # Set the speed of the enemy ship
        self.speed = 6

    def move(self):
        # Move the enemy ship vertically downwards by its speed
        self.center_y -= self.speed

    def rise_speed(self):
        # Increase the speed of the enemy ship
        self.speed += 1
