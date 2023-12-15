import pygame

from functoins import load_level, load_image
from settings import *

# Инициализируем игру
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

# создаем  player
# открываем стартовый экран который воспроизводит игровой цикл пока не нажмем кнопку

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass
            # обработка нажатий стрелок
    screen.fill(pygame.Color("black"))
    # Отрисовываем тайлы
    # Отрисовываем игрока
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
