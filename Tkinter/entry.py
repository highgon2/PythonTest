import tkinter
from math import *

windows = tkinter.Tk()
windows.title("Entry Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

def calc(event):
	label.config(text="result = " + str(eval(entry.get())))

entry = tkinter.Entry(windows)
entry.bind("<Return>", calc)
entry.pack()

label = tkinter.Label(windows)
label.pack()

windows.mainloop()
