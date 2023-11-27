import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    x_pos=0
    screen = pygame.display.set_mode(size)

    while pygame.event.wait().type != pygame.QUIT:
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
        x_pos += 1
        pygame.display.flip()
    pygame.quit()