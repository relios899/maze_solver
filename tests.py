import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_col = 3
        num_row = 5
        m1 = Maze(0,0, num_row, num_col, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_row 
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_col
        )
    def test_maze_reset_visited(self):
        num_rows = 3
        num_cols = 5
        m1 = Maze(0,0, num_cols, num_rows, 10,10)
        m1._cells[0][0].visited = True
        m1._reset_cells_visited()
        self.assertEqual(
                m1._cells[0][0].visited,
                False
        )


if __name__ == "__main__":
    unittest.main()
