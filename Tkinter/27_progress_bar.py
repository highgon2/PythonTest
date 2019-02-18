import tkinter
import tkinter.ttk

windows = tkinter.Tk()
windows.title("Progressbar Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

progress_bar = tkinter.ttk.Progressbar(windows, maximum=100, mode="indeterminate")
progress_bar.pack()
progress_bar.start(50)

windows.mainloop()
