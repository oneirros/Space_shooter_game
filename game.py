import pygame
import sys
from spaceship import MotherShip
from bullet import Bullet
from pygame.math import Vector2
import os


class Game(object):
    def __init__(self):
        self.SCREEN_WIDTH, self.HEIGHT = 1280, 720
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join("/Users/kuba/Documents/Python/shooter_game/images", "Shooter_game_BG.jpg")), (self.SCREEN_WIDTH, self.HEIGHT))
        pygame.init()
        pygame.font.init()
        self.main_font = pygame.font.SysFont("comicsans", 30)
        self.tps_max = 40

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.HEIGHT))
        pygame.display.set_caption("SpaceShooterGame")
        self.level_label = self.main_font.render("level", 1, (255, 255, 255))

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.player = MotherShip(self)




        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)


            self.tps_delta += self.tps_clock.tick() / 1000.0

            while self.tps_delta > 1 / self.tps_max:
                self.ticking()
                self.tps_delta -= 1 / self.tps_max


            self.screen.fill((0, 0, 0))
            self.drawing()
            pygame.display.flip()

    def ticking(self):

        self.player.control()
        for bullet in self.player.bullets:
            bullet.movement()


    def drawing(self):
        self.screen.blit(self.BG, (0, 0))
        self.player.drawing()
        self.screen.blit(self.level_label, (1, 1))











if __name__ == "__main__":
    Game()


