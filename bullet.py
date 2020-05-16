import pygame
from pygame.math import Vector2


class Bullet:

    def __init__(self, game, position, speed, direction):
        self.game = game
        self.position = position
        self.speed = speed
        self.direction = direction

    def drawing(self):
        pygame.draw.rect(self.game.screen, (100, 50, 200), (self.position.x, self.position.y, 15, 30))

    def movement(self):

        if self.direction is True:
                self.position += Vector2(0.0, -self.speed)
        if self.direction is False:
                self.position += Vector2(0.0, self.speed)

