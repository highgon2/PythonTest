import tkinter

windows = tkinter.Tk()
windows.title("Menu Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

def close():
	windows.quit()
	windows.destroy()

menubar = tkinter.Menu(windows)

menu1 = tkinter.Menu(menubar, tearoff=0)
menu1.add_command(label="sub menu 1-1")
menu1.add_command(label="sub menu 1-2")
menu1.add_separator()
menu1.add_command(label="sub menu 1-3", command=close)
menubar.add_cascade(label="Top menu1", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu2.add_radiobutton(label="sub menu 2-1", state="disable")
menu2.add_radiobutton(label="sub menu 2-2")
menu2.add_radiobutton(label="sub menu 2-3")
menubar.add_cascade(label="Top menu2", menu=menu2)

menu3 = tkinter.Menu(menubar, tearoff=0)
menu3.add_checkbutton(label="sub menu 3-1")
menu3.add_checkbutton(label="sub menu 3-2")
menubar.add_cascade(label="Top menu3", menu=menu3)

windows.config(menu=menubar)
windows.mainloop()

print("Window Close")
