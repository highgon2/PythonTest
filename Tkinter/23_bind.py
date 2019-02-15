import tkinter

windows = tkinter.Tk()
windows.title("Bind Test")
windows.geometry("640x480+100+100")
windows.resizable(1, 1)

width = 1

def drawing(event):
	if width > 0:
		x1 = event.x - 1
		y1 = event.y - 1
		x2 = event.x + 1
		y2 = event.y + 1
		canvas.create_oval(x1, y1, x2, y2, fill="cyan", width=width)

def scroll(event):
	global width

	# print("scroll : event.num = %d, event.delta = %d" %(event.num, event.delta))
	# Windows OS : event.delta
	# Linux OS   : event.num
	if event.num == 4 or event.delta == 120:
		# print("up")
		width += 1

	if event.num == 5 or event.delta == -120:
		# print("down")
		width -= 1

	label.config(text=str(width))

canvas = tkinter.Canvas(windows, relief="solid", bd=2)
canvas.pack(expand=True, fill="both")
canvas.bind("<B1-Motion>", drawing)
# Windows 
# canvas.bind("<MouseWheel>", scroll)
# Linux
canvas.bind("<Button-4>", scroll)
canvas.bind("<Button-5>", scroll)

label = tkinter.Label(windows, text=str(width))
label.pack()

windows.mainloop()
