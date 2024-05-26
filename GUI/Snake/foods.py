##### MohammadAli Mirzaei #####

from random import randint  # Importing randint function from random module
import arcade  # Importing arcade library for creating games

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Apple.png")  # Calling the superclass constructor with the image file path
        self.width = 36  # Setting the width of the sprite
        self.height = 36  # Setting the height of the sprite
        # Setting the initial position of the sprite randomly within the game window
        self.center_x = randint(10, game.width - 10)
        self.center_y = randint(10, game.height - 10)
        self.change_x = 0  # Initializing the horizontal movement speed of the sprite
        self.change_y = 0  # Initializing the vertical movement speed of the sprite

class Pear(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Pear.png")  # Calling the superclass constructor with the image file path
        self.width = 36  # Setting the width of the sprite
        self.height = 36  # Setting the height of the sprite
        # Setting the initial position of the sprite randomly within the game window
        self.center_x = randint(10, game.width - 10)
        self.center_y = randint(10, game.height - 10)
        self.change_x = 0  # Initializing the horizontal movement speed of the sprite
        self.change_y = 0  # Initializing the vertical movement speed of the sprite

class Shit(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Shit.png")  # Calling the superclass constructor with the image file path
        self.width = 36  # Setting the width of the sprite
        self.height = 36  # Setting the height of the sprite
        # Setting the initial position of the sprite randomly within the game window
        self.center_x = randint(10, game.width - 10)
        self.center_y = randint(10, game.height - 10)
        self.change_x = 0  # Initializing the horizontal movement speed of the sprite
        self.change_y = 0  # Initializing the vertical movement speed of the sprite
