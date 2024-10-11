from graphics import *
from window import *
from cell import *
from time import sleep
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed:
            random.seed(seed)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        # build cells
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        # draw cells
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)




    def _draw_cell(self, i, j):
        start_x = self._x1 + j * self._cell_size_x
        start_y = self._y1 + i * self._cell_size_y
        start = Point(start_x, start_y)
        end_x = start_x + self._cell_size_x
        end_y = start_y + self._cell_size_y
        end = Point(end_x, end_y)
        self._cells[i][j].draw(start, end)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        sleep(0.2)

    def _break_entrance_and_exit(self):
        # top right cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        last_col = len(self._cells[0])-1
        last_row = len(self._cells) -1
        self._cells[last_row][last_col].has_bottom_wall = False
        self._draw_cell(last_row, last_col)

    def _break_walls_between_cells(self, i, j, new_cell):
        new_cell_idx, dir = new_cell
        new_cell_y = new_cell_idx[0]
        new_cell_x = new_cell_idx[1]
        # curr cell -> redraw
        match dir:
            case "top":
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i,j)
                self._cells[new_cell_y][new_cell_x].has_bottom_wall = False
                self._draw_cell(new_cell_y, new_cell_x)
            case "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i,j)
                self._cells[new_cell_y][new_cell_x].has_top_wall = False
                self._draw_cell(new_cell_y, new_cell_x)
            case "left":
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i,j)
                self._cells[new_cell_y][new_cell_x].has_right_wall = False
                self._draw_cell(new_cell_y, new_cell_x)
            case "right":
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                self._cells[new_cell_y][new_cell_x].has_left_wall = False
                self._draw_cell(new_cell_y, new_cell_x)

        # new cell -> redraw

        
    def _break_walls_r(self, i, j):
        if not self._cells:
            return
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # top y - 1
            if i-1 >=0 and not self._cells[i-1][j].visited:
                to_visit.append(([i-1, j], "top"))
            # bottom y + 1
            if i + 1 < len(self._cells) and not self._cells[i+1][j].visited:
                to_visit.append(([i+1, j], "bottom"))
            # left x -1
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append(([i, j-1], "left"))
            # right x + 1
            if j+1 < len(self._cells[0]) and not self._cells[i][j+1].visited:
                to_visit.append(([i, j+1], "right"))
            # j = x , i = y
            # check if inbounds

            # base case no directions to move so done
            if not to_visit:
                self._draw_cell(i,j)
                return
            rand_idx = random.randrange(0, len(to_visit))
            new_x = to_visit[rand_idx][0][1]
            new_y = to_visit[rand_idx][0][0]
            self._break_walls_between_cells(i,j,to_visit[rand_idx])
            self._break_walls_r(new_y, new_x)


    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].visited = False

        

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        # goal cell is the final cell in the grid
        # len(y) - 1 and len(x) -1
        if ( i == len(self._cells) - 1 and j == len(self._cells[0]) - 1):
            return True


        # check top
        if (
                i-1 >=0 
                and not self._cells[i-1][j].visited 
                and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            res = self._solve_r(i-1, j)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        # check bottom
        if (
                i+1 < len(self._cells) 
                and not self._cells[i+1][j].visited 
                and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            res = self._solve_r(i+1, j)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        
        # check left
        if (
                j-1 >=0 
                and not self._cells[i][j-1].visited 
                and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            res = self._solve_r(i, j-1)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # check right
        if (
                j+1 < len(self._cells[0]) 
                and not self._cells[i][j+1].visited 
                and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            res = self._solve_r(i, j+1)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False
