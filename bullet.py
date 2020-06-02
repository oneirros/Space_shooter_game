import pygame
from pygame.math import Vector2
import copy
import os


class Bullet:

    def __init__(self, game, position, speed, direction: bool):
        self.game = game
        self.position = copy.copy(position)
        self.speed = speed
        self.direction = direction
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("/Users/kuba/Documents/Python/shooter_game/images", "bullet.png")), (15, 20))
        self.mask = pygame.mask.from_surface(self.image)

    def drawing(self):

        self.game.screen.blit(self.image, (self.position[0], self.position[1]))

    def movement(self):

        if self.direction is True:
            self.position[1] += -self.speed
        if self.direction is False:
            self.position[1] += self.speed

    def collide(self, alienShip):
        offset_x = alienShip.position[0] - self.position[0]
        offset_y = alienShip.position[1] - self.position[1]
        return self.mask.overlap(alienShip.mask, (int(offset_x), int(offset_y)))
