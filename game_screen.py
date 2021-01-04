from new_year_game.screen import Screen


class GameScreen(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.bar_height = 70

    def get_playable_height(self):
        return self.screen.get_height() - self.bar_height

    def get_playable_width(self):
        return self.screen.get_width()




