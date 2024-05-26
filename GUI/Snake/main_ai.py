##### MohammadAli Mirzaei #####

import arcade  # Importing arcade library for creating games
from snake import Snake  # Importing the Snake class from the snake module
from foods import *  # Importing all classes from the foods module

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="AI Snake Game🐍")  # Calling the superclass constructor with window parameters
        arcade.set_background_color(arcade.color.GREEN)  # Setting the background color of the game window
        self.apple = Apple(self)  # Creating an instance of Apple class
        self.snake = Snake(self)  # Creating an instance of Snake class
        self.snake.score = 0  # Initializing the score attribute of the snake

    def on_draw(self):
        arcade.start_render()  # Starting the rendering process
        # Drawing the current score on the screen
        arcade.draw_text(f"Score: {self.snake.score}", 10, 570, color=arcade.color.BLACK, font_size=20)
        self.snake.draw()  # Drawing the snake
        self.apple.draw()  # Drawing the apple
        arcade.finish_render()  # Finishing the rendering process

    def on_update(self, delta_time: float):
        # Checking for collision between snake and apple
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat_apple(self.apple)  # If collision occurs, calling eat_apple method of snake
            self.apple = Apple(self)  # Creating a new instance of Apple at a random position

        # Moving the snake towards the apple's position using AI logic
        self.snake.move_with_ai(self.apple.center_x, self.apple.center_y)
        self.snake.move()  # Moving the snake

if __name__ == "__main__":
    game = Game()  # Creating an instance of the Game class
    arcade.run()  # Running the game loop

