import pygame


class Rect:
    def __init__(self, posit1, posit2):
        self.posit1 = posit1
        self.posit2 = posit2

    def get_coords(self):
        return self.posit1

    def get_size(self):
        return (self.posit2[0] - self.posit1[0], self.posit2[1] - self.posit1[1])


pygame.init()
screen = pygame.display.set_mode((501, 501))
running = True
down = False
otzhata = False
rects = []
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            down = True
            pos1 = event.pos
            pos2 = pos1
        if event.type == pygame.MOUSEBUTTONUP:
            otzhata = True
        if event.type == pygame.MOUSEMOTION:
            pos2 = event.pos
        if event.type == pygame.KEYDOWN:
            if event.mod == 64 and event.key == pygame.K_z:
                if rects:
                    rects.pop()
    for i in rects:
        pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(i.get_coords(), i.get_size()), 2)
    if down:
        pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(*pos1, pos2[0] - pos1[0], pos2[1] - pos1[1]), 2)
    if otzhata:
        otzhata = False
        down = False
        rects.append(Rect(pos1, pos2))
    pygame.display.flip()
pygame.quit()
