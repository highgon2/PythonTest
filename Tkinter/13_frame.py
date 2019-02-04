import tkinter

windows = tkinter.Tk()
windows.title("Frame Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

frame1 = tkinter.Frame(windows, relief="solid", bd=10)
frame1.pack(side="left", fill="both", expand=True)

frame2 = tkinter.Frame(windows, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

button1 = tkinter.Button(frame1, text="Frame1")
button1.pack(side="right")

button2 = tkinter.Button(frame2, text="Frame2")
button2.pack(side="left")

windows.mainloop()
