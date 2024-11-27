from tkinter import Tk, BOTH, Canvas

class Window:
	def __init__(self, width, height):
		self.__root = Tk()
		self.__root.title("Title")
		self.canvas = Canvas(self.__root, width=width, height=height, background='gray75')
		self.canvas.pack()
		self.isRunning = False
		self.__root.protocol("WM_DELETE_WINDOW", self.close)

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.isRunning = True
		while self.isRunning == True:
			self.redraw()

	def close(self):
		self.isRunning = False