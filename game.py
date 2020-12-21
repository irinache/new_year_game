from new_year_game.button import *
from new_year_game.colors import *
from new_year_game.game_screen import GameScreen
from new_year_game.menu_screen import MenuScreen
from new_year_game.santa import Santa


class Game:
    def __init__(self):
        # run pygame
        pygame.init()

        # create sprite groups
        self.menu = pygame.sprite.Group()
        self.game_field = pygame.sprite.Group()

        # initialize variables
        self.intro = True
        self.menu_screen = MenuScreen()
        self.game_screen = GameScreen()

        self.santa = Santa()

        self.menu_screen.draw_buttons(self.start, self.quit_game)
        self.screen = self.menu_screen.get_screen()

        self.menu.add(self.menu_screen.get_start_button())
        self.menu.add(self.menu_screen.get_quit_button())

        self.game_field.add(self.santa)



    # quit game method
    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    # render text sprite
    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

    # loop for entering menu
    def game_intro(self):
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            # fill background
            self.screen.fill(BACKGROUND)

            # create heading
            text = pygame.font.Font('fonts/Montserrat-Regular.ttf', 30)
            text_surf, text_rext = self.text_objects("New Year Game", text)
            text_rext.center = (self.menu_screen.get_width() / 2, 50)
            self.screen.blit(text_surf, text_rext)

            self.menu.draw(self.screen)
            self.menu.update()

            # update display
            pygame.display.update()

    def start(self):
        self.intro = False

        self.screen = self.game_screen.get_screen()

        # run main loop
        self.game_loop()

    # main game loop
    def game_loop(self):

        running = True
        while running:

            # handling event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # rendering
            self.screen.fill(BACKGROUND)
            self.game_field.draw(self.screen)

            # after drawing flip screen
            pygame.display.flip()

        self.quit_game()
