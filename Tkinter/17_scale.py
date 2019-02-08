import tkinter

windows = tkinter.Tk()
windows.title("Scale Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

def select(self):
	value = "value : " + str(scale.get())
	label.config(text=value)

var = tkinter.IntVar()
scale = tkinter.Scale(windows, variable=var, command=select, takefocus=True, orient="horizontal", showvalue=False, tickinterval=50, to=500, length=300)
scale.pack()

label = tkinter.Label(windows, text="value : 0")
label.pack()

windows.mainloop()
