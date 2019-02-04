import tkinter

windows = tkinter.Tk()
windows.title("Listbox Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

listbox = tkinter.Listbox(windows, selectmode="single", height=0)
for i in range(5):
	if i == 1 or i == 2:
		listbox.insert(i, "2번")
	else:
		listbox.insert(i, "%d번" %i)
listbox.delete(1, 2)
listbox.yview_scroll(10, "units")
listbox.pack()

windows.mainloop()
