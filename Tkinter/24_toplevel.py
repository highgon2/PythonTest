import tkinter

windows = tkinter.Tk()
windows.title("TopLevel Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

menubar = tkinter.Menu(windows)

menu1 = tkinter.Menu(menubar, tearoff=0)
menu1.add_command(label="sub menu 1-1")
menu1.add_command(label="sub menu 1-2")
menu1.add_separator()
menu1.add_command(label="sub menu 1-3")

menubar.add_cascade(label="menu 1", menu=menu1)

top_level = tkinter.Toplevel(windows, menu=menubar)
top_level.title("Sub windows")
top_level.geometry("320x200+820+100")

label = tkinter.Label(top_level, text="Top Level")
label.pack()

windows.mainloop()
