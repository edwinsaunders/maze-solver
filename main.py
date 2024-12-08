
from window import Window
# from graphics import Point, Line
from cell import Cell
from constants import *
from maze import Maze


def main():
    win = Window(WIN_WIDTH, WIN_HEIGHT)  # noqa: F405

    cell1 = Cell(
        MARGIN_LR,  # noqa: F405
        MARGIN_TB,  # noqa: F405
        MARGIN_LR + CELL_SIZE,  # noqa: F405
        MARGIN_TB + CELL_SIZE,  # noqa: F405
        win
    )
    cell1.has_left_wall = False
    cell1.has_right_wall = False

    # formula for top left
    # cell center position x = y = cellsize / 2 + margin
    # other cells (e.g. position 2, 3, 4, etc. left to right, top to bottom):
    # just add multiple of cell size to x and/or y
    # for top left and bottom right coords:
    # tl-x = tl-y = centerpos - cellsize / 2
    cell2 = Cell(
        MARGIN_LR + CELL_SIZE,  # noqa: F405
        MARGIN_TB,  # noqa: F405
        MARGIN_LR + 2 * CELL_SIZE,  # noqa: F405
        MARGIN_TB + CELL_SIZE,  # noqa: F405
        win
    )
    cell2.has_left_wall = False

    maze = Maze(  # noqa: 841
        MARGIN_LR, MARGIN_TB, NUM_ROWS, NUM_COLS, CELL_SIZE,  # noqa: F405
        CELL_SIZE,  # noqa: F405
        win
    )

    # cell1.draw()
    # cell2.draw()
    # cell1.draw_move(cell2)

    win.wait_for_close()


main()
