import pygame
from game_functions import *
import math


class Servant:
    def __init__(self, settings, screen, master, engine, HP, damage, cost, name):
        self.HP_full = self.HP = HP
        self.damage = damage
        self.cost = cost
        self.master = master
        self.location = master
        self.settings = settings
        self.engine = engine

        self.image = pygame.image.load("image/" + name + ".png")
        self.image_browse = pygame.image.load("image/" + name + "_bright.png")
        self.select_mark = pygame.image.load("image/select_mark.png")
        self.screen = screen
        self.rect = self.image.get_rect()

    def prepare_attack(self):
        def legal(x):
            return x.location == self.location and x.master != self.master
        tg = self.engine.get_target(legal)
        if tg == Void():
            return
        else:
            self.attack(tg)


    def attack(self, target):
        target.gain_attack(self)

    def gain_attack(self, source):
        self.HP -= source.damage
        if self.HP <= 0:
            self.death()

    def blitme(self):
        # Draw the image
        if inside(self.engine.mouse_position, self.rect):
            self.screen.blit(self.image_browse, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

        # Draw HP bar
        single_bar_length = int(1 / self.HP_full * self.settings.HP_bar_length - 1)
        rect = pygame.Rect(self.rect.left - 1, self.rect.top - 1.5*self.settings.HP_bar_width - 1,
                           (single_bar_length + 1) * self.HP_full + 1, self.settings.HP_bar_width + 2)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
        for each in range(self.HP_full):
            rect = pygame.Rect(self.rect.left + each * (1 + single_bar_length), self.rect.top - 1.5*self.settings.HP_bar_width,
                                    single_bar_length, self.settings.HP_bar_width)
            pygame.draw.rect(self.screen, self.master.color if each < self.HP else self.settings.bg_color, rect)

        # Draw the select mark if it's selected
        if self.engine.current_item == self:
            rect2 = self.select_mark.get_rect()
            rect2.centerx = self.rect.centerx
            rect2.bottom = self.rect.top - self.settings.HP_bar_width
            self.screen.blit(self.select_mark, rect2)

    def moveto(self, new_location):
        old_location = self.location
        old_location.remove(self)
        self.location = new_location
        new_location.welcome(self)

    def death(self):
        master = self.master
        location = self.location
        master.friendly_servants.remove(self)
        location.remove(self)


class WangLiYuan(Servant):
    def __init__(self, settings, screen, master, engine):
        super().__init__(settings, screen, master, engine, 2, 2, 0, "wangliyuan")


class ZhuYiChen(Servant):
    def __init__(self, settings, screen, master, engine):
        super().__init__(settings, screen, master, engine, 4, 2, 1, "zhuyichen")


class XuTianYi(Servant):
    def __init__(self, settings, screen, master, engine):
        super().__init__(settings, screen, master, engine, 8, 2, 2, "xutianyi")


SERVANT_LIST = (Servant, WangLiYuan, XuTianYi)
