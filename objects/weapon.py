import arcade
import math
from objects import bullet

class Weapon(arcade.Sprite):
    def __init__(self, player, reticle, texture, bullet_speed, bullet_texture):
        self.bullet_speed=bullet_speed
        self.bullet_texture=bullet_texture

        self.player = player
        self.reticle=reticle

        super().__init__(texture, center_x=player.center_x, center_y=player.center_y, scale=0.5)

    def update_position_and_angle(self):
        self.center_x = self.player.center_x
        self.center_y = self.player.center_y

        dx = self.reticle.center_x - self.player.center_x
        dy = self.reticle.center_y - self.player.center_y
        angle = math.degrees(math.atan2(dy, dx))

        self.angle = angle

    def shoot(self):
        arcade.get_window().bullet_list.append(bullet.Bullet(self))



class AK47(Weapon):
    def __init__(self, player, reticle):
        super().__init__(player, reticle, 'textures/ak47.png', 5, 'textures/ak47_bullet.png')


