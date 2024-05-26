##### MohammadAli Mirzaei #####

import random
import time
from typing import Optional
import arcade
from arcade import Texture
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart

class Game(arcade.Window):
    def __init__(self):
        # Initialize the game window
        super().__init__(width=800, height=600, title="Interstellar")
        # Load the background texture
        self.background = arcade.load_texture("back.jpg")
        # Create the player spaceship object
        self.me = Spaceship(self)
        # Initialize score
        self.score = 0
        # Lists to hold enemy and heart objects
        self.enemy_list = []
        self.heart_list = []
        # Load game sounds
        self.gameover = arcade.load_sound(':resources:sounds/gameover1.wav', False)
        self.laser_sound = arcade.load_sound(':resources:sounds/hit1.wav')
        self.black_page = arcade.load_texture("black.png")
        # Create heart objects and add them to the heart list
        for i in range(3):
            heart_object = Heart(i)
            self.heart_list.append(heart_object)
        # Track time
        self.second = time.time()
        self.rise_speed = time.time()

    def on_draw(self):
        # Draw objects on the screen
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )
        # Draw score
        arcade.draw_text(str(self.score), self.width-60, 15, arcade.color.WHITE, 25, 12)
        # Draw player spaceship
        self.me.draw()
        # Draw enemies
        for enemiesn in self.enemy_list:
            enemiesn.draw()
        # Draw bullets
        for bullet in self.me.bullet_list:
            bullet.draw()
        # Draw hearts
        for heart in self.heart_list:
            heart.draw()
        # Display game over if no more hearts left
        if len(self.heart_list) == 0:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.black_page)
            arcade.draw_text("GAME OVER", self.width/3, self.height/2, arcade.color.RED, 36, 15)
        # Update enemy movement and collision detection
        for enemies in self.enemy_list:
            enemies.move()
            if arcade.check_for_collision(self.me, enemies):
                arcade.play_sound(self.gameover, 1)
                time.sleep(1)
                exit(0)
            if enemies.center_y < 0:
                self.enemy_list.remove(enemies)
                self.heart_list.pop()
                if len(self.heart_list) == 0:
                    arcade.play_sound(self.gameover, 1)
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        # Respond to key presses
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.S:
            self.me.change_x = 0
        elif symbol == arcade.key.SPACE or symbol == arcade.key.UP:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        # Respond to key releases
        self.me.change_x = 0

    def on_update(self, delta_time: float):
        # Update game state
        if len(self.heart_list) != 0:
            self.me.move()
            for bullet in self.me.bullet_list:
                bullet.move()
            for enemies in self.enemy_list:
                for bullet in self.me.bullet_list:
                    if arcade.check_for_collision(enemies, bullet):
                        arcade.play_sound(sound=self.laser_sound)
                        self.enemy_list.remove(enemies)
                        self.me.bullet_list.remove(bullet)
                        self.score += 1
            if time.time()-self.second >= 3:
                self.second = time.time()
                self.enemies = Enemy(self)
                self.enemy_list.append(self.enemies)
            if time.time()-self.rise_speed >= 10:
                self.rise_speed = time.time()
                Enemy(self).rise_speed()
                self.me.bullet_rise_speed()
        else:
            # Clear lists and end game if no more hearts left
            self.enemy_list.clear()
            self.me.bullet_list.clear()
            self.me.kill()

    
    



    


