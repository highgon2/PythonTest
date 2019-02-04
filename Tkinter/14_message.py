import tkinter

windows = tkinter.Tk()
windows.title("Message Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

message = tkinter.Message(windows, text="Hello World", width=200, relief="solid")
message.pack()

windows.mainloop()
