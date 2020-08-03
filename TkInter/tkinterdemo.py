#tkinter Python binding works by actively sanding TCL code to TCL
try:
	import tkinter
except ImportError: #python 2
	import TkInter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+4+200')

label = tkinter.Label(mainWindow, text="Hello world")
label.grid(row=0, column=0)

leftFame = tkinter.Frame(mainWindow)
leftFame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFame = tkinter.Frame(mainWindow)
rightFame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.grid(row=2, column=2)
button2.grid(row=3, column=2)
button3.grid(row=4, column=2)

#configer the column
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFame.config(relief='sunken', borderwidth=1)
rightFame.config(relief='sunken', borderwidth=1)
leftFame.grid(sticky='ns')
rightFame.grid(sticky='new')

rightFame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')
mainWindow.mainloop()
