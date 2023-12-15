import os
import sys

import pygame

from Player import Player
from Tile import Tile


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


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level, tile_group, player_group, tile_images, player_image):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile(tile_images, 'empty', x, y, tile_group)
            elif level[y][x] == '#':
                Tile(tile_images, 'wall', x, y, tile_group)
            elif level[y][x] == '@':
                Tile(tile_images, 'empty', x, y, tile_group)
                new_player = Player(player_image, x, y, player_group)
                # level[y][x] = "."
    return new_player, x, y


def move(hero, level_map, movement, max_x, max_y):
    x, y = hero.pos
    print(level_map[x][y - 1])
    print(level_map[x][y + 1])
    print(level_map[x - 1][y])
    print(level_map[x][y + 1])
    print()
    if movement == "up":
        if y > 0 and level_map[y - 1][x] == ".":
            hero.move(x, y - 1)
    elif movement == "down":
        if y < max_y - 1 and level_map[y + 1][x] == ".":
            hero.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == ".":
            hero.move(x - 1, y)
    elif movement == "right":
        if x < max_x - 1 and level_map[y][x + 1] == ".":
            hero.move(x + 1, y)
