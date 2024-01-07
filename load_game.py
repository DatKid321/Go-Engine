import itertools
import numpy
import pygame

Colour = {"B": (0, 0, 0), "W": (255, 255, 255), "G": (242, 176, 109)}
Goban = numpy.zeros((19, 19), dtype = 'bool')
maskedGoban = numpy.ma.masked_array(Goban, mask = numpy.ones((19, 19)))

def px(*ints):
    return tuple(25 * int for int in ints)

print(px(1,2), 'hello')
print([point for point in itertools.product(px(4, 10, 16), repeat = 2)])

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen.fill(Colour["G"])

for point in itertools.product(px(4, 10, 16), repeat = 2): pygame.draw.circle(screen, Colour["B"], point, 5)
for i in range(1, 20):
    pygame.draw.line(screen, Colour["B"], px(i, 1), px(i, 19))
    pygame.draw.line(screen, Colour["B"], px(1, i), px(19, i))

with open("-1.sgf", "r") as sgf_file:
    for line in sgf_file:
        for move in filter(None, line.strip().split(";")[1:]):
            # Goban[ord(move[2]) - 96][ord(move[3]) - 96] += 1
            position = (25 * (ord(move[2]) - 96), 25 * (ord(move[3]) - 96))
            pygame.draw.circle(screen, Colour[move[0]], position, 12)
            pygame.draw.circle(screen, Colour["B"], position, 12, 1)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()