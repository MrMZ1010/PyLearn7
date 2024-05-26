##### Mohammad Ali Mirzaei #####

import arcade  # Import the arcade module for creating games

class Spaceship(arcade.Sprite):  # Define a new class 'Spaceship' that inherits from 'arcade.Sprite'
    def __init__(self, game):  # Define the initializer (constructor) for the 'Spaceship' class
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")  # Call the parent class (arcade.Sprite) initializer with the sprite image path
        
        # Set the initial horizontal position to the center of the game window
        self.center_x = game.width // 2
        
        # Set the initial vertical position
        self.center_y = 50
        
        # Set the change in horizontal position (velocity) to 0
        self.change_x = 0
        
        # Set the change in vertical position (velocity) to 0
        self.change_y = 0
        
        # Set the width of the spaceship sprite
        self.width = 48
        
        # Set the height of the spaceship sprite
        self.height = 48
        
        # Set the speed at which the spaceship moves horizontally
        self.speed = 8
        
        # Store the width of the game window for reference
        self.game_with = game.width
        
        # Initialize an empty list to store bullets fired by the spaceship
        self.bullet_list = []






