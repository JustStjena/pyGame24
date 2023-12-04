import random
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


class Minesweeper(Board):
    def __init__(self, width, height, n):
        super().__init__(width, height)
        # вначале все клетки закрыты
        self.board = [[-1] * width for _ in range(height)]
        i = 0
        while i < n:  # пока не открыли все n клеток
            x = random.randint()  # дописать аргумент для определения рандомной координаты
            y = random.randint()  # дописать аргумент для определения рандомной координаты
            if self.board[y][x] == -1:
                self.board[y][x] = 10  # кладем бомбу
                i += 1

    def on_click(self, cell):
        self.open_cell(cell)
        x, y = cell
        # проверяем на бомбу
        if self.board[y][x] == 10:
            return False
        bomb_count = 0
        # также как в Жизни обходим клетки и смотрим есть ли бомбы и считаем их
        self.board[y][x] = bomb_count

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                # мина - красный квадрат
                if self.board[y][x] == 10:
                    pass
                    # мина - красный квадрат
                else:
                    pass
                    # пустой квадрат

                if self.board[y][x] >= 0 and self.board[y][x] != 10:  # для всех открытых дополнительно надпись
                    font = pygame.font.Font(None, self.cell_size - 6)
                    text = font.render(str(self.board[y][x]), 1, (100, 255, 100))
                    screen.blit(text, (
                        x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3))


if __name__ == '__main__':
    pygame.init()
    size = 320, 470
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Дедушка сапёра')
    board = Minesweeper(10, 15, 10)
    board.set_view(10, 10, 30)

    # Включено ли обновление поля
    time_on = False
    ticks = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)

        pygame.display.flip()
        clock.tick(50)
        ticks += 1
    pygame.quit()
