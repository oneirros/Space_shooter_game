import pygame
from pygame.math import Vector2
import sys
import os
from bullet import Bullet
import random


class Ship(object):
    def __init__(self, game, position, width, height):
        self.game = game
        self.position = position  # [x, y]
        self.width = width
        self.height = height
        self.velocity = [0, 0]
        self.image = None
        self.mask = None
        self.bullets = []


    def drawing(self):
        self.game.screen.blit(self.image, (self.position[0], self.position[1]))
        for bullet in self.bullets:
            bullet.drawing()
            self.remove_bullet(bullet)

    def control(self):
        pass

    def shooting(self, position, bullet_sped: float, up_or_down: bool):
        bullet = Bullet(self.game, position, bullet_sped, up_or_down)
        self.bullets.append(bullet)

    def remove_bullet(self, bullet):
        if bullet.position[1] < 0 or bullet.position[1] > self.game.SCREEN_HEIGHT:
            self.bullets.remove(bullet)

    def off_screen(self):
        if self.position[1] > self.game.SCREEN_HEIGHT:
            return True
        return False

    def collision(self):
        pass


class MotherShip(Ship):
    def __init__(self, game, position, width, height, health: float = 100):
        super().__init__(game, position, width, height)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("/Users/kuba/Documents/Python/shooter_game/images", "Mother_ship1.png")),
            (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
        self.sum_clock = 0.0
        self.clock = pygame.time.Clock()
        self.health = health

    def control(self):

        self.sum_clock += self.clock.tick() / 1000.0

        # control the ship with arrows
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.velocity[1] += -0.5
        if pressed_key[pygame.K_DOWN]:
            self.velocity[1] += 0.5
        if pressed_key[pygame.K_LEFT]:
            self.velocity[0] += -0.5
        if pressed_key[pygame.K_RIGHT]:
            self.velocity[0] += 0.5
        if pressed_key[pygame.K_z] and len(self.bullets) < 3 and self.sum_clock > 0.2:
            self.shooting([self.position[0] + 30, self.position[1]], 5, True)
            self.sum_clock = 0.0



        # gravity
        if not pressed_key[pygame.K_UP]:
            self.velocity[1] += 0.3

        # bounce off the wall
        if self.position[1] <= 15:
            self.velocity[1] += 10
        elif self.position[0] <= 2:
            self.velocity[0] += 10
        elif self.position[0] > self.game.SCREEN_WIDTH - 50:
            self.velocity[0] += -10

        # velocity of the ship
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def healthBar(self):
        pygame.draw.rect(self.game.screen, (255, 0, 0), (self.position[0], self.position[1] + self.height + 2,
                                                         self.width, 10))
        pygame.draw.rect(self.game.screen, (0, 255, 0), (self.position[0], self.position[1] + self.height + 2,
                                                         (self.width * self.health) / 100, 10))

    def drawing(self):
        super().drawing()
        self.healthBar()



class AlienShip(Ship):
    def __init__(self, game, position, width, height):
        super().__init__(game, position, width, height)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("/Users/kuba/Documents/Python/shooter_game/images", "Alien_ship.png")),
            (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)

    def control(self):
        self.position[1] += 1
        if random.randrange(0, 120) == 1:
            self.shooting([self.position[0] + 20, self.position[1] + 40], 5, False)





