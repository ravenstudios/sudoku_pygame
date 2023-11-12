from constants import *



class Solver:
    def __init__(self):
        pass




    def is_board_full(self, grid):
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c].value:
                    return False
        return True




    def get_row(self, grid, row):
        return grid[row].copy()


    def get_col(self, grid, row, col):
        col_arr = []
        for i in range(len(grid)):
            col_arr.append(grid[row + i][col])
        return col_arr



    def get_values(self, lst):
        result = []
        for l in lst:
            result.append(l.value)
        return result



    def check_row(self, grid, row, col, value):
        r = self.get_row(grid, row)
        x = grid[row][col]
        r.remove(x)
        nums = []
        for i in r:
            nums.append(i.value)
        return value in nums



    def check_col(self, grid, row, col, value):
        nums = []
        col_arr = []
        for i in range(len(grid)):
            col_arr.append(grid[i][col])
        x = grid[row][col]
        col_arr.remove(x)
        for c in col_arr:
            nums.append(c.value)
        print(f"nums:{nums}")
        return value in nums



    def check_box(self, grid, row, col, value):
        box_arr = []
        nums = []
        row_start = row // 3 * 3
        col_start = col // 3 * 3
        for i in range(3):
            box_arr.append(grid[row_start][col_start + i])
            box_arr.append(grid[row_start + 1][col_start + i])
            box_arr.append(grid[row_start + 2][col_start + i])
        x = grid[row][col]
        box_arr.remove(x)
        for b in box_arr:
            nums.append(b.value)
        return value in nums
