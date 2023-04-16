import arcade
from PIL import Image, ImageDraw

GRAVITY = 1
MOVEMENT_SPEED = 2
JUMP_SPEED = 10

STAIR_HEIGHT = 20
TEXTURE_SIZE = 16

import random

class Player(arcade.Sprite):
    def __init__(self, center_x, center_y, camera):


        super().__init__('textures/player.png', center_x=center_x, center_y=center_y, hit_box_algorithm='Simple', scale=0.5)
        self.get_hit_box()
        self.direction = 0

    def update(self):
        self.change_x = MOVEMENT_SPEED * self.direction

    def jump(self):
        self.change_y = JUMP_SPEED

