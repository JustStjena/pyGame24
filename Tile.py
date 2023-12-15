from pygame.sprite import Sprite

from settings import tile_width, tile_height


class Tile(Sprite):
    def __init__(self, tile_images, tile_type, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
