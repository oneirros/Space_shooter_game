"""Stałe potrzebne w programie."""
import os

import pygame.freetype

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 800
LOCATION_PLACE = [320, 400]
PLAYER_SHIP_WIDTH = 75
PLAYER_SHIP_HEIGHT = 75
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("/Users/kuba/Documents/Python/shooter_game/images", "spacebg.jpg")),
    (SCREEN_WIDTH, SCREEN_HEIGHT))


class Fonts:
    """Czcionki."""
    pygame.init()
    pygame.font.init()
    INFO_FONT = pygame.freetype.SysFont("Courier", 20, bold=True)
    MENU_FONT = pygame.freetype.SysFont("Courier", 30, bold=True)
    MENU_FONT_HIGHLIGHT = pygame.freetype.SysFont("Courier", 30 * 1.20, bold=True)


class Colors:
    """Paleta barw."""
    WHITE = (255, 255, 255)
