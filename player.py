import pygame
import math


class Player:
    def __init__(self, settings, screen, number, engine, face_dir):
        self.HP_full = self.HP = settings.player_HP
        self.settings = settings
        self.number = number
        self.color = self.settings.player_color[number - 1]
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.engine = engine
        self.face_dir = face_dir
        self.location = self.master = self

        self.image = pygame.image.load("image/player_3.png")
        self.rect = self.image.get_rect()
        self.local_servants = []
        self.enemy_servants = []
        self.friendly_servants = []

    def summon_servant(self, Servant):
        # Summon a certain servant

        servant = Servant(self.settings, self.screen, self, self.engine)
        self.local_servants.append(servant)
        self.adjust_position()
        self.friendly_servants.append(servant)

    def adjust_position(self):
        # Adjust the friendly and hostile servants in two circles

        horizonal = (self.face_dir[1], -self.face_dir[0])

        l1 = len(self.local_servants)
        cx = 0
        for each in self.local_servants:
            delta = (l1 - 1) / 2 - cx
            each.rect.centerx = self.rect.centerx + self.settings.friendly_servant_radius \
                                * self.face_dir[0] + delta * horizonal[0] * self.settings.servant_interval
            each.rect.centery = self.rect.centery + self.settings.friendly_servant_radius \
                                * self.face_dir[1] + delta * horizonal[1] * self.settings.servant_interval
            cx += 1

        l1 = len(self.enemy_servants)
        a1 = math.pi
        cx = 0
        for each in self.enemy_servants:
            delta = (l1 - 1) / 2 - cx
            each.rect.centerx = self.rect.centerx + self.settings.hostile_servant_radius \
                                * self.face_dir[0] + delta * horizonal[0] * self.settings.servant_interval
            each.rect.centery = self.rect.centery + self.settings.hostile_servant_radius \
                                * self.face_dir[1] + delta * horizonal[1] * self.settings.servant_interval
            cx += 1

    def blitme(self):
        # Draw the player and its servants on the screen
        self.screen.blit(self.image, self.rect)

        # Draw HP bar
        single_bar_length = int(1 / self.HP_full * self.rect.width - 1)
        rect = pygame.Rect(self.rect.left - 1, self.rect.top - 1.5*self.settings.HP_bar_width - 1,
                           (single_bar_length + 1) * self.HP_full + 1, self.settings.HP_bar_width + 2)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
        for each in range(self.HP_full):
            rect = pygame.Rect(self.rect.left + each * (1 + single_bar_length), self.rect.top - 1.5*self.settings.HP_bar_width,
                                    single_bar_length, self.settings.HP_bar_width)
            pygame.draw.rect(self.screen, self.color if each < self.HP else self.settings.bg_color, rect)

        for each in self.local_servants:
            each.blitme()
        for each in self.enemy_servants:
            each.blitme()

    def remove(self, servant):
        if servant in self.local_servants:
            self.local_servants.remove(servant)
        elif servant in self.enemy_servants:
            self.enemy_servants.remove(servant)
        self.adjust_position()

    def welcome(self, servant):
        if servant.master == self:
            self.local_servants.append(servant)
        else:
            self.enemy_servants.append(servant)
        self.adjust_position()

    def update_image(self):
        s = str(self.HP // 2)
        self.image = pygame.image.load("image/player_" + s + ".png")

    def gain_attack(self, source):
        self.HP -= source.damage
        self.update_image()


class Players:
    def __init__(self, settings, screen, engine):
        self.size = settings.player_amount
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.engine = engine
        self.list = []

        a1 = 0
        for i in range(self.size):
            each = Player(settings, screen, i+1, engine, (-math.cos(a1), -math.sin(a1)))
            each.rect.centerx = self.screen_rect.centerx + settings.player_radius * math.cos(a1)
            each.rect.centery = self.screen_rect.centery + settings.player_radius * math.sin(a1)
            self.list.append(each)
            a1 += 2 * math.pi / self.size

    def blitme(self):
        for each in self.list:
            each.blitme()

    def __iter__(self):
        return self.list.__iter__()
