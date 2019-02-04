import tkinter

windows = tkinter.Tk()
windows.title("Place Test")
windows.geometry("640x480+100+100")
windows.resizable(0, 0)

b1 = tkinter.Button(windows, text="(50, 50)")
b2 = tkinter.Button(windows, text="(50, 100)")
b3 = tkinter.Button(windows, text="(100, 150)")
b4 = tkinter.Button(windows, text="(0, 200)")
b5 = tkinter.Button(windows, text="(0, 300)")
b6 = tkinter.Button(windows, text="(0, 300)")

b1.place(x=50, y=50)
b2.place(x=50, y=100, width=50, height=50)
b3.place(x=100, y=150, bordermode="inside")
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx=0.5)
b6.place(x=0, y=300, relx=0.5, anchor="s")

windows.mainloop()
