import pygame


class HintIllustrator:
    def __init__(self, settings, screen, engine):
        self.screen = screen
        self.settings = settings
        self.engine = engine
        self.active = False
        self.ticker = 0

    def illustrate(self, info):
        self.image = pygame.image.load("image/error/info_" + info + ".png")
        self.rect = self.image.get_rect()
        self.active = True
        self.ticker = self.settings.hint_duration

    def blitme(self):
        if self.active:
            self.rect.bottom = self.engine.mouse_position[1]
            self.rect.left = self.engine.mouse_position[0]
            self.screen.blit(self.image, self.rect)
            self.ticker -= 1
            if self.ticker == 0:
                self.active = False

