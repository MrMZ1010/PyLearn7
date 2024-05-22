from random import randint
import arcade

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Apple.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Pear(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Pear.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Shit(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Shit.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0
