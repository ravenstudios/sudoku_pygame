import square
from constants import *
import pygame


class Board_manager:
    def __init__(self):
        self.grid = []
        for r in range(ROWS):
            row = []
            for c in range(COLS):
                row.append(square.Square(c, r))
            self.grid.append(row)


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
        self.check_row(self.row, value)



    def check_row(self, row, value):
        print(f"value: {value}")

        r = self.grid[row]
        nums = []
        for i in range(9):
            nums.append(self.grid[row][i].get_value())
        print(nums)
        print(value in nums)
        # for x in r:
        #     print(r.get_value())

    def check_col(self):
        pass

    def check_box(self):
        pass
