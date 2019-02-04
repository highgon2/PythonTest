import tkinter

windows = tkinter.Tk()
windows.title("RadioButton Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

def check():
	label.config(text =	"radio_variety1 = " + str(radio_variety1.get()) + "\n" +
						"radio_variety2 = " + str(radio_variety2.get()) + "\n\n" +
						"total = " + str(radio_variety1.get() + radio_variety2.get()))
						
radio_variety1 = tkinter.IntVar()
radio_variety2 = tkinter.IntVar()

radio1 = tkinter.Radiobutton(windows, text="1번", value=3, variable=radio_variety1, command=check)
radio1.pack()

radio2 = tkinter.Radiobutton(windows, text="2번(1번)", value=3, variable=radio_variety1, command=check)
radio2.pack()

radio3 = tkinter.Radiobutton(windows, text="3번", value=9, variable=radio_variety1, command=check)
radio3.pack()

label = tkinter.Label(windows, text="None", height=5)
label.pack()

radio4 = tkinter.Radiobutton(windows, text="4번", value=12, variable=radio_variety2, command=check)
radio4.pack()

radio5 = tkinter.Radiobutton(windows, text="5번", value=15, variable=radio_variety2, command=check)
radio5.pack()

windows.mainloop()
