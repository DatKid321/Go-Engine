import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen.fill((220, 177, 108))

for i in range(1, 20):
    pygame.draw.line(screen, (0, 0, 0), (25*i, 25*1), (25*i, 25*19))
    pygame.draw.line(screen, (0, 0, 0), (25*1, 25*i), (25*19, 25*i))

with open("-1.sgf", "r") as sgf_file:
    print("hi")
    for line in sgf_file:
        print(line)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

