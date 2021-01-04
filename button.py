import pygame
from new_year_game.text import Text


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, message, color, hover_color, text_color, position_y, width, height, action=None):
        pygame.sprite.Sprite.__init__(self)

        # initialize image property
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_screen().get_width() / 2, position_y)

        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action
        self.message = message
        self.screen = screen
        self.position_y = position_y
        self.position_x = 0
        self.text = Text(self.screen, self.message, self.text_color, self.position_y, self.position_x,
                         "Montserrat-Regular", 16, "c")

    def set_text(self):
        self.text = Text(self.screen, self.message, self.text_color, self.position_y, self.position_x,
                         "Montserrat-Regular", 16, "c")

    def update(self):
        # get mouse position
        mouse = pygame.mouse.get_pos()
        # get click event
        click = pygame.mouse.get_pressed()

        # if mouse hover button
        if self.rect.collidepoint(mouse):
            self.image.fill(self.hover_color)
            # if clicked do action
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            self.image.fill(self.color)
        self.set_text()
