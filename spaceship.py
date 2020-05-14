import pygame
from pygame.math import Vector2

class MotherShip(object):
    def __init__(self, game):
        self.game = game

        self.position = Vector2(600.0, 650.0)
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = Vector2(0.0, 0.0)

    def control(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.position += Vector2(0, -5)
        if pressed_key[pygame.K_DOWN]:
            self.position += Vector2(0, 5)
        if pressed_key[pygame.K_LEFT]:
            self.position += Vector2(-5, 0)
        if pressed_key[pygame.K_RIGHT]:
            self.position += Vector2(5, 0)





    def drawing(self):
        motherShip = pygame.Rect(self.position.x, self.position.y, 50, 50)
        pygame.draw.rect(self.game.screen, (20, 50, 145), motherShip)
