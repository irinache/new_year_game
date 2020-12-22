from random import randint

import numpy as np

from new_year_game.tree import Tree


class GameField:
    def __init__(self, screen):
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.trees = []
        self.screen = screen

    # def generate_field(self):
    #     tree_counter = 40
    #     while tree_counter > 0:
    #         i = randint(0, 9)
    #         j = randint(0, 9)
    #         if self.field[i][j] != 1:
    #             self.field[i][j] = 1
    #             tree = Tree(i, j)
    #             self.trees.append(tree)
    #             tree_counter -= 1
    #     print(self.field)
    #     return self.trees

    def generate_field(self):
        tree_counter = 100
        needed_tree_count = 40

        start_i = 0
        start_j = 0

        self.field[start_i][start_j] = 1
        tree_counter -= 1

        while tree_counter > needed_tree_count:
            size = randint(1, 9)
            direction = randint(0, 3)

            if direction == 0:
                i = start_i
                beginning = None
                end = None
                for i in range(start_i - size, start_i):
                    if 0 <= i < (self.screen.get_height() / 50) and tree_counter > needed_tree_count:
                        if beginning is None:
                            beginning = i
                        if self.field[i][start_j] != 1:
                            self.field[i][start_j] = 1
                            tree_counter -= 1
                            end = i
                    else:
                        continue
                if beginning is not None and end is not None and beginning <= end:
                    start_i = randint(beginning, end)
            elif direction == 1:
                j = start_j
                beginning = None
                end = None
                for j in range(start_j + 1, start_j + size + 1):
                    if 0 <= j < (self.screen.get_width() / 50) and tree_counter > needed_tree_count:
                        if beginning is None:
                            beginning = j
                        if self.field[start_i][j] != 1:
                            self.field[start_i][j] = 1
                            tree_counter -= 1
                            end = j
                    else:
                        continue
                if beginning is not None and end is not None and beginning <= end:
                    start_j = randint(beginning, end)
            elif direction == 2:
                i = start_i
                beginning = None
                end = None
                for i in range(start_i + 1, start_i + size + 1):
                    if 0 <= i < (self.screen.get_height() / 50) and tree_counter > needed_tree_count:
                        if beginning is None:
                            beginning = i
                            print("----", i, start_j)
                        if self.field[i][start_j] != 1:
                            self.field[i][start_j] = 1
                            tree_counter -= 1
                            end = i
                    else:
                        continue
                if beginning is not None and end is not None and beginning <= end:
                    start_i = randint(beginning, end)
            elif direction == 3:
                j = start_j
                beginning = None
                end = None
                for j in range(start_j - size, start_j):
                    if 0 <= j < (self.screen.get_width() / 50) and tree_counter > needed_tree_count:
                        if beginning is None:
                            beginning = j
                        if self.field[start_i][j] != 1:
                            self.field[start_i][j] = 1
                            tree_counter -= 1
                            end = j
                    else:
                        continue
                if beginning is not None and end is not None and beginning <= end:
                    start_j = randint(beginning, end)
            # set next position
            print(np.array(self.field))
            print(tree_counter)
            x = 0
            for i in range(0, 10):
                for j in range(0, 10):
                    if self.field[i][j] == 0:
                        x += 1
            print(x)

        for i in range(0, 10):
            for j in range(0, 10):
                if self.field[i][j] == 0:
                    self.trees.append(Tree(i, j))

        print(np.array(self.field))
        print(len(self.trees))

        return self.trees
