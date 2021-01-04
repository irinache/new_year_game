from new_year_game.bottom_bar import BottomBar
from new_year_game.colors import *
from new_year_game.game_field import GameField
from new_year_game.game_screen import GameScreen
from new_year_game.menu_screen import MenuScreen
from new_year_game.santa import Santa
from new_year_game.text import Text

import pygame
from pygame import event


# todo иногда попадает в бесконечный уикл
class Game:
    def __init__(self):
        # run pygame
        pygame.init()
        pygame.mixer.init()

        # create sprite groups
        self.menu = pygame.sprite.Group()
        self.game_field = pygame.sprite.Group()

        # initialize variables
        self.intro = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        #self.menu_screen = MenuScreen(500, 300)
        self.screen = MenuScreen(500, 300)
        #self.game_screen = GameScreen(500, 570)
        #self.screen = self.menu_screen.get_screen()
        self.santa = None
        self.keys = []
        self.field = None
        self.wood = []
        self.prizes = []
        self.bar = None

        # draw buttons
        self.screen.draw_buttons(self.start, self.quit_game)

        # initialize sprite groups
        self.menu.add(self.screen.get_start_button())
        self.menu.add(self.screen.get_quit_button())


    # quit game method
    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    # loop for entering menu
    def game_intro(self):
        while self.intro:
            # Держим цикл на правильной скорости
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            # fill background
            self.screen.fill(BACKGROUND)
            self.screen.fill(BACKGROUND)

            # create heading
            text = Text(self.screen, "New Year Game", BLACK, 50, 0, "Montserrat-Regular", 30, "c")
            self.menu.add(text)

            self.menu.draw(self.screen.get_screen())
            self.menu.update()

            # update display
            pygame.display.update()

    def start(self):
        self.intro = False

        # run main loop
        self.game_loop()

    # main game loop
    def game_loop(self):

        self.screen = GameScreen(500, 570)

        self.santa = Santa(self.screen)
        self.keys = [False, False, False, False]
        self.field = GameField(self.screen)
        self.wood = self.field.generate_field()
        self.prizes = self.field.place_prizes()
        self.bar = BottomBar(self.screen, BAR_BACKGROUND, self.screen.get_width(), 60)

        self.game_field.add(self.santa)
        self.game_field.add(self.wood)
        self.game_field.add(self.prizes)
        self.game_field.add(self.bar)

        running = True
        while running:
            # Держим цикл на правильной скорости
            self.clock.tick(self.fps)

            # handling event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.keys[0] = True
                    elif event.key == pygame.K_DOWN:
                        self.keys[1] = True
                    elif event.key == pygame.K_RIGHT:
                        self.keys[2] = True
                    elif event.key == pygame.K_LEFT:
                        self.keys[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.keys[0] = False
                    elif event.key == pygame.K_DOWN:
                        self.keys[1] = False
                    elif event.key == pygame.K_RIGHT:
                        self.keys[2] = False
                    elif event.key == pygame.K_LEFT:
                        self.keys[3] = False

            # rendering
            self.screen.fill(BACKGROUND)
            self.game_field.draw(self.screen.get_screen())

            # update display
            self.game_field.update(self.keys, self.game_field)

            # after drawing flip screen
            pygame.display.flip()

        self.quit_game()
