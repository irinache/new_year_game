import pygame

from new_year_game.tree import Tree


class Santa(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # initialize image property
        self.image = pygame.Surface((30, 45), pygame.SRCALPHA)
        self.image = pygame.image.load("images/santa.png")
        self.image = pygame.transform.scale(self.image, (30, 45))
        # self.image.fill(color)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0

        self.screen = screen
        self.speed = 5

    #todo optimize solution
    def update(self, keys, field):
        if self.rect.left < (self.screen.get_width() - self.image.get_width()) and keys[2]:
            self.rect.x += self.speed
            if self.check_collision(field):
                self.rect.x -= self.speed
        if self.rect.top > 0 and keys[0]:
            self.rect.y -= self.speed
            if self.check_collision(field):
                self.rect.y += self.speed
        if self.rect.top < (self.screen.get_playable_height() - self.image.get_height()) and keys[1]:
            self.rect.y += self.speed
            if self.check_collision(field):
                self.rect.y -= self.speed
        if self.rect.left > 0 and keys[3]:
            self.rect.x -= self.speed
            if self.check_collision(field):
                self.rect.x += self.speed

    def check_collision(self, sprite_set):
        for s in sprite_set:
            if isinstance(s, Tree):
                hits = pygame.sprite.collide_rect(s, self)
                if hits:
                    return True


