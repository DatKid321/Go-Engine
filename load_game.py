import pygame

Colour = {"B" : (0, 0, 0), "W" : (255, 255, 255)}

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen.fill((220, 177, 108))

for i in range(1, 20):
    pygame.draw.line(screen, Colour["B"], (25 * i, 25 * 1), (25 * i, 25 * 19))
    pygame.draw.line(screen, Colour["B"], (25 * 1, 25 * i), (25 * 19, 25 * i))

with open("-1.sgf", "r") as sgf_file:
    for line in sgf_file:
        for move in filter(None, line.strip().split(";")[1:]):
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

