##### MohammadAli Mirzaei #####

import random  # Import the random module for generating random numbers
import arcade  # Import the arcade module for creating games
from spaceship import Spaceship  # Import the Spaceship class from spaceship module
from enemy import Enemy  # Import the Enemy class from enemy module
from game import Game  # Import the Game class from game module

window = Game()  # Create an instance of the Game class and assign it to the variable 'window'
arcade.run()  # Start the game loop, which continuously updates and renders the game
