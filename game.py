import pygame
import sys
from spaceship import MotherShip
from spaceship import AlienShip
from bullet import Bullet
from pygame.math import Vector2
import os
import random
import main_menu



class Game(object):
    def __init__(self):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 700, 1000
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join("/Users/kuba/Documents/Python/shooter_game/images", "spacebg.jpg")), (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.init()
        pygame.font.init()
        self.main_font = pygame.font.SysFont("comicsans", 30)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("SpaceShooterGame")
        self.level_label = self.main_font.render("level", 1, (255, 255, 255))

        self.tps_max_alien = 75
        self.tps_max = 100
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.tps_delta_alien = 0.0

        self.player = MotherShip(self, [600, 500], 75, 75)
        self.aliens = []

        while True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            self.tps_delta += self.tps_clock.tick() / 1000.0

            while self.tps_delta > 1 / self.tps_max:
                self.ticking()
                self.tps_delta = 0.0

            self.tps_delta_alien += self.tps_clock.tick() / 1000.0

            while self.tps_delta_alien > 1 / self.tps_max_alien:
                self.aliens.append(AlienShip(self, [random.randint(15, self.SCREEN_WIDTH - 50), -50], 50, 50))
                self.tps_delta_alien = 0.0

            self.screen.fill((0, 0, 0))
            self.drawing()
            pygame.display.flip()
            self.tps_max_alien += 0.005

    def ticking(self):

        self.player.control()
        for bullet in self.player.bullets:
            bullet.movement()

        for alien in self.aliens:
            alien.control()

            for bullet in alien.bullets:
                bullet.movement()

    def drawing(self):
        self.screen.blit(self.BG, (0, 0))
        self.player.drawing()

        for alien in self.aliens:
            alien.drawing()
            if alien.off_screen():
                self.aliens.remove(alien)
            for bullet in alien.bullets:
                if bullet.collide(self.player):
                    alien.bullets.remove(bullet)
                    self.player.health -= 10


        for bullet in self.player.bullets:
            for alien in self.aliens:
                if bullet.collide(alien):
                    self.aliens.remove(alien)
                    self.player.bullets.remove(bullet)

        self.screen.blit(self.level_label, (1, 1))

if __name__ == "__main__":
    Game()


