from cell import Cell
import time
import random


class Maze:
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

        if seed is not None:
            random.seed(seed)

        # check for valid values for num_rows and num_cols
        if num_rows < 1 or num_cols < 1 or not isinstance(num_rows, int) or \
                not isinstance(num_cols, int):
            raise ValueError("Invalid value for num_rows or num_cols")

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve_r(0, 0)

    def _create_cells(self):
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                x1 = self.x1 + j * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                x2 = self.x1 + (j + 1) * self.cell_size_x
                y2 = self.y1 + (i + 1) * self.cell_size_y

                self._cells[i].append(Cell(x1, y1, x2, y2, self._win))
        self._draw_cells()

    def _draw_cells(self):
        # for testing purpose, when no window exists, don't draw
        if not self._win:
            return
        for row_list in self._cells:
            for cell in row_list:
                cell.draw()

    def _animate(self):
        # for testing purpose, when no window exists, don't draw
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells()
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cells()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            poss_directions = []

            # if current cell has cell above not visited
            if i > 0 and not self._cells[i - 1][j].visited:
                poss_directions.append((i - 1, j))

            # if current cell has cell to the right not visited
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                poss_directions.append((i, j + 1))

            # if current cell has cell below not visited
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                poss_directions.append((i + 1, j))

            # if current cell has cell to the left not visited
            if j > 0 and not self._cells[i][j - 1].visited:
                poss_directions.append((i, j - 1))

            # If there are zero directions you can go from the current
            # cell, then draw the current cell and return to break out
            # of the loop
            if not poss_directions:
                current_cell.draw()
                return

            # Otherwise, pick a random direction
            new_dir_index = random.randrange(len(poss_directions))
            new_dir = poss_directions[new_dir_index]

            new_i = new_dir[0]
            new_j = new_dir[1]
            next_cell = self._cells[new_i][new_j]

            # math to figure out which wall in current_cell
            #   and new_cell to open
            above = (i - 1, j)
            below = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)

            if new_dir == above:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif new_dir == below:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif new_dir == left:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif new_dir == right:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False

            self._break_walls_r(new_i, new_j)
            self._animate()

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if current_cell == self._cells[self.num_rows - 1][self.num_cols - 1]:
            return True

        while True:
            if i > 0:
                cell_above = self._cells[i - 1][j]
            if j < self.num_cols - 1:
                cell_right = self._cells[i][j + 1]
            if i < self.num_rows - 1:
                cell_below = self._cells[i + 1][j]
            if j > 0:
                cell_left = self._cells[i][j - 1]

            # if current cell has cell above not visited
            if i > 0 and not cell_above.visited \
                    and not current_cell.has_top_wall \
                    and not cell_above.has_bottom_wall:
                current_cell.draw_move(cell_above)
                if self._solve_r(i - 1, j):
                    return True
                else:
                    current_cell.draw_move(cell_above, undo=True)

            # if current cell has cell to the right not visited
            if j < self.num_cols - 1 and not cell_right.visited \
                    and not current_cell.has_right_wall \
                    and not cell_right.has_left_wall:
                current_cell.draw_move(cell_right)
                if self._solve_r(i, j + 1):
                    return True
                else:
                    current_cell.draw_move(cell_right, undo=True)

            # if current cell has cell below not visited
            if i < self.num_rows - 1 and not cell_below.visited \
                    and not current_cell.has_bottom_wall \
                    and not cell_below.has_top_wall:
                current_cell.draw_move(cell_below)
                if self._solve_r(i + 1, j):
                    return True
                else:
                    current_cell.draw_move(cell_below, undo=True)

            # if current cell has cell to the left not visited
            if j > 0 and not cell_left.visited \
                    and not current_cell.has_left_wall \
                    and not cell_left.has_right_wall:
                current_cell.draw_move(cell_left)
                if self._solve_r(i, j - 1):
                    return True
                else:
                    current_cell.draw_move(cell_left, undo=True)

            return False
