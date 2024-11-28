from window import Window
from graphics import Point, Line

def main():
	win = Window(800, 600)

	point1 = Point(2, 3)
	point2 = Point(40, 50)
	line1 = Line(point1, point2)

	point1 = Point(20, 30)
	point2 = Point(40, 100)
	line2 = Line(point1, point2)

	point1 = Point(500, 3)
	point2 = Point(0, 75)
	line3 = Line(point1, point2)

	win.draw_line(line1, "red")
	win.draw_line(line2, "black")
	win.draw_line(line3, "red")

	win.wait_for_close()

main()
