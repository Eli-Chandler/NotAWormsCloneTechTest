import arcade
import math


class Bullet(arcade.Sprite):
    def __init__(self, weapon):
        self.speed = weapon.bullet_speed





        super().__init__(weapon.bullet_texture, center_x=weapon.center_x, center_y=weapon.center_y)
        self.scale=0.05
        self.angle=weapon.angle

        self.change_x = math.cos(math.radians(self.angle)) * self.speed
        self.change_y = math.sin(math.radians(self.angle)) * self.speed

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y