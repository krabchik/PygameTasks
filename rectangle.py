import pygame

pygame.init()
size = width, height = [int(i) for i in input().split()]
screen = pygame.display.set_mode(size)
pygame.draw.rect(screen, pygame.Color('red'), (1, 1, width - 2, height - 2))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()