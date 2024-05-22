##### Mohammad Ali Mirzaei #####

import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.width = 48
        self.height = 48
        self.speed = 8
        self.game_with = game.width
        self.bullet_list = []





