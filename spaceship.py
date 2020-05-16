import pygame
from pygame.math import Vector2
import sys
from bullet import Bullet
import copy

class MotherShip(object):
    def __init__(self, game):
        self.game = game

        self.position = [Vector2(600.0, 600.0), Vector2(625.0, 550.0), Vector2(650.0, 600.0)]
        self.velocity = [Vector2(0.0, 0.0), Vector2(0.0, 0.0), Vector2(0.0, 0.0)]
        self.bullets = []



    def drawing(self):

        #create mother ship
        pygame.draw.polygon(self.game.screen, (20, 234, 129), self.position)
        for bullet in self.bullets:
            bullet.drawing()
            self.remove_bullet(bullet)



    def control(self):

        # control the ship with arrows
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.velocity = [vector + Vector2(0.0, -0.5)for vector in self.velocity]

        if pressed_key[pygame.K_DOWN]:
            self.velocity = [vector + Vector2(0.0, 0.5) for vector in self.velocity]

        if pressed_key[pygame.K_LEFT]:
            self.velocity = [vector + Vector2(-0.5, 0.0) for vector in self.velocity]

        if pressed_key[pygame.K_RIGHT]:
            self.velocity = [vector + Vector2(0.5, 0.0) for vector in self.velocity]

        if pressed_key[pygame.K_z] and len(self.bullets) < 1:
            self.shooting()

        # gravity
        if not pressed_key[pygame.K_UP]:
            self.velocity = [vector + Vector2(0.0, 0.5) for vector in self.velocity]

        # bounce off the wall
        if self.position[1].y <= 15.0:
            self.velocity = [vector + Vector2(0.0, 10.0) for vector in self.velocity]
        elif self.position[0].x <= 15.0:
            self.velocity = [vector + Vector2(10.0, 0.0) for vector in self.velocity]
        elif self.position[2].x > self.game.SCREEN_WIDTH - 15.0:
            self.velocity = [vector + Vector2(-10.0, 0.0) for vector in self.velocity]

        # velocity of the ship
        self.position = [vector_1 + vector_2 for vector_1, vector_2 in zip(self.velocity, self.position)]

    def shooting(self):
        bullet = Bullet(self.game, self.position[1], 5, True)
        self.bullets.append(bullet)

    def remove_bullet(self, bullet):
        if bullet.position.y < 0.0 or bullet.position.y > self.game.HEIGHT:
            self.bullets.remove(bullet)















