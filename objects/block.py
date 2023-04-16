import arcade
from PIL import Image
import random

MAX_DEPTH = 10
NUM_COLORS = 30

textures = []

class Block(arcade.Sprite):
    def __init__(self, center_x, center_y, screen_width, screen_height, block_list, scale=1, depth=0):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.block_list = block_list

        self.depth = depth

        if self.depth==0:
            self.create_textures()

        texture = random.choice(textures)

        super().__init__(center_x=center_x, center_y=center_y, scale=scale, texture=texture)
        self.use_spatial_hash = True
        self.color = arcade.color.WHITE
        self.block_list.append(self)


    def subdivide(self):
        self.block_list.remove(self)

        if self.depth+1 >= MAX_DEPTH:
            return

        new_width = self.screen_width
        new_height = self.screen_height
        new_scale = self.scale / 2

        for i in [-1, 1]:
            for j in [-1, 1]:
                Block(
                    self.center_x + (new_width * i * new_scale) / 2,
                    self.center_y + (new_height * j * new_scale) / 2,
                    new_width,
                    new_height,
                    self.block_list,
                    new_scale,
                    depth = self.depth+1
                )

    def create_textures(self):
        for i in range(NUM_COLORS):

            img = Image.new("RGBA", (self.screen_width, self.screen_height),
                            color=(random.randint(0, 255),
                                   random.randint(0, 255),
                                   random.randint(0, 255),
                                   255))

            texture = arcade.Texture(f"brown_rectangle_{i}", image=img) # Cache texture
            textures.append(texture)





