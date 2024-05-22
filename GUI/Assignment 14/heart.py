##### Mohammad Ali Mirzaei #####

import arcade

class Heart(arcade.Sprite):
    def __init__(self, location):
        super().__init__("heart.jpg")
        self.center_x = 20 + location * 30
        self.center_y = 20
        self.width = 30
        self.height = 30