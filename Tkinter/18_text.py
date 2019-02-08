import tkinter

windows = tkinter.Tk()
windows.title("Text Test")
windows.geometry("480x320+100+100")
windows.resizable(1, 1)

text = tkinter.Text(windows)
text.insert(tkinter.CURRENT, "안녕하세요.\n")
text.insert("current", "Nce meet you")
text.insert(2.1, "i")
text.pack()

text.tag_add("강조", "1.0", "1.6")
text.tag_config("강조", background="yellow")
text.tag_remove("강조", "1.1", "1.2")

windows.mainloop()
