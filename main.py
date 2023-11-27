import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    v=20
    fps = 60
    clock = pygame.time.Clock()
    x_pos=0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
        x_pos += 1
        x_pos += v / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()