import arcade

class Block():
    def __init__(self, center_x, center_y, width, height, block_list):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

        self.rectangle = arcade.create_rectangle_filled(center_x, center_y, width, height, color=arcade.color.BROWN)

        self.block_list = block_list
        self.block_list.append(self.rectangle)

    def subdivide(self):
        self.block_list.remove(self.rectangle)
        

    def destroy(self):
        self.is_solid = False
        self.alpha = 0
