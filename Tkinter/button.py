import tkinter

windows = tkinter.Tk()
windows.title("Button Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

count = 0
def countUP():
	global count
	count += 1
	label.config(text=str(count))

label = tkinter.Label(windows, text="0")
label.pack()

button = tkinter.Button(windows, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()
button.invoke()

windows.mainloop()
