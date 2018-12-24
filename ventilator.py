import pygame
import math


def draw(t, shag, surface):
    radius = 67
    centre = 100
    shag_v_rad = math.pi / 12
    pygame.draw.polygon(surface, pygame.Color('white'),
                        [[centre, centre],
                         [int(centre + radius * math.sin(t + shag_v_rad * shag)),
                          int(centre + radius * math.cos(t + shag_v_rad * shag))],
                         [int(centre + radius * math.sin(t + shag_v_rad * (shag + 2))),
                          int(centre + radius * math.cos(t + shag_v_rad * (shag + 2)))]])


pygame.init()
screen = pygame.display.set_mode((201, 201))
clock = pygame.time.Clock()
running = True
t = 0
v = 0

while running:
    tick = clock.tick(25)
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, pygame.Color('white'), (100, 100), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                v += math.pi / 90
            elif event.button == 3:
                v -= math.pi / 90
    t += v
    if t > 6.3:
        t = 0
    draw(t, 3, screen)
    draw(t, 11, screen)
    draw(t, 19, screen)
    pygame.display.flip()

pygame.quit()
