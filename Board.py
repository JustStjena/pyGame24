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
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

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


if __name__ == '__main__':
    # Иницилизаци яприложения
    pygame.init()
    SIZE = WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Не забываем писать заголовок окна')
    # Инициализация клетчатого поля
    BOARD_WIDTH, BOARD_HEIGHT = 5, 7
    board = Board(BOARD_WIDTH, BOARD_HEIGHT)
    board_size = min(WIDTH // BOARD_WIDTH, HEIGHT // BOARD_HEIGHT)
    board.set_view(0, 0, board_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
