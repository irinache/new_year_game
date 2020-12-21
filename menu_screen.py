from new_year_game.button import Button
from new_year_game.colors import *
from new_year_game.screen import Screen


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()

        self.start_button = None
        self.quit_button = None

    def draw_buttons(self, start_action, quit_action):
        # buttons params
        height = 40
        width = 120

        start_button_y = 130
        quit_button_y = 190

        # create buttons
        self.start_button = Button(self.screen, "Start game", BUTTON, BUTTON_HOVER, BLACK,
                                   start_button_y, width, height, start_action)
        self.quit_button = Button(self.screen, "Quit", BUTTON, BUTTON_HOVER, BLACK,
                                  quit_button_y, width, height, quit_action)

    def get_start_button(self):
        return self.start_button

    def get_quit_button(self):
        return self.quit_button
