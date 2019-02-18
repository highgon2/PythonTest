import tkinter
import tkinter.filedialog

windows = tkinter.Tk()
windows.title("FileDialog Test")
windows.geometry("640x320+100+100")
windows.resizable(0, 0)

def fopen():
	file_path = tkinter.filedialog.askopenfilename(initialdir=".", filetypes=(("bin files", "*.bin"), ("all files", "*.*")), title="Choose a file")
	file_name = file_path.split("/")
	print(file_name[-1])
	label.config(text=file_path) 

button = tkinter.Button(windows, text="file open", command=fopen)
button.pack()

label = tkinter.Label(windows)
label.pack()

windows.mainloop()
