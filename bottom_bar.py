import pygame

from new_year_game.colors import WHITE
from new_year_game.text import Text


class BottomBar(pygame.sprite.Sprite):
    def __init__(self, screen, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        # initialize image property
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = 570

        self.color = color
        self.screen = screen
        self.lives_label = None
        self.lives_count = None
        self.prize_label = None
        self.prize_count = None

    def set_text(self):
        self.lives_label = Text(self.screen, "Lives:", WHITE, 520, 30, "Montserrat-Regular", 16, "l")
        self.lives_count = Text(self.screen, "5", WHITE, 520, 150, "Montserrat-Regular", 16, "l")

        self.prize_label = Text(self.screen, "Prizes:", WHITE, 540, 30, "Montserrat-Regular", 16, "l")
        self.prize_count = Text(self.screen, "0", WHITE, 540, 150, "Montserrat-Regular", 16, "l")

    def set_lives_count(self, count):
        self.lives_count = count

    def set_prize_count(self, count):
        self.prize_count = count

    def update(self, keys, field):
        self.image.fill(self.color)
        self.set_text()


