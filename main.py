import pygame

from functoins import load_level, load_image, generate_level, move
from settings import *
from start import start_screen

pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()
# Создаем спрайты
tile_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')
level_map = load_level("map.map")

# открываем стартовый экран который воспроизводит игровой цикл пока не нажмем кнопку
start_screen(screen, clock)
# Как только на стартовом экране нажали кнопку, функция завершилась(return) и нас выкинуло в продолжение программы

player, max_x, max_y = generate_level(level_map, tile_group, hero_group, tile_images, player_image)
print(tile_group)
print(hero_group)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(player, level_map, "up", max_x, max_y)
            elif event.key == pygame.K_DOWN:
                move(player, level_map, "down", max_x, max_y)
            elif event.key == pygame.K_LEFT:
                move(player, level_map, "left", max_x, max_y)
            elif event.key == pygame.K_RIGHT:
                move(player, level_map, "right", max_x, max_y)
    screen.fill(pygame.Color("black"))
    tile_group.draw(screen)
    hero_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
