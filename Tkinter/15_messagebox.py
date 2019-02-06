import tkinter
import tkinter.messagebox		# Messagebox를 그릴 경우 반드시 import 해야 함

windows = tkinter.Tk()
windows.title("Messagebox Test")
windows.geometry("480x320+100+100")
windows.option_add("*Dialog.msg.font", "맑은고딕 10")
windows.resizable(0, 0)

def draw_popup():
	# tkinter.messagebox.showinfo(title="Information", message="Hello World")
	tkinter.messagebox.showwarning(title="Warning", message="Hello World")

button = tkinter.Button(windows, text="Show popup", command=draw_popup)
button.pack()

windows.mainloop()
