import sys
import pygame

from servant import *
from settings import *
from player import *
from game_functions import *
from game_engine import *


def game_start():
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('ZeiJiangShi')
    engine = GameEngine(settings, screen)
    engine.run()




game_start()

