from graphics import *
from window import *
from time import sleep

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        # build cells
        start_y = self._y1
        for i in range(self._num_rows):
            start_x = self._x1
            row = []
            for j in range(self._num_cols):
                start = Point(start_x, start_y)
                end_x = start_x + self._cell_size_x
                end_y = start_y + self._cell_size_y
                end = Point(end_x, end_y)
                row.append(Cell(self._win, start, end))
                start_x += self._cell_size_x 
            self._cells.append(row)
            start_y += self._cell_size_y
        # draw cells
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)




    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.5)

