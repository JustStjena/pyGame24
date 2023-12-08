import os
import sys

import pygame


def load_image(name, colorkey=None, size=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # Можно сразу удалить задний фон
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    # Можно сразу сжать картинку до нужного размера
    if size is not None:
        image = pygame.transform.scale(image, size)
    return image
