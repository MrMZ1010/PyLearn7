import arcade
from snake import Snake
from foods import *

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height = 600,title = "AI Snake Game🐍")
        arcade.set_background_color(arcade.color.GREEN)
        self.apple = Apple(self)
        self.snake = Snake(self)
        self.snake.score = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Score: {self.snake.score}",10,570,color=arcade.color.BLACK,font_size=20)
        self.snake.draw()
        self.apple.draw()

        arcade.finish_render()

    def on_update(self, delta_time: float):

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat_apple(self.apple)
            self.apple = Apple(self)

        self.snake.move_with_ai(self.apple.center_x, self.apple.center_y)
        self.snake.move()

if __name__ == "__main__":
    game = Game()
    arcade.run()
