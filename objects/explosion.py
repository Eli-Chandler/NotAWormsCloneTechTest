import arcade
from PIL import Image, ImageDraw
import math

textures = {}
TEXTURE_SIZE = 200

class Explosion(arcade.Sprite):
    def __init__(self, center_x, center_y, explosion_size, explosion_list, block_list, explosion_color=arcade.color.WHITE):
        window = arcade.get_window()
        width = window.width
        explosion_size = TEXTURE_SIZE / width * explosion_size
        self.explosion_color = explosion_color
        self.explosion_size = explosion_size
        self.explosion_list = explosion_list
        self.block_list = block_list

        texture = textures.get(str(self.explosion_color), self.create_texture())

        super().__init__(center_x=center_x, center_y=center_y, texture=texture, scale=self.explosion_size, hit_box_algorithm='Detailed', hit_box_detail=100)

        self.explosion_list.append(self)
        self.alpha=100
        self.hit_list = []

    def check_sprite_fully_outside(self, sprite):
        # Calculate the closest point on the sprite's bounding box to the circle's center
        closest_x = max(sprite.left, min(self.center_x, sprite.right))
        closest_y = max(sprite.bottom, min(self.center_y, sprite.top))

        # Calculate the distance between the closest point and the circle's center
        distance_squared = (closest_x - self.center_x) ** 2 + (closest_y - self.center_y) ** 2

        # Check if the distance is greater than the circle's radius squared
        return distance_squared > (self.width / 2) ** 2


    def check_sprite_fully_encompassed(self, sprite):
        bottom_left = (sprite.left, sprite.bottom)
        bottom_right = (sprite.right, sprite.bottom)
        top_left = (sprite.left, sprite.top)
        top_right = (sprite.right, sprite.top)

        points = [bottom_left, bottom_right, top_left, top_right]

        for point in points:
            distance_from_center = ((point[0] - self.center_x)**2 + (point[1] - self.center_y)**2) ** 0.5
            if distance_from_center > self.width/2:
                return False
        return True

    def update(self):
        self.explode()

    def explode(self):
        hits = arcade.check_for_collision_with_list(self, self.block_list)

        num_subdivided = 0

        for hit in hits:
            if self.check_sprite_fully_encompassed(hit):
                self.block_list.remove(hit)
            elif self.check_sprite_fully_outside(hit):
                continue
            else:
                hit.subdivide()
                num_subdivided += 1

        if num_subdivided == 0:
            self.destroy()


    def destroy(self):
        self.explosion_list.remove(self)

    def create_texture(self):
        # create a new image with white background
        image = Image.new('RGBA', (TEXTURE_SIZE, TEXTURE_SIZE), (255, 255, 255, 0))


        # create a drawing context
        draw = ImageDraw.Draw(image)

        # calculate the center coordinates of the circle
        center_x, center_y = image.size[0] // 2, image.size[1] // 2

        # calculate the radius of the circle
        radius = TEXTURE_SIZE // 2

        # draw a black circle centered in the image
        draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=self.explosion_color)

        texture = arcade.Texture(str(self.explosion_color), image=image)

        textures[self.explosion_color] = texture
        return texture

