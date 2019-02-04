import tkinter

windows = tkinter.Tk()
windows.title("Grid Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

b1 = tkinter.Button(windows, text="(0, 0)")
b2 = tkinter.Button(windows, text="(0, 1)")
b3 = tkinter.Button(windows, text="(0, 2)")

b4 = tkinter.Button(windows, text="(1, 0)")
b5 = tkinter.Button(windows, text="(1, 1)")
b6 = tkinter.Button(windows, text="(1, 2)")

b7 = tkinter.Button(windows, text="(2, 1)")
b8 = tkinter.Button(windows, text="(2, 2)")
b9 = tkinter.Button(windows, text="(2, 4)")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0, rowspan=2)
b5.grid(row=1, column=1, columnspan=2)
b6.grid(row=1, column=3)

b7.grid(row=2, column=0, sticky="w")
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

windows.mainloop()
