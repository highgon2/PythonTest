import tkinter

windows = tkinter.Tk()
windows.title("PanedWindow Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

paned_window1 = tkinter.PanedWindow(relief="raised", bd=2)
paned_window1.pack(expand=True)

left_label = tkinter.Label(paned_window1, text="inner window-1 : left")
paned_window1.add(left_label)

paned_window2 = tkinter.PanedWindow(paned_window1, orient="vertical", relief="groove", bd=3)
paned_window1.add(paned_window2)

right_label = tkinter.Label(paned_window1, text="inner window-2 : right")
paned_window1.add(right_label)

top_label = tkinter.Label(paned_window2, text="in window-3 : top")
paned_window2.add(top_label)

bottom_label = tkinter.Label(paned_window2, text="in window-3 : bottom")
paned_window2.add(bottom_label)

windows.mainloop()
