import pygame
pygame.init()

with open("-1.sgf", "r") as sgf_file:
    print("hi")
    for line in sgf_file:
        print(line)

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 204, 170))
    pygame.display.flip()

pygame.quit()

