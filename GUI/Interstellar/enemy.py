##### MohammadAli Mirzaei #####

import random  # Import the random module for generating random numbers
import arcade  # Import the arcade module for creating games

class Enemy(arcade.Sprite):  # Define a new class 'Enemy' that inherits from 'arcade.Sprite'
    def __init__(self, game):  # Define the initializer (constructor) for the 'Enemy' class
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")  # Call the parent class (arcade.Sprite) initializer with the sprite image path
        
        # Set the initial horizontal position to a random value within the game window width
        self.center_x = random.randint(0, game.width)
        
        # Set the initial vertical position just above the top of the game window
        self.center_y = game.height + 24
        
        # Set the width of the enemy sprite
        self.width = 48
        
        # Set the height of the enemy sprite
        self.height = 48
        
        # Set the angle of the sprite to make it face downwards
        self.angle = 180
        
        # Set the speed at which the enemy sprite moves
        self.speed = 6
