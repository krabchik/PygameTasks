import pygame

pygame.init()
size = width, height = [int(i) for i in input().split()]
screen = pygame.display.set_mode(size)
pygame.draw.line(screen, pygame.Color('white'), (0, 0), (width, height), 5)
pygame.draw.line(screen, pygame.Color('white'), (0, height), (width, 0), 5)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
