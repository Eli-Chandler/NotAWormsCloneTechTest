import arcade
from objects.block import Block

#from objects.player.player import Player

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BOARD_SIZE_X = 1000
BOARD_SIZE_Y = (SCREEN_WIDTH//SCREEN_HEIGHT) * BOARD_SIZE_X
BLOCK_SIZE = 16
BLOCK_SCALE = SCREEN_WIDTH / BOARD_SIZE_X / BLOCK_SIZE

SCREEN_TITLE = "Platformer"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.block_list = arcade.SpriteList()



    def setup(self):
        block = Block(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.block_list)

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.block_list.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for hit in arcade.get_sprites_at_point((x, y), self.block_list):
            hit.subdivide()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
