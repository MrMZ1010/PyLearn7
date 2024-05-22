import arcade
from snake import Snake
from foods import *

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height = 600,title = "Snake Game🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.pear = Pear(self)
        self.apple = Apple(self)
        self.shit = Shit(self)
        self.snake = Snake(self)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.snake.change_x = -1
            self.snake.change_y = 0
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.snake.change_x = 1
            self.snake.change_y = 0

    def on_draw(self):
        arcade.start_render()
        
        if self.snake.score == 0:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
            self.snake.change_x = 0
            self.snake.change_y = 0
            

        if self.snake.center_x == self.width or self.snake.center_y == self.height:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
            self.snake.change_x = 0
            self.snake.change_y = 0
            
        
        if self.snake.center_x == 0 or self.snake.center_y == 0:
            arcade.draw_text("GAME OVER!",150,300,arcade.color.RED_DEVIL,35)
            self.snake.change_x = 0
            self.snake.change_y = 0
            
  
        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
                arcade.draw_text("GAME OVER!", 150, 300, arcade.color.RED_DEVIL, 35)
                self.snake.change_x = 0
                self.snake.change_y = 0

        arcade.draw_text(f"Score: {self.snake.score}",10,570,color=arcade.color.BLACK,font_size=20)

        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.shit.draw()

        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat_pear(self.apple)
            self.pear = Pear(self)

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat_apple(self.apple)
            self.apple = Apple(self)

        if arcade.check_for_collision(self.snake, self.shit):
            self.snake.eat_shit(self.shit)
            self.shit = Shit(self)

if __name__ == "__main__":
    game = Game()
    arcade.run()
