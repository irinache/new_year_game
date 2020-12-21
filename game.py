from new_year_game.colors import *
from new_year_game.game_screen import GameScreen
from new_year_game.menu_screen import MenuScreen
from new_year_game.santa import Santa
from new_year_game.text import Text

import pygame
from pygame import event

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
        self.menu_screen = MenuScreen()
        self.game_screen = GameScreen()
        self.screen = self.menu_screen.get_screen()
        self.santa = Santa(self.screen)
        self.keys = [False, False, False, False]


        # draw buttons
        self.menu_screen.draw_buttons(self.start, self.quit_game)

        # initialize sprite groups
        self.menu.add(self.menu_screen.get_start_button())
        self.menu.add(self.menu_screen.get_quit_button())
        self.game_field.add(self.santa)

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

            # create heading
            text = Text(self.screen, "New Year Game", BLACK, 50, "Montserrat-Regular", 30)
            self.menu.add(text)

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

            self.game_field.update(self.keys)

            # rendering
            self.screen.fill(BACKGROUND)
            self.game_field.draw(self.screen)

            # after drawing flip screen
            pygame.display.flip()

        self.quit_game()
