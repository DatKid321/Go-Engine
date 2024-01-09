import itertools as it
import numpy as np
import pygame as pg

Colour = {True: (0, 0, 0), False: (255, 255, 255), None: (242, 176, 109)}
maskedGoban = np.ma.array(np.empty((19, 19)), dtype = 'bool', mask = True)

# Read .sgf
with open("-1.sgf", "r") as sgf_file:
    moves = iter([move for line in sgf_file for move in filter(None, line.strip().split(";")[1:])]) 

pg.init()

screen = pg.display.set_mode([500, 500])
screen.fill(Colour[None])

# Convert coords to screen pixels
def px(*ints):
    return 25 * (np.array(ints) + 1)

# Flip stones onto goban
def drawStones():
    for point in it.product(range(19), repeat = 2):
        try:
            pg.draw.circle(screen, Colour[maskedGoban[point]], px(*point), 12)
            pg.draw.circle(screen, Colour[True], px(*point), 12, 1)
        except TypeError:
            pass
    pg.display.flip()

def libertyCount(bool, position):
    print(bool, maskedGoban[tuple(position)])

def removeStones(position):
    for i in range(4):
        z = 1j**i
        libertyCount(~maskedGoban[tuple(position)], position + np.array([z.real, z.imag], dtype = int))

# Get next move from .sgf
def nextMove():
    try:
        move = next(moves)
        position = np.array([ord(move[2]) - 97, ord(move[3]) - 97])
        maskedGoban[tuple(position)] = (move[0] == "B")
        removeStones(position)
        drawStones()
    except StopIteration:
        pass

# Goban
for point in it.product(px(3, 9, 15), repeat = 2): 
    pg.draw.circle(screen, Colour[True], point, 5)
for i in range(19):
    pg.draw.line(screen, Colour[True], px(i, 0), px(i, 18))
    pg.draw.line(screen, Colour[True], px(0, i), px(18, i))
    
drawStones()
print(maskedGoban)

pg.display.flip()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                nextMove()
        if event.type == pg.QUIT:
            running = False

pg.quit()