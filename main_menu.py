import pygame
import pygame.freetype
import sys
class Menu(object):
    def __init__(self, game):
        self.game = game
        self.run = True
        self.white = (255, 255, 255)
        self.mouse_over = False
        self.center_position = (350, 250)
        self.font_size = 30
        self.menu_font = pygame.freetype.SysFont("Courier", self.font_size, bold=True )
        self.button = None

    def mainLoop(self):
        while self.run:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.run = False

            self.game.screen.blit(self.game.BG, (0, 0))
            self.drawing()

            if self.buttonPressed():
                self.run = False
            pygame.display.flip()

    def createButton(self, text, text_color, font_size):
        menu_font = pygame.freetype.SysFont("Courier", font_size, bold=True)
        button, _ = menu_font.render(text=text, fgcolor=text_color)
        button = button.convert_alpha()
        button_rect = button.get_rect(center=self.center_position)

        return button,  button_rect

    def whichButton(self):
        button = self.createButton("play", self.white, self.font_size)
        highlightet_button = self.createButton("play", self.white, self.font_size * 1.25)
        return (highlightet_button[0], highlightet_button[1]) if self.mouse_over else (button[0], button[1])
    def updateMousePos(self):
        if self.button[1].collidepoint(pygame.mouse.get_pos()):
            self.mouse_over = True
            return True
        else:
            self.mouse_over = False
        return False
    def buttonPressed(self):
        if self.button[1].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
           return True
        return False



    def pauseLoop(self):
        pass

    def pause(self):
        pass

    def drawing(self):
        self.button = self.whichButton()
        self.game.screen.blit(self.button[0], self.button[1])
        self.updateMousePos()





