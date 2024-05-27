##### MohammadAli Mirzaei #####

import arcade  # Import the arcade module for graphics and game development
from ball import Ball  # Import the Ball class from the ball module
from rocket import Rocket  # Import the Rocket class from the rocket module

class Game(arcade.Window):  # Define a class named Game that inherits from arcade.Window

    def __init__(self):  # Initialize the Game class
        super().__init__(width=800, height=500, title="Pong")  # Call the parent class's constructor with specified width, height, and title
        arcade.set_background_color(arcade.color.DARK_GREEN)  # Set the background color of the game window
        self.Player1 = Rocket(40, self.height // 2, arcade.color.RED, "Player 1")  # Create Player 1 Rocket object
        self.Player2 = Rocket(self.width - 40, self.height // 2, arcade.color.BLUE, "Player 2")  # Create Player 2 Rocket object
        self.ball = Ball(self)  # Create Ball object
        self.Players = arcade.SpriteList()  # Create a SpriteList to hold player sprites
        self.Players.append(self.Player1)  # Add Player 1 to the sprite list
        self.Players.append(self.Player2)  # Add Player 2 to the sprite list

    def on_draw(self):  # Define a method to handle drawing the game window
        arcade.start_render()  # Start rendering the game
        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 30, self.height - 30, arcade.color.WHITE, 5)  # Draw the game boundary
        arcade.draw_line(self.width // 2, 30, self.width // 2, self.height - 30, arcade.color.WHITE, 3)  # Draw the center line
        arcade.draw_text(f"Score: {self.Player1.score}", 30, 30, arcade.color.YELLOW, 18)  # Draw Player 1's score
        arcade.draw_text(f"Score: {self.Player2.score}", self.width - 120, 30, arcade.color.YELLOW, 18)  # Draw Player 2's score
        self.Player1.draw()  # Draw Player 1
        self.Player2.draw()  # Draw Player 2
        self.ball.draw()  # Draw the ball
        arcade.finish_render()  # Finish rendering the game

    def on_update(self, delta_time: float):  # Define a method to update the game state
        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30:  # If the ball hits the top or bottom boundary
            self.ball.change_y *= -1  # Reverse the y direction of the ball

        if arcade.check_for_collision_with_list(self.ball, self.Players):  # If the ball collides with any player
            self.ball.change_x *= -1  # Reverse the x direction of the ball

        if self.ball.center_x < 0:  # If the ball goes beyond the left boundary
            self.Player2.score += 1  # Increment Player 2's score
            del self.ball  # Delete the ball object
            self.ball = Ball(self)  # Create a new ball object

        if self.ball.center_x > self.width:  # If the ball goes beyond the right boundary
            self.Player1.score += 1  # Increment Player 1's score
            del self.ball  # Delete the ball object
            self.ball = Ball(self)  # Create a new ball object
        
        self.ball.move()  # Move the ball
        self.Player2.move(self.ball, self)  # Move Player 2 according to the ball position

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):  # Define a method to handle mouse motion
        if self.Player1.height < y < self.height - self.Player1.height:  # If the mouse y position is within the game boundary
            self.Player1.center_y = y  # Update Player 1's y position with the mouse y position

game = Game()  # Create an instance of the Game class
arcade.run()  # Run the game loop
