import pygame


class Santa(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # initialize image property
        self.image = pygame.Surface((35, 50), pygame.SRCALPHA)
        self.image = pygame.image.load("images/santa.png")
        self.image = pygame.transform.scale(self.image, (35, 50))
        # self.image.fill(color)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0

        self.screen = screen

    def update(self, keys):
        if self.rect.left <= (self.screen.get_width() - self.image.get_width()) and keys[2]:
            self.rect.x += 5
        if keys[0]:
            self.rect.y -= 5
        elif keys[1]:
            self.rect.y += 5
        elif keys[3]:
            self.rect.x -= 5


