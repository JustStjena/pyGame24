import copy

import pygame


class Board:
    '''
    Класс клетчатого поля для игры
    '''

    def __init__(self, width, height):
        '''
        :param width: Количество клеток в строке(по-умолчанию - 10)
        :param height: Количество клеток в столбце(по-умолчанию - 10)
        '''
        self.width = width
        self.height = height
        # Матрица состояний клетов доски
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        '''
        Метод отрисовки клетчатого поля
        :param screen: Хост на котором будт поле
        '''
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))

    def pos2coord(self, pos):
        x = (pos[0] - self.top) // self.cell_size
        y = (pos[1] - self.left) // self.cell_size
        if x > self.width - 1 or y > self.height - 1 or x < 0 or y < 0:
            return None
        return x, y

    def on_click(self, pos):
        pass

    def set_view(self, left, top, cell_size):
        '''
        Настройка внешнего вида клетчатого поля
        :param left: Координаты левого верхнего угла
        :param top:  Координаты правого верхнего угла
        :param cell_size: Размер клетки
        '''
        self.left = left
        self.top = top
        self.cell_size = cell_size


class Life(Board):
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height)
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        if self.board[cell[1]][cell[0]] == 1:
            self.board[cell[1]][cell[0]] = 0
        else:
            self.board[cell[1]][cell[0]] = 1

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                # живые клетки рисуем зелеными
                else:
            # дохлые клетки просто контур

    def who_ia_alive(self, x, y, tmp_board):

    # возвращает1  если клетка выжила и 0 наоборот

    def next_move(self):
        # сохраняем поле
        tmp_board = self.board[::]
        # пересчитываем
        for y in range(self.height):
            for x in range(self.width):
                tmp_board[y][x] = self.who_ia_alive(x, y, tmp_board)

        # обновляем поле
        self.board = copy.deepcopy(tmp_board)


if __name__ == '__main__':
    pygame.init()
    size = 470, 470
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Игра «Жизнь»')

    board = Life(30, 30, 10, 10, 15)

    # Включено ли обновление поля
    time_on = False
    ticks = 0
    speed = 10

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                time_on = not time_on
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                speed += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                speed -= 1

        screen.fill((0, 0, 0))
        board.render(screen)
        if ticks >= speed:
            if time_on:
                board.next_move()
            ticks = 0
        pygame.display.flip()
        clock.tick(100)
        ticks += 1
    pygame.quit()
