from pygame.sprite import Sprite

from settings import tile_width, tile_height


class Player(Sprite):
    def __init__(self, player_image, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)
