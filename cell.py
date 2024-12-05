
from window import Window
from graphics import Point, Line

class Cell:
	def __init__(self, x1, y1, x2, y2, win=None):
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self._x1 = x1
		self._x2 = x2
		self._y1 = y1
		self._y2 = y2
		self._win = win
		self.visited = False

	def draw(self):
		
		point1 = Point(self._x1, self._y1)
		point2 = Point(self._x1, self._y2)
		line1 = Line(point1, point2)
		
		if self.has_left_wall:
			self._win.draw_line(line1, "black")
		else:
			self._win.draw_line(line1, "gray75")

		point1 = Point(self._x2, self._y1)
		point2 = Point(self._x2, self._y2)
		line2 = Line(point1, point2)		
		
		if self.has_right_wall:
			self._win.draw_line(line2, "black")
		else:
			self._win.draw_line(line2, "gray75")
		
		point1 = Point(self._x1, self._y1)
		point2 = Point(self._x2, self._y1)
		line3 = Line(point1, point2)
		
		if self.has_top_wall:
			self._win.draw_line(line3, "black")
		else:
			self._win.draw_line(line3, "gray75")
		
		point1 = Point(self._x1, self._y2)
		point2 = Point(self._x2, self._y2)
		line4 = Line(point1, point2)
		
		if self.has_bottom_wall:
			self._win.draw_line(line4, "black")
		else:
			self._win.draw_line(line4, "gray75")
		
		
	def draw_move(self, dest_cell, undo=False):
		src_midX = self._x1 + (self._x2 - self._x1) / 2
		src_midY = self._y1 + (self._y2 - self._y1) / 2
		dest_midX = dest_cell._x1 + (dest_cell._x2 - dest_cell._x1) / 2
		dest_midY = dest_cell._y1 + (dest_cell._y2 - dest_cell._y1) / 2
		point1 = Point(src_midX, src_midY)
		point2 = Point(dest_midX, dest_midY)
		line = Line(point1, point2)
		self._win.draw_line(line, "red")