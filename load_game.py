import itertools as it
import numpy as np
import pygame as pg

Colour = {True: (0, 0, 0), False: (255, 255, 255), None: (242, 176, 109)}
maskedGoban = np.ma.array(np.empty((19, 19)), dtype = 'bool', mask = True)

# Read .sgf
with open("-1.sgf", "r", encoding = "utf-8") as sgf_file:
    moves = iter([move for line in sgf_file for move in filter(None, line.strip().split(";")[1:])]) 

pg.init()

screen = pg.display.set_mode([500, 500])
screen.fill(Colour[None])

# Convert coords to screen pixels
def px(*ints):
    return 25 * (np.array(ints) + 1)

# Flip stones onto goban
def drawStones():
    screen.fill(Colour[None])
    # Goban
    for point in it.product(px(3, 9, 15), repeat = 2): 
        pg.draw.circle(screen, Colour[True], point, 5)
    for i in range(19):
        pg.draw.line(screen, Colour[True], px(i, 0), px(i, 18))
        pg.draw.line(screen, Colour[True], px(0, i), px(18, i))
    for point in it.product(range(19), repeat = 2):
        try:
            pg.draw.circle(screen, Colour[maskedGoban[point]], px(*point), 12)
            pg.draw.circle(screen, Colour[True], px(*point), 12, 1)
        except TypeError:
            pass
    pg.display.flip()

def libertyCount(colour, position, mask):
    print(colour, position)
    mask.append(tuple(position))
    for i in range(4):
        z = 1j**i
        adjacent = position + np.array([z.real, z.imag], dtype = int)
        try:
            if tuple(adjacent) in mask or min(adjacent) < 0:
                pass
            elif isinstance(maskedGoban[tuple(adjacent)], np.bool_):
                if maskedGoban[tuple(adjacent)] == colour: # Same colour
                    print(z, tuple(adjacent), maskedGoban[tuple(adjacent)], colour, 'same')
                    if libertyCount(colour, adjacent, mask):
                        return True
                # else: # Opposite
                #     print(z, tuple(adjacent), maskedGoban[tuple(adjacent)], colour, 'opposite')
            else: # Empty
                print(z, tuple(adjacent), maskedGoban[tuple(adjacent)], colour, 'empty')
                return True
        except IndexError:
            pass

def removeStones(position):
    for i in range(4):
        z = 1j**i
        try:
            adjacent = position + np.array([z.real, z.imag], dtype = int)
            if isinstance(maskedGoban[tuple(adjacent)], np.bool_) and (maskedGoban[tuple(position)] != maskedGoban[tuple(adjacent)]):
                if libertyCount(not maskedGoban[tuple(position)], adjacent, mask := []) is None:
                    print(mask)
                    for element in mask:
                        maskedGoban[element] = np.ma.masked
        except IndexError:
            pass

# Get next move from .sgf
def nextMove():
    try:
        move = next(moves)
        position = np.array([ord(move[2]) - 97, ord(move[3]) - 97])
        maskedGoban[tuple(position)] = (move[0] == "B")
        print("-----")
        removeStones(position)
    except StopIteration:
        pass
    
drawStones()
print(maskedGoban)

clock = pg.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                nextMove()
                drawStones()
        if event.type == pg.QUIT:
            running = False

pg.quit()