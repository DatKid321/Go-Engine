import itertools as it
import numpy as np
import os
import pygame as pg
import random as rd

Colour = {True: (0, 0, 0), False: (255, 255, 255), None: (242, 176, 109)}
masked_goban = np.ma.array(np.empty((19, 19)), dtype = 'bool', mask = True)
clock = pg.time.Clock()

# Define directory 
user_db = "/Users/olivertan/Desktop/Go/sgfs/BadukMovies Collection"

# Random file
random_sgf = user_db + "/" + rd.choice(os.listdir(user_db))

print(random_sgf)

# Read .sgf
with open(random_sgf, "r", encoding = "utf-8") as sgf_file:
    moves = iter([move for line in sgf_file for move in filter(None, line.strip().split(";")[1:]) if line[0] == ";"]) 

pg.init()

screen = pg.display.set_mode([500, 600])
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
            pg.draw.circle(screen, Colour[masked_goban[point]], px(*point), 12)
            pg.draw.circle(screen, Colour[True], px(*point), 12, 1)
        except TypeError:
            pass
    pg.display.flip()

# Remove stones if they have no liberties
def libertyCount(colour, position, mask):
    print(colour, position)
    mask.append(tuple(position))
    for i in range(4):
        z = 1j**i
        adjacent = position + np.array([z.real, z.imag], dtype = int)
        try:
            if tuple(adjacent) in mask or min(adjacent) < 0:
                pass
            elif isinstance(masked_goban[tuple(adjacent)], np.bool_):
                if masked_goban[tuple(adjacent)] == colour: # Same colour
                    print(z, tuple(adjacent), masked_goban[tuple(adjacent)], colour, 'same')
                    if libertyCount(colour, adjacent, mask):
                        return True
                # else: # Opposite
                #     print(z, tuple(adjacent), masked_goban[tuple(adjacent)], colour, 'opposite')
            else: # Empty
                print(z, tuple(adjacent), masked_goban[tuple(adjacent)], colour, 'empty')
                return True
        except IndexError:
            pass

# Count liberties of adjacent opposing stones
def removeStones(position):
    for i in range(4):
        z = 1j**i
        try: 
            adjacent = position + np.array([z.real, z.imag], dtype = int)
            if min(adjacent) > 0 and isinstance(masked_goban[tuple(adjacent)], np.bool_) and (masked_goban[tuple(position)] != masked_goban[tuple(adjacent)]):
                if libertyCount(not masked_goban[tuple(position)], adjacent, mask := []) is None:
                    print(mask)
                    for element in mask:
                        masked_goban[element] = np.ma.masked
        except IndexError:
            pass

# Get next move from .sgf
def nextMove():
    try:
        move = next(moves)
        position = np.array([ord(move[2]) - 97, ord(move[3]) - 97])
        masked_goban[tuple(position)] = (move[0] == "B")
        print("-----")
        removeStones(position)
    except StopIteration:
        pass
    
drawStones()
print(masked_goban)

running = True
while running:
    clock.tick(60)
    nextMove()
    drawStones()
    for event in pg.event.get():
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_SPACE:
        #         nextMove()
        #         drawStones()
        if event.type == pg.QUIT:
            running = False

pg.quit()