import pygame


class Tree(pygame.sprite.Sprite):
    def __init__(self, i, j):
        super().__init__()

        # initialize image property
        self.image = pygame.Surface((35, 50), pygame.SRCALPHA)
        self.image = pygame.image.load("images/christmas_tree.png")
        self.image = pygame.transform.scale(self.image, (35, 50))

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.top = i*50
        self.rect.left = j*50
