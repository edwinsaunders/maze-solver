from window import Window
from graphics import Point, Line
from cell import Cell
from constants import *

def main():
	win = Window(800, 600)

	cell1 = Cell(
		MARGIN, 
		MARGIN, 
		MARGIN + CELL_SIZE, 
		MARGIN + CELL_SIZE, 
		win
	)
	cell1.has_left_wall = False
	cell1.has_right_wall = False

	#formula for top left
	# cell center position x = y = cellsize / 2 + margin
	# other cells (e.g. position 2, 3, 4, etc. left to right, top to bottom):
	# just add multiple of cell size to x and/or y
	# for top left and bottom right coords:
	# tl-x = tl-y = centerpos - cellsize / 2
	cell2 = Cell(
		MARGIN + CELL_SIZE, 
		MARGIN, 
		MARGIN + 2 * CELL_SIZE, 
		MARGIN + CELL_SIZE, 
		win
	)
	cell2.has_left_wall = False

	cell1.draw()
	cell2.draw()
	
	win.wait_for_close()

main()
