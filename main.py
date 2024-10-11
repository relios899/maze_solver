from window import Window
from graphics import *
from maze import *

def main():
    win = Window(800, 600)
    # start = Point(20, 50)
    # end = Point(50, 100)
    # line = Line(start, end)
    # cell = Cell(win, start, end, lw=False, rw=False)
    # cell.draw()
    # # win.draw_line(line, "black")
    #
    # start = Point(60, 50)
    # end = Point(110, 100)
    # cell2 = Cell(win, start, end, tw=False, bw=False)
    # cell2.draw()

    maze = Maze(20,20,3,3,100,100,win)


    # cell.draw_move(cell2, undo=True)

    win.wait_for_close()

main()
