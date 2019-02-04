import tkinter

windows = tkinter.Tk()
windows.title("Label Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

label = tkinter.Label(windows, text="Hello Tkinter", width=15, height=5, fg="red", relief="solid")
label.pack()

windows.mainloop()
