from tkinter import Tk, BOTH, Canvas
import sys


class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Title")
        self.canvas = Canvas(self._root,
                             width=width,
                             height=height,
                             background='gray75')
        self.canvas.pack()
        self.isRunning = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False
        self._root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)