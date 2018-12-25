import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 255))
running = True
draw = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            draw = True
            r = 1
            screen.fill((0, 0, 255))
    if draw:
        pygame.draw.circle(screen, pygame.Color('yellow'), position, int(r))
        r += 2
    clock.tick(50)
    pygame.display.flip()
pygame.quit()