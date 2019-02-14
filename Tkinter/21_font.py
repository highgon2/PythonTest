import tkinter
import tkinter.font

windows = tkinter.Tk()
windows.title("Font Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

font = tkinter.font.Font(family="맑은고딕", size=20, slant="italic")

label = tkinter.Label(windows, text="파이썬 3.6", font=font)
label.pack()

windows.mainloop()
