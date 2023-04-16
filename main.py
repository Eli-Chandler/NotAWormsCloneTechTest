import arcade
from objects.block import Block
from objects.explosion import Explosion

#from objects.player.player import Player

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Platformer"

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.block_list = arcade.SpriteList(use_spatial_hash=True)
        self.explosion_list = arcade.SpriteList()

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        block = Block(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.block_list)

    def on_update(self, delta_time: float):
        self.explosion_list.update()

    def on_draw(self):
        arcade.start_render()
        self.block_list.draw()
        for explosion in self.explosion_list:
            explosion.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        '''for hit in arcade.get_sprites_at_point((x, y), self.block_list):
            hit.subdivide()'''
        self.create_explosion_at_mouse(x, y)

    def create_explosion_at_mouse(self, mouse_x, mouse_y):
        explosion = Explosion(mouse_x, mouse_y, 10, self.explosion_list, self.block_list)




def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
