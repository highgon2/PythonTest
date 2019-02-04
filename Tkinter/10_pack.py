import tkinter

windows = tkinter.Tk()
windows.title("Pack Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

b1 = tkinter.Button(windows, text="top")
b1_1 = tkinter.Button(windows, text="top-1")

b2 = tkinter.Button(windows, text="bottom")
b2_1 = tkinter.Button(windows, text="bottom-1")

b3 = tkinter.Button(windows, text="left")
b3_1 = tkinter.Button(windows, text="left-1")

b4 = tkinter.Button(windows, text="right")
b4_1 = tkinter.Button(windows, text="right-1")

b5 = tkinter.Button(windows, text="center", bg="red")

b1.pack(side="top")
b1_1.pack(side="top", fill="x")

b2.pack(side="bottom")
b2_1.pack(side="bottom", anchor="e")

b3.pack(side="left")
b3_1.pack(side="left", fill="y")

b4.pack(side="right")
b4_1.pack(side="right", anchor="s")

b5.pack(expand=True, fill="both")

windows.mainloop()
