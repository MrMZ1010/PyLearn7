##### MohammadAli Mirzaei #####

import arcade  # Import the arcade module for game development
from ball import Ball  # Import the Ball class from the ball module
from block import Block  # Import the Block class from the block module
from rocket import Rocket  # Import the Rocket class from the rocket module

# Define the Game class, inheriting from arcade.Window
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=800, title="Breakout")  # Initialize the game window with width, height, and title
        arcade.set_background_color(arcade.color.BLUE)  # Set the background color of the game window to blue
        self.player = Rocket(self)  # Create an instance of the Rocket class for the player
        self.ball = Ball(self)  # Create an instance of the Ball class for the ball
        self.block_list = arcade.SpriteList()  # Create a list to hold block sprites

        # Create and position blocks in the game window
        for i in range(400, self.height-100, 50):  # Loop to create rows of blocks
            for j in range(90, self.width-80, 80):  # Loop to create columns of blocks
                new_block = Block(j, i, arcade.color.GREEN)  # Create a new block with given position and color
                new_block.center_x = j  # Set the block's horizontal position
                new_block.center_y = i  # Set the block's vertical position
                self.block_list.append(new_block)  # Add the block to the block list

    # Define the method to handle drawing the game elements
    def on_draw(self):
        arcade.start_render()  # Start the render process
        arcade.draw_rectangle_outline(250, 360, self.width-80, self.height, arcade.color.DARK_BLUE, 3)  # Draw the game boundary
        arcade.draw_text(f"Score: {self.player.score}", (self.width//2)+30, self.height-30, arcade.color.WHITE, 25)  # Draw the score
        arcade.draw_text(f"HP: {self.player.health}", (self.width//2)-110, self.height-30, arcade.color.WHITE, 25)  # Draw the health
        self.player.draw()  # Draw the player (rocket)
        self.ball.draw()  # Draw the ball
        for block in self.block_list:  # Loop to draw each block in the block list
            block.draw()

        # Check for game over condition
        if self.player.health == 0:
            arcade.draw_text("GAME OVER", (self.width//2)-95, self.height//2, arcade.color.RED, 24)  # Display "GAME OVER"
            self.player.change_x = 0  # Stop the player's horizontal movement
            self.player.change_y = 0  # Stop the player's vertical movement (if applicable)
            self.ball.change_x = 0  # Stop the ball's horizontal movement
            self.ball.change_y = 0  # Stop the ball's vertical movement
        arcade.finish_render()  # Finish the render process

    # Define the method to update the game elements
    def on_update(self, delta_time: float):
        self.player.move()  # Update the player's position
        self.ball.move()  # Update the ball's position
        
        # Check for collision with the left or right boundaries
        if 50 >= self.ball.center_x or self.ball.center_x >= self.width - 50:
            self.ball.change_x *= -1  # Reverse the ball's horizontal direction

        # Check for collision with the top boundary
        if self.ball.center_y >= self.height - 50:
            self.ball.change_y *= -1  # Reverse the ball's vertical direction

        # Prevent the player from moving out of bounds on the left side
        if self.player.center_x <= 80:
            self.player.change_x = 0

        # Prevent the player from moving out of bounds on the right side
        if self.player.center_x >= self.width - 80:
            self.player.change_x = 0

        # Check for collision between the player and the ball
        if arcade.check_for_collision(self.player, self.ball):
            self.ball.change_y *= -1  # Reverse the ball's vertical direction

        # Check for collision between the ball and any block
        for block in self.block_list:
            if arcade.check_for_collision(self.ball, block):
                self.player.score += 1  # Increase the player's score
                self.block_list.remove(block)  # Remove the block from the list
                self.ball.change_y *= -1  # Reverse the ball's vertical direction

        # Check if the ball falls below the screen
        if self.ball.center_y < 0:
            self.player.health -= 1  # Decrease the player's health
            del self.ball  # Delete the current ball
            self.ball = Ball(self)  # Create a new ball

    # Define the method to handle key press events
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -1  # Move the player to the left
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 1  # Move the player to the right

    # Define the method to handle mouse motion events
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player.width < x < self.width - self.player.width:
            self.player.change_x = 0  # Stop the player's horizontal movement
            self.player.center_x = x  # Set the player's horizontal position to the mouse position

# Create an instance of the Game class and start the game
game = Game()
arcade.run()

