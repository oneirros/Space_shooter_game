"""Moduł łączący wszystkie elementy gry w całość."""
import sys
import random
import pygame

import constants
from spaceship import MotherShip
from spaceship import AlienShip
from menu import Menu


class Game:
    """Główna pętla gry."""
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("SpaceShooterGame")

        self.tps_max_alien = 75
        self.tps_max = 100
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.tps_delta_alien = 0.0

        self.player = MotherShip(
            self, constants.LOCATION_PLACE,
            constants.PLAYER_SHIP_WIDTH, constants.PLAYER_SHIP_HEIGHT)
        self.aliens = []

        self.menu = Menu(self)

        while True:
            self.menu.main_loop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.menu.pause_run = True

            self.tps_delta += self.tps_clock.tick() / 1000.0

            while self.tps_delta > 1 / self.tps_max:
                self.ticking()
                self.tps_delta = 0.0

            self.tps_delta_alien += self.tps_clock.tick() / 1000.0

            while self.tps_delta_alien > 1 / self.tps_max_alien:
                self.aliens.append(
                    AlienShip(self, [random.randint(15, constants.SCREEN_WIDTH - 50), -50], 50, 50))
                self.tps_delta_alien = 0.0
            self.score_label, _ = constants.Fonts.INFO_FONT.render(
                text="score = {}".format(self.player.score), fgcolor=constants.Colors.WHITE)
            self.screen.fill((0, 0, 0))
            self.drawing()
            if self.player.health == 0:
                self.__init__()
            pygame.display.flip()
            self.menu.pause_loop()
            self.tps_max_alien += 0.01

    def ticking(self) -> None:
        """Ticking."""
        self.player.control()
        for bullet in self.player.bullets:
            bullet.movement()

        for alien in self.aliens:
            alien.control()

            for bullet in alien.bullets:
                bullet.movement()

    def drawing(self) -> None:
        """Rysuje elementy głównej pętli oraz sprawdza kolizje."""

        self.screen.blit(constants.BG, (0, 0))
        self.player.drawing()

        for alien in self.aliens:
            alien.drawing()
            if alien.off_screen():
                self.aliens.remove(alien)
            for bullet in alien.bullets:
                if bullet.collide(self.player):
                    alien.bullets.remove(bullet)
                    self.player.health -= 10

            if alien.collision(self.player.position, self.player.mask):
                self.player.health -= 50
                self.aliens.remove(alien)

        for bullet in self.player.bullets:
            for alien in self.aliens:
                if bullet.collide(alien):
                    self.aliens.remove(alien)
                    self.player.bullets.remove(bullet)
                    self.player.score += 10

        self.score_label = self.score_label.convert_alpha()
        pos = self.score_label.get_rect(center=(65, 10))
        self.screen.blit(self.score_label, pos)


if __name__ == "__main__":
    Game()
