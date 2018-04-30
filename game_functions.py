import pygame
import sys
from pygame.locals import *


def inside(pos, rect):
    return rect.left < pos[0] < rect.right and rect.top < pos[1] < rect.bottom


class Void:
    def __eq__(self, other):
        return type(self) == type(other)