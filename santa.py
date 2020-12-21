import pygame


class Santa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # initialize image property
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load("images/santa.png")
        # self.image.fill(color)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0
