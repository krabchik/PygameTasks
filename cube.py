import pygame


def change_col(color):
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] - 25, hsv[3])
    return color


w, hue = [int(i) for i in input().split()]
x_out, y_out = int(150 - 0.75 * w), int(150 - 0.75 * w)
x_in, y_in = int(150 - 0.25 * w), int(150 - 0.25 * w)
pygame.init()
screen = pygame.display.set_mode((300, 300))
col = pygame.Color('red')
hsv = col.hsva
col.hsva = (hue, hsv[1], hsv[2], hsv[3])

pygame.draw.polygon(screen, col, [[x_in, y_out], [300 - x_out, y_out], [300 - x_in, y_in], [x_out, y_in]])
col = change_col(col)
pygame.draw.polygon(screen, col, [[x_out, y_in], [300 - x_in, y_in], [300 - x_in, 300 - y_out], [x_out, 300 - y_out]])
col = change_col(col)
pygame.draw.polygon(screen, col, [[300 - x_in, y_in], [300 - x_in, 300 - y_out], [300 - x_out, 300 - y_in],
                                  [300 - x_out, y_out]])

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()