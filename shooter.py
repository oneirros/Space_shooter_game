import pygame
import sys

max_tps = 40

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("SpaceShooterGame")
rectangle = pygame.Rect(20, 40, 100, 100)
clock = pygame.time.Clock()
delta = 0.0

while True:
    # Ticking

    keys = pygame.key.get_pressed()
    delta += clock.tick() / 1000.0

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            rectangle.x += 1

    #inputs

    while delta > 1/max_tps:

        if keys[pygame.K_RIGHT]:
            rectangle.x += 5
        elif keys[pygame.K_LEFT]:
            rectangle.x -= 5
        elif keys[pygame.K_DOWN]:
            rectangle.y += 5
        elif keys[pygame.K_UP]:
            rectangle.y -= 5
        delta = 0.0


    # Drowing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (20, 50, 145), rectangle)
    pygame.display.flip()









