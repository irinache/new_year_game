import pygame


class Screen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("New Year Game")

    def get_screen(self):
        return self.screen

    def get_height(self):
        return self.screen.get_height()

    def get_width(self):
        return self.screen.get_width()

    def fill(self, color):
        self.screen.fill(color)



