import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_col = 3
        num_row = 3
        m1 = Maze(0,0, num_row, num_col, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_col
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_row
        )

if __name__ == "__main__":
    unittest.main()
