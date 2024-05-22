import arcade
from bullet import Bullet


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.width = 60
        self.height = 60
        self.speed = 4
        self.game_with = game.width
        self.bullet_list = []
        self.heart_list = []
        self.fire_sound = arcade.load_sound(':resources:sounds/laser1.wav')

    def move(self):
        if self.change_x == -1:
            if self.center_x > 24:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.game_with - 24:
                self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)

        arcade.play_sound(
            sound = self.fire_sound
        )
        
    def bullet_rise_speed(self):
        Bullet(self).rise_speed()