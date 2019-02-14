import tkinter

windows = tkinter.Tk()
windows.title("PhotoImage Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

image = tkinter.PhotoImage(file="python.png")
label = tkinter.Label(windows, image=image)
label.pack()

windows.mainloop()
