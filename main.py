import arcade
from objects.block import Block
from objects.explosion import Explosion
from objects.player import Player
from objects import weapon
import math
#from objects.player.player import Player

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SCREEN_TITLE = "Platformer"

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.setup()

    def setup(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.block_list = arcade.SpriteList(use_spatial_hash=True)
        self.explosion_list = arcade.SpriteList()
        self.camera = arcade.Camera()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        block = Block(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.block_list)

        self.player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, self.camera)



        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        self.create_explosion_at_position(self.player.center_x, self.player.center_y, 5)
        while self.explosion_list:
            self.explosion_list.update()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.block_list, gravity_constant=1)

        self.reticle = arcade.Sprite('textures/reticle.png', scale=0.5)
        self.reticle_list = arcade.SpriteList()
        self.reticle_list.append(self.reticle)
        self.update_reticle_position(0, 0)

        self.bullet_list = arcade.SpriteList()

        self.player.weapon = weapon.AK47(self.player, self.reticle)
        self.weapon_list = arcade.SpriteList()
        self.weapon_list.append(self.player.weapon)

    def on_update(self, delta_time: float):
        x, y = self.convert_viewport_coordinates_to_global(self.mouse_x, self.mouse_y)
        self.update_reticle_position(x, y)
        self.explosion_list.update()
        self.physics_engine.update()
        self.player.update()
        self.bullet_list.update()

        #self.player_list.update()

    def on_draw(self):
        #self.camera.use()
        arcade.start_render()
        self.set_viewport(self.player.center_x-160, self.player.center_x+160, self.player.center_y-90, self.player.center_y+90)

        self.block_list.draw()
        self.player_list.draw()
        for explosion in self.explosion_list:
            explosion.draw()
        self.reticle_list.draw()
        self.weapon_list.draw()
        self.bullet_list.draw()

    def convert_viewport_coordinates_to_global(self, x, y):
        left, right, bottom, top = self.get_viewport()


        screen_width = self.screen.width
        screen_height = self.screen.height

        x_ratio = screen_width / (right - left)
        y_ratio = screen_height / (top - bottom)

        global_x = x / x_ratio + left
        global_y = y / y_ratio + bottom

        return global_x, global_y

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
        if symbol == arcade.key.UP or symbol == arcade.key.W or symbol == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.jump()
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.player.direction = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player.direction = 1

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            if self.player.direction == -1:
                self.player.direction = 0

        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            if self.player.direction == 1:
                self.player.direction = 0


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        '''for hit in arcade.get_sprites_at_point((x, y), self.block_list):
            hit.subdivide()'''

        print(self.convert_viewport_coordinates_to_global(x, y))
        x, y = self.convert_viewport_coordinates_to_global(x, y)
        self.create_explosion_at_position(x, y, 5)
        self.player.weapon.shoot()

    def create_explosion_at_position(self, x, y, size=5):
        explosion = Explosion(x, y, size, self.explosion_list, self.block_list)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_x = x
        self.mouse_y = y
        x, y = self.convert_viewport_coordinates_to_global(x, y)



    def update_reticle_position(self, x, y):
        angle = self.calculate_angle(self.player.center_x, self.player.center_y, x, y)
        distance_from_player = 50
        reticle_x = self.player.center_x + distance_from_player * math.cos(math.radians(angle))
        reticle_y = self.player.center_y + distance_from_player * math.sin(math.radians(angle))

        # Center the reticle on the mouse cursor
        #reticle_x -= self.reticle.width / 2
        #reticle_y -= self.reticle.height / 2

        self.reticle.center_x = reticle_x
        self.reticle.center_y = reticle_y

    @staticmethod
    def calculate_angle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))




def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
