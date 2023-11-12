import square
from constants import *
import pygame


class Board_manager:
    def __init__(self):
        self.grid = []
        count = 0
        for r in range(ROWS):
            row = []
            for c in range(COLS):
                row.append(square.Square(c, r, count))
                count += 1
            self.grid.append(row)

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
        self.check_col(self.row, self.col, value)



    def check_row(self, row, col, value):
        print(f"value: {col}")

        r = self.grid[row].copy()
        x = self.grid[row][col]
        print(f"row:{x.row}, col:{x.col}, value:{x.value}")
        r.remove(x)
        nums = []
        for i in r:
            nums.append(i.value)
        print(nums)
        print(value in nums)


    def check_col(self, row, col, value):
        nums = []
        col_arr = []
        for i in range(len(self.grid)):
            col_arr.append(self.grid[i][col])
        x = self.grid[row][col]
        col_arr.remove(x)
        for c in col_arr:
            nums.append(c.value)

        print(nums)


    def check_box(self):
        pass
