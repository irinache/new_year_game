import pygame


class Prize(pygame.sprite.Sprite):
    def __init__(self, i, j):
        super().__init__()

        # initialize image property
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.image = pygame.image.load("images/prize.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.top = i * 50 + 10
        self.rect.left = j * 50 + 10


