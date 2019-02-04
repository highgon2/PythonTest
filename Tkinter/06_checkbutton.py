import tkinter

windows = tkinter.Tk()
windows.title("Checkbox Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

def flash():
	checkbox_button1.flash()
	# print(checkbox_variety1.get(), checkbox_variety2.get())

checkbox_variety1 = tkinter.IntVar()
checkbox_variety2 = tkinter.IntVar()


checkbox_button1 = tkinter.Checkbutton(windows, text="O", variable=checkbox_variety1, activebackground="blue")
checkbox_button2 = tkinter.Checkbutton(windows, text="@", variable=checkbox_variety2)
checkbox_button3 = tkinter.Checkbutton(windows, text="X", variable=checkbox_variety2, command=flash)

checkbox_button1.pack()
checkbox_button2.pack()
checkbox_button3.pack()

windows.mainloop()
