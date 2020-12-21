from new_year_game.button import Button, BUTTON_HOVER, BUTTON
from new_year_game.screen import Screen


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()

    def draw_buttons(self, start_action, quit_action):
        # buttons params
        mouse_height = 40
        mouse_width = 120
        start_button_x = 130
        start_button_y = 130
        quit_button_x = 130
        quit_button_y = 190

        # create buttons
        self.start_button = Button(self.screen, "Start game", BUTTON, BUTTON_HOVER, start_button_x,
                              start_button_y,
                              mouse_width, mouse_height, start_action)
        self.quit_button = Button(self.screen, "Quit", BUTTON, BUTTON_HOVER, quit_button_x, quit_button_y,
                             mouse_width,
                             mouse_height, quit_action)


    def get_start_button(self):
        return self.start_button

    def get_quit_button(self):
        return self.quit_button



