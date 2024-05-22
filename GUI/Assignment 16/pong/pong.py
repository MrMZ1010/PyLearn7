##### MohammadAli Mirzaei #####

import arcade
from ball import Ball
from rocket import Rocket

class Game(arcade.Window):

    def __init__(self):
        super().__init__(width=800, height=500, title="Pong")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.Player1 = Rocket(40, self.height//2, arcade.color.RED, "Player 1")
        self.Player2 = Rocket(self.width-40, self.height//2, arcade.color.BLUE, "Player 2")
        self.ball = Ball(self)
        self.Players = arcade.SpriteList()
        self.Players.append(self.Player1)
        self.Players.append(self.Player2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2, self.width-30, self.height-30, arcade.color.WHITE, 5)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height-30, arcade.color.WHITE, 3)
        arcade.draw_text(f"Score: {self.Player1.score}", 30, 30, arcade.color.YELLOW, 18)
        arcade.draw_text(f"Score: {self.Player2.score}", self.width-120, 30, arcade.color.YELLOW, 18)
        self.Player1.draw()
        self.Player2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        if self.ball.center_y < 30 or self.ball.center_y > self.height-30:
            self.ball.change_y *= -1

        if arcade.check_for_collision_with_list(self.ball, self.Players):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            self.Player2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width:
            self.Player1.score += 1
            del self.ball
            self.ball = Ball(self)
        
        self.ball.move()
        self.Player2.move(self.ball, self)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.Player1.height < y < self.height-self.Player1.height:
            self.Player1.center_y = y

game = Game()
arcade.run()