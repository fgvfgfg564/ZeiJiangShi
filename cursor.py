import pygame


class Cursor:
    def __init__(self, screen, engine, image):
        self.screen = screen
        self.engine = engine
        self.image = pygame.image.load("image/cursor/" + image + ".png")
        self.rect = self.image.get_rect()

    def blitme(self):
        self.rect.center = self.engine.mouse_position
        self.screen.blit(self.image, self.rect)


class AttackCursor(Cursor):
    def __init__(self, screen, engine):
        super().__init__(screen, engine, "attack")


class NormalCursor(Cursor):
    def __init__(self, screen, engine):
        super().__init__(screen, engine, "normal")

    def blitme(self):
        self.rect.top = self.engine.mouse_position[1]
        self.rect.left = self.engine.mouse_position[0]
        self.screen.blit(self.image, self.rect)