##### MohammadAli Mirzaei #####

import arcade
from bullet import Bullet  # Import the Bullet class from the bullet module

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        # Initialize the Spaceship sprite with the image of a blue player ship
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        # Set the initial position of the spaceship at the top center of the game window
        self.center_x = game.width // 2
        self.center_y = 50
        # Set the initial movement speed of the spaceship
        self.speed = 4
        # Set the initial movement direction of the spaceship (no movement initially)
        self.change_x = 0
        self.change_y = 0
        # Set the width and height of the spaceship
        self.width = 60
        self.height = 60
        # Store the width of the game window
        self.game_with = game.width
        # Initialize lists to hold bullets and hearts
        self.bullet_list = []
        self.heart_list = []
        # Load the sound for firing bullets
        self.fire_sound = arcade.load_sound(':resources:sounds/laser1.wav')

    def move(self):
        # Move the spaceship horizontally based on the change in x-coordinate
        if self.change_x == -1:  # Move left
            if self.center_x > 24:  # Ensure spaceship doesn't move past the left edge
                self.center_x -= self.speed
        elif self.change_x == 1:  # Move right
            if self.center_x < self.game_with - 24:  # Ensure spaceship doesn't move past the right edge
                self.center_x += self.speed

    def fire(self):
        # Create a new bullet object and add it to the bullet list
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
        # Play the sound effect for firing bullets
        arcade.play_sound(sound=self.fire_sound)

    def bullet_rise_speed(self):
        # Increase the speed of bullets
        Bullet(self).rise_speed()
