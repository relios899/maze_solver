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

if __name__ == "__main__":
    unittest.main()
