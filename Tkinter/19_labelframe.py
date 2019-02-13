import tkinter

windows = tkinter.Tk()
windows.title("LabelFrame Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

def check():
	label.config(text=radio_variety1.get())

labelframe = tkinter.LabelFrame(windows, text="Platform Sel")
labelframe.pack()

radio_variety1 = tkinter.StringVar()
radio_variety1.set("미선택")

radio1 = tkinter.Radiobutton(labelframe, text="Pyton", value="가능", variable=radio_variety1, command=check)
radio1.pack()

radio2 = tkinter.Radiobutton(labelframe, text="C/C++", value="부분 가능", variable=radio_variety1, command=check)
radio2.pack()

radio3 = tkinter.Radiobutton(labelframe, text="JSON", value="불가능", variable=radio_variety1, command=check)
radio3.pack()

label = tkinter.Label(labelframe, text="None")
label.pack()

windows.mainloop()
