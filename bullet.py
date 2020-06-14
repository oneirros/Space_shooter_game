"""Moduł odpowiedzialny za pociski"""
import os
import copy
import pygame


class Bullet:
    """Klasa odpowiedzialna za tworzenie pocisku"""
    def __init__(self, game, position, speed, direction: bool):
        self.game = game
        self.position = copy.copy(position)
        self.speed = speed
        self.direction = direction
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            "/Users/kuba/Documents/Python/shooter_game/images", "bullet.png")), (15, 20))
        self.mask = pygame.mask.from_surface(self.image)

    def drawing(self):
        """Rysuje pocisk"""
        self.game.screen.blit(self.image, (self.position[0], self.position[1]))

    def movement(self):
        """Metoda odpowiedzialna za ruch pocisku"""
        if self.direction is True:
            self.position[1] += -self.speed
        if self.direction is False:
            self.position[1] += self.speed

    def collide(self, alien_ship):
        """Sprawdza czy pocisk koliduje z innym obiektem"""
        offset_x = alien_ship.position[0] - self.position[0]
        offset_y = alien_ship.position[1] - self.position[1]
        return self.mask.overlap(alien_ship.mask, (int(offset_x), int(offset_y)))
