import itertools as iter
import numpy as np
import pygame as pg

Colour = {"B": (0, 0, 0), "W": (255, 255, 255), "G": (242, 176, 109)}
Goban = np.zeros((19, 19), dtype = 'bool')
maskedGoban = np.ma.masked_array(Goban, mask = np.ones((19, 19)))

def px(*ints):
    return 25 * np.array(ints)

print(px(1,2), 'hello')
print([point for point in iter.product(px(4, 10, 16), repeat = 2)])

pg.init()

screen = pg.display.set_mode([500, 500])
screen.fill(Colour["G"])

for point in iter.product(px(4, 10, 16), repeat = 2): pg.draw.circle(screen, Colour["B"], point, 5)
for i in range(1, 20):
    pg.draw.line(screen, Colour["B"], px(i, 1), px(i, 19))
    pg.draw.line(screen, Colour["B"], px(1, i), px(19, i))

with open("-1.sgf", "r") as sgf_file:
    for line in sgf_file:
        for move in filter(None, line.strip().split(";")[1:]):
            # Goban[ord(move[2]) - 96][ord(move[3]) - 96] += 1
            position = (25 * (ord(move[2]) - 96), 25 * (ord(move[3]) - 96))
            pg.draw.circle(screen, Colour[move[0]], position, 12)
            pg.draw.circle(screen, Colour["B"], position, 12, 1)

pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()