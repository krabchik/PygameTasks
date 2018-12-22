import pygame


def col_reverse(uslovie):
    if uslovie:
        return 'black'
    return 'white'


pygame.init()
size = w, n = [int(i) for i in input().split()]
screen = pygame.display.set_mode((w, w))
col = col_reverse(n % 2)
dlina = int(w / n)
for i in range(n):
    first_col = col
    for j in range(n):
        screen.fill(pygame.Color(col), (j * dlina, i * dlina, dlina, dlina))
        col = col_reverse(col == 'white')
    col = col_reverse(first_col == 'white')
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
