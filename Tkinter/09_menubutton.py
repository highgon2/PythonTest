import tkinter

windows = tkinter.Tk()
windows.title("Menubutton Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

menubutton = tkinter.Menubutton(windows, text="Menu Menubutton", relief="raised", direction="right")
menubutton.pack()
menu = tkinter.Menu(menubutton, tearoff=0)
menu.add_command(label="sub menu-1")
menu.add_separator()
menu.add_command(label="sub menu-2")
menu.add_command(label="sub menu-3")

menubutton["menu"]=menu
windows.mainloop()
