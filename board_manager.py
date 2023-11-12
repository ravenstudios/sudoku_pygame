import square
from constants import *
import pygame
import random
import solver


class Board_manager:
    def __init__(self):
        self.grid = self.make_board(True)


        self.solver = solver.Solver()
        solved = self.solver.is_board_full(self.grid)



    def make_board(self, fill=False):
        grid = []
        for r in range(ROWS):
            row = []
            count = 1
            for c in range(COLS):
                s = square.Square(c, r)
                if fill:
                    s.value = count
                row.append(s)
                count += 1
            grid.append(row)
        return grid

        # done = False
        # count = 0
        # while not done:
        #     for r in range(ROWS):
        #         for c in range(COLS):
        #             cell = self.grid[r][c]
        #
        #             x = random.randint(1, 9)
        #             if not self.check_row(r, c, x):
        #                 if not self.check_col(r, c, x):
        #                     if not self.check_box(r, c, x):
        #                         self.grid[r][c].value = x
        #                         count += 1
        #             print(count)
        #             if count == 9 * 9 -1:
        #                 done = True











        # for r in range(len(self.grid)):
        #     for c in range(len(self.grid[r])):
        #         print(f"r:{self.grid[r][c].row}, c:{self.grid[r][c].col}, value:{self.grid[r][c].get_value()}")


    def update(self):
        for gr in self.grid:
            for gc in gr:
                gc.update()

    def draw(self, surface):
        for gr in self.grid:
            for gc in gr:
                gc.draw(surface)

    def clicked(self):
        self.row = pygame.mouse.get_pos()[1] // BLOCK_SIZE
        self.col = pygame.mouse.get_pos()[0] // BLOCK_SIZE
        self.grid[self.row][self.col].clicked()
        value = self.grid[self.row][self.col].get_value()
        # self.check_row(self.row, self.col, value)
        # self.check_col(self.row, self.col, value)
        self.check_box(self.row, self.col, value)
