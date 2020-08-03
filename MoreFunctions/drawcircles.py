import math

try:
	import tkinter
except ImportError:  # python2
	import TkInter as tkinter


def parablola(page, size):
	for x in range(-size, size):
		y = x * x / size
		plot(page, x, y)


# Modify the circle function so that it allows the color of the circle to be specified
# and defaults to red if a color is not given.

def circle(page, radius, g, h, colour="red"):
	page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)


# for x in range(g * 100, (g + radius) * 100):
# 	x/=100
# 	print(x)
# 	y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
# 	plot(page, x, y)
# 	plot(page, x, 2 * h -y)
# 	plot(page, 2 * g -x, y)
# 	plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
	page.update()
	x_origin = canvas.winfo_width() / 2
	y_origin = canvas.winfo_height() / 2
	page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
	page.create_line(-x_origin, 0, x_origin, 0, fill="black")
	page.create_line(0, -y_origin, 0, y_origin, fill="black")
	print(locals())


def plot(canvas, x, y):
	canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parablola(canvas, 100)
parablola(canvas, 200)
circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
