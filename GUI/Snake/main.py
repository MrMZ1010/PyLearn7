##### MohammadAli Mirzaei #####

import arcade  # Importing arcade library for creating games
from snake import Snake  # Importing the Snake class from the snake module
from foods import *  # Importing all classes from the foods module

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="Snake Game🐍")  # Calling the superclass constructor with window parameters
        arcade.set_background_color(arcade.color.KHAKI)  # Setting the background color of the game window
        self.pear = Pear(self)  # Creating an instance of Pear class
        self.apple = Apple(self)  # Creating an instance of Apple class
        self.shit = Shit(self)  # Creating an instance of Shit class
        self.snake = Snake(self)  # Creating an instance of Snake class

    def on_key_press(self, symbol: int, modifiers: int):
        # Handling key press events for controlling the snake's movement
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
        arcade.start_render()  # Starting the rendering process
        
        # Displaying "GAME OVER!" message when the snake collides with the game window boundaries or itself
        if self.snake.score == 0 or self.snake.center_x == self.width or self.snake.center_y == self.height or self.snake.center_x == 0 or self.snake.center_y == 0:
            arcade.draw_text("GAME OVER!", 150, 300, arcade.color.RED_DEVIL, 35)
            self.snake.change_x = 0
            self.snake.change_y = 0

        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
                arcade.draw_text("GAME OVER!", 150, 300, arcade.color.RED_DEVIL, 35)
                self.snake.change_x = 0
                self.snake.change_y = 0

        # Drawing the current score on the screen
        arcade.draw_text(f"Score: {self.snake.score}", 10, 570, color=arcade.color.BLACK, font_size=20)

        # Drawing all game objects (snake, apple, pear, shit)
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.shit.draw()

        arcade.finish_render()  # Finishing the rendering process

    def on_update(self, delta_time: float):
        self.snake.move()  # Moving the snake

        # Checking for collisions between snake and pear, apple, and shit, and performing appropriate actions
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
    game = Game()  # Creating an instance of the Game class
    arcade.run()  # Running the game loop
