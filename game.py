import pygame
import sys
from spaceship import MotherShip


class Game(object):
    def __init__(self):
        pygame.init()
        self.tps_max = 40
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("SpaceShooterGame")
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
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RIGHT]:
        #     rectangle.x += 5
        # elif keys[pygame.K_LEFT]:
        #     rectangle.x -= 5
        # elif keys[pygame.K_DOWN]:
        #     rectangle.y += 5
        # elif keys[pygame.K_UP]:
        #     rectangle.y -= 5

        self.player.control()



    def drawing(self):
        self.player.drawing()




if __name__ == "__main__":
    Game()


