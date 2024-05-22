##### Mohammad Ali Mirzaei #####

import random
import arcade
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.doshman = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )
        self.me.draw()
        self.doshman.draw()
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.me.center_x -= self.me.speed 
        elif symbol == arcade.key.D:
            self.me.center_x += self.me.speed
            
    def on_update(self, delta_time: float):

        self.doshman.center_x -=self.doshman.speed
