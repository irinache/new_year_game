import pygame
from new_year_game.colors import *


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, message, color, hover_color, position_x, position_y, width, height, action=None):
        pygame.sprite.Sprite.__init__(self)

        # initialize image property
        self.image = pygame.Surface((width, height))
        self.image.fill(color)


        # initialize rect property and sprite position
        self.rect = self.image.get_rect()
        self.rect.top = position_y
        self.rect.left = position_x

        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.message = message
        self.screen = screen

        self.set_text()

    # render text sprite
    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

    def set_text(self):
        start_button_text = pygame.font.Font('fonts/Montserrat-Regular.ttf', 16)
        button_text_surf, button_text_rect = self.text_objects(self.message, start_button_text)
        button_text_rect.center = (
        self.rect.left + (self.image.get_width() / 2), (self.rect.top + (self.image.get_height() / 2)))
        self.screen.blit(button_text_surf, button_text_rect)

    def update(self):
        # get mouse position
        mouse = pygame.mouse.get_pos()
        # get click event
        click = pygame.mouse.get_pressed()

        # if mouse hover button
        if self.rect.collidepoint(mouse):
            # draw rect with hover color
            self.image.fill(self.hover_color)
            # if clicked do action
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            self.image.fill(self.color)
        self.set_text()
