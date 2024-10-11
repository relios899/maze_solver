from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x, y):
        # x=0 left of screen y=0 top of screen
        self.x = x
        self.y = y

class Line():
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def draw(self,canvas, fill_color):
        canvas.create_line(self._start.x, self._start.y,
                           self._end.x, self._end.y, fill=fill_color,
                           width = 2)



class Cell():
    def __init__(self, top_left=Point(0,0), bottom_right=Point(1,1), window=None, lw=True,
                 rw=True, tw=True, bw=True):
        self._win = window
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        self.has_left_wall = lw 
        self.has_right_wall = rw 
        self.has_top_wall = tw
        self.has_bottom_wall = bw

    def draw(self):
        default_color = "black"
        # left wall is x1 and y1 -> y2
        if self.has_left_wall:
            lw_p1 = Point(self._x1, self._y1)
            lw_p2 = Point(self._x1, self._y2)
            lw_line = Line(lw_p1, lw_p2)
            self._win.draw_line(lw_line, default_color)

        # right wall is x2 and y1 -> y2
        if self.has_right_wall:
            rw_p1 = Point(self._x2, self._y1)
            rw_p2 = Point(self._x2, self._y2)
            rw_line = Line(rw_p1, rw_p2)
            self._win.draw_line(rw_line, default_color)

        # top wall is x1 -> x2 and y1
        if self.has_top_wall:
            tw_p1 = Point(self._x1, self._y1)
            tw_p2 = Point(self._x2, self._y1)
            tw_line = Line(tw_p1, tw_p2)
            self._win.draw_line(tw_line, default_color)
            

        # bottom wall is x1 -> x2 and y2
        if self.has_top_wall:
            bw_p1 = Point(self._x1, self._y2)
            bw_p2 = Point(self._x2, self._y2)
            bw_line = Line(bw_p1, bw_p2)
            self._win.draw_line(bw_line, default_color)

    def find_center(self):
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y1 + self._y2) / 2
        return Point(x_center, y_center)


    def draw_move(self, to_cell, undo=False):
        color = None
        if undo:
            color = "gray"
        else:
            color = "red"

        # center of a cell is defined as (x1 + x2) // 2 
        # and (y1 + y2) // 2
        p1 = self.find_center()
        p2 = to_cell.find_center()
        line = Line(p1, p2)
        self._win.draw_line(line, color)


