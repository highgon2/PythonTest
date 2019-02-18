import tkinter
import tkinter.ttk

windows = tkinter.Tk()
windows.title("ComboBox Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

values = [str(i) + "번"  for i in range(1, 101)]

combo_box = tkinter.ttk.Combobox(windows, height=15, value=values)
combo_box.pack()

combo_box.set("목록 선택")

windows.mainloop()
