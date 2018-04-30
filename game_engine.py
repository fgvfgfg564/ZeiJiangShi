import pygame
from player import *
from pygame.locals import *
import sys
from event import *
from game_functions import *
from servant import *
from hint import *
from cursor import *


class GameEngine:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.players = Players(settings, screen, self)
        self.ticker = pygame.time.Clock()

        self.hint_illustrator = HintIllustrator(settings, screen, self)
        self.cursor = NormalCursor(screen, self)

        self.mouse_position = (0, 0)
        self.current_item = Void()

    def run(self):
        pygame.mouse.set_visible(False)
        for i in range(3):
            self.players.list[0].summon_servant(ZhuYiChen)
            self.players.list[1].summon_servant(WangLiYuan)
        while True:
            self.check_event(self.get_event())
            self.update_screen()
            self.ticker.tick(self.settings.default_fps)

    def update_screen(self):
        # Update the screen
        self.screen.fill(self.settings.bg_color)

        # Draw players and servants
        self.players.blitme()

        #Draw hint
        self.hint_illustrator.blitme()

        # Draw cursor
        self.cursor.blitme()

        # Renew
        pygame.display.flip()

    def check_event(self, event):
        if isinstance(event, MouseClickItem):
            if event.key == 1:
                if isinstance(event.item, Void):
                    self.current_item = Void()
                else:
                    if isinstance(event.item, SERVANT_LIST):
                        self.current_item = event.item
            elif event.key == 3:
                if self.current_item == Void:
                    pass
                elif isinstance(event.item, SERVANT_LIST) or isinstance(event.item, Player):
                    self.current_item.moveto(event.item.location)
        elif isinstance(event, MouseMove):
            self.mouse_position = event.pos
        elif isinstance(event, KeyDown):
            if self.current_item == Void():
                pass
            else:
                self.current_item.prepare_attack()

    def get_event(self):
        return self.translate_event(pygame.event.poll())

    def translate_event(self, each):
        if each.type == QUIT:
            sys.exit()
        elif each.type == MOUSEBUTTONDOWN:
            pos = each.pos
            for player in self.players:
                if inside(pos, player.rect):
                    return MouseClickItem(each.button, player)
            for player in self.players:
                for servant in player.friendly_servants:
                    if inside(pos, servant.rect):
                        return MouseClickItem(each.button, servant)
            return MouseClickItem(each.button, Void())
        elif each.type == MOUSEMOTION:
            self.mouse_position = each.pos
            return MouseMove(each.pos[0], each.pos[1])
        elif each.type == KEYDOWN:
            return KeyDown(each.key)

    def get_target(self, legal):
        self.cursor = AttackCursor(self.screen, self)
        return_item = Void()
        while True:
            ev = self.get_event()
            if isinstance(ev, MouseClickItem):
                if ev.item == Void():
                    return_item = Void()
                    break
                elif legal(ev.item):
                    return_item = ev.item
                    break
                else:
                    self.hint_illustrator.illustrate("illegal_target")
            self.update_screen()
        self.cursor = NormalCursor(self.screen, self)
        return return_item