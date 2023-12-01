import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


if __name__ == '__main__':
    pygame.init()
    SIZE = WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Не забываем писать заголовок окна')

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
