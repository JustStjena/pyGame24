import pygame

class Ball():
    def __init__(self, pos, radius):
        #стартовые атрибуты шарика
    def move(self):
        #изменение атрибутов шарика при движении
    def draw(self):
        #отрисовка шарика по атрибутам


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()
    balls=[]  #Заводим коллекцию, в оторой будем хранить нарисованные шарики
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Добавить экземпляр класса Ball в коллекцию balls
        for ball in balls:
            #Подвинуть шарик
            #Отрисовать шарик

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

    # Подумать,куда воткнуть screen.fill((0, 0, 0))