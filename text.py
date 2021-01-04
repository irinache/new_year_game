import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, screen, message, color, position_y, position_x, font_name, font_size, alignment):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.message = message
        self.screen = screen
        self.font_name = font_name
        self.font_size = font_size
        self.position_y = position_y
        self.position_x = position_x
        self.alignment = alignment

        # initialize image property
        self.image = pygame.Surface((screen.get_width(), 50), pygame.SRCALPHA)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() / 2, position_y)


        self.set_up_text()

    def set_up_text(self):
        text = pygame.font.Font('fonts/' + self.font_name + '.ttf', self.font_size)
        text_surf, text_rect = self.text_objects(self.message, text)
        if self.alignment == "c":
            text_rect.center = (self.screen.get_screen().get_width() / 2, self.position_y)
        elif self.alignment == "l":
            text_rect.left = self.position_x
            text_rect.top = self.position_y

        self.screen.get_screen().blit(text_surf, text_rect)

    def text_objects(self, text, font):
        text_surface = font.render(text, True, self.color)
        return text_surface, text_surface.get_rect()
