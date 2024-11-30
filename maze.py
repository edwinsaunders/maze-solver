from cell import Cell
import time

class Maze:
	def __init__(
			self, 
			x1, 
			y1, 
			num_rows, 
			num_cols, 
			cell_size_x, 
			cell_size_y, 
			win
		):

		self.x1 = x1
		self.y1 = y1
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self.win = win

		self._create_cells()

	def _create_cells(self):
		self._cells = []
		for i in range(self.num_rows):
			self._cells.append([])
			for j in range(self.num_cols):
				x1 = self.x1 + j * self.cell_size_x
				y1 = self.y1 + i * self.cell_size_y
				x2 = self.x1 + (j + 1) * self.cell_size_x
				y2 = self.y1 + (i + 1) * self.cell_size_y

				self._cells[i].append(Cell(x1, y1, x2, y2, self.win))
		self._draw_cell()

	def _draw_cell(self):
		for row_list in self._cells:
			for cell in row_list:
				cell.draw()
				self._animate()

	def _animate(self):		
		self.win.redraw()
		time.sleep(0.05)
