##### MohammadAli Mirzaei #####

import arcade

class Bullet(arcade.Sprite):
    def __init__(self, host):
        # Initialize the Bullet sprite with the image of a blue laser
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        # Set the initial position of the bullet to match the host's position
        self.center_x = host.center_x
        self.center_y = host.center_y
        # Set the speed of the bullet
        self.speed = 6
        # Set the initial direction of the bullet (straight up)
        self.change_x = 0
        self.change_y = 1
        # Set the angle of the bullet (90 degrees, pointing upwards)

    def move(self):
        # Move the bullet vertically upwards by its speed
        self.center_y += self.speed

    def rise_speed(self):
        # Increase the speed of the bullet
        self.speed += 1
