import unittest
from maze import Maze

class Tests(unittest.TestCase):
	def test_maze_create_10x12(self):
		num_rows = 10
		num_cols = 12
		
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_rows
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_cols
		)

	def test_maze_create_20x20(self):
		num_rows = 2
		num_cols = 2
		
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_rows
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_cols
		)

	def test_maze_create_0x0(self):
		num_rows = 0
		num_cols = 0
		
		with self.assertRaises(ValueError):
			m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

	def test_maze_create_neg(self):
		num_rows = -1
		num_cols = -1
		
		with self.assertRaises(ValueError):
			m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		
if __name__ == "__main__":
    unittest.main()