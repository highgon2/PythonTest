import tkinter

windows = tkinter.Tk()
windows.title("Scrollbar Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

frame = tkinter.Frame(windows)

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
for line in range(1, 1001):
	listbox.insert(line, str(line) + " / 1000")
listbox.pack(side="left")

scrollbar["command"] = listbox.yview
frame.pack()

windows.mainloop()
