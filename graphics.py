class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x,
                           self.point2.y, fill=fill_color, width=2)

    def adjust_length(self):
        adjustment = 1
        # shrink line so as not to have marks where deletion lines are drawn
        # determine which direction line is oriented
        if self.point1.x == self.point2.x:
            self.point1.y += adjustment
            self.point2.y -= adjustment
        elif self.point1.y == self.point2.y:
            self.point1.x += adjustment
            self.point2.x -= adjustment
