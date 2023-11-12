import unittest
import solver
import square
from constants import *
import board_manager


class TestSolver(unittest.TestCase):
    def setUp(self):
        bm = board_manager.Board_manager()
        self.solver = solver.Solver()
        self.grid = bm.grid




    def testGetRow(self):
        self.assertEqual(len(self.solver.get_row(self.grid, 0)), 9, "length not = 9")
        self.assertEqual(type(self.solver.get_row(self.grid, 0)[0]), square.Square, "not getting correct list")
        values = self.solver.get_values(self.solver.get_row(self.grid, 0))
        self.assertEqual(values, [1, 2, 3, 4, 5, 6, 7, 8, 9],  "not getting correct list")



    def testGetCol(self):
        self.assertEqual(len(self.solver.get_col(self.grid, 0, 0)), 9, "length not = 9")
        values = self.solver.get_values(self.solver.get_col(self.grid, 0, 0))
        self.assertEqual(values, [1, 1, 1, 1, 1, 1, 1, 1, 1], "not getting correct list")
        values = self.solver.get_values(self.solver.get_col(self.grid, 0, 1))
        self.assertEqual(values, [2, 2, 2, 2, 2, 2, 2, 2, 2], "not getting correct list")
        values = self.solver.get_values(self.solver.get_col(self.grid, 0, 4))
        self.assertEqual(values, [5, 5, 5, 5, 5, 5, 5, 5, 5], "not getting correct list")
        values = self.solver.get_values(self.solver.get_col(self.grid, 0, 8))
        self.assertEqual(values, [9, 9, 9, 9, 9, 9, 9, 9, 9], "not getting correct list")


    def test_check_row(self):

        self.assertEqual(self.solver.check_row(self.grid, 0, 0, 0), False, "True should = False")
        self.assertEqual(self.solver.check_row(self.grid, 0, 1, 1), True, "False should = True")




if __name__ == '__main__':
    unittest.main()
