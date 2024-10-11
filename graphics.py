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



