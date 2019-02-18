import tkinter
import tkinter.ttk

windows = tkinter.Tk()
windows.title("Notebook Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

notebook = tkinter.ttk.Notebook(windows, width=300, height=300)
notebook.pack()

frame1 = tkinter.Frame(windows)
notebook.add(frame1, text="page1")
label1 = tkinter.Label(frame1, text="content of page1")
label1.pack()

frame2 = tkinter.Frame(windows)
notebook.add(frame2, text="page2")
label2 = tkinter.Label(frame2, text="content of page2")
label2.pack()

frame3 = tkinter.Frame(windows)
notebook.add(frame3, text="page4")
label3 = tkinter.Label(frame3, text="content of page4")
label3.pack()

frame4 = tkinter.Frame(windows)
#notebook.add(frame4, text="page4")
notebook.insert(2, frame4, text="page3")
label4 = tkinter.Label(frame4, text="content of page3")
label4.pack()

windows.mainloop()
