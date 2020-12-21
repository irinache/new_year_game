import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, screen, message, color, position_y, font_name, font_size):
        pygame.sprite.Sprite.__init__(self)

        # initialize image property
        self.image = pygame.Surface((screen.get_width(), 50), pygame.SRCALPHA)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() / 2, position_y)

        self.color = color
        self.message = message
        self.screen = screen
        self.font_name = font_name
        self.font_size = font_size
        self.position_y = position_y

        self.set_up_text()

    def set_up_text(self):
        text = pygame.font.Font('fonts/' + self.font_name + '.ttf', self.font_size)
        text_surf, text_rext = self.text_objects(self.message, text)
        text_rext.center = (self.screen.get_width() / 2, self.position_y)
        self.screen.blit(text_surf, text_rext)

    def text_objects(self, text, font):
        text_surface = font.render(text, True, self.color)
        return text_surface, text_surface.get_rect()
