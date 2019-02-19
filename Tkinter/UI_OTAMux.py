import os
import tkinter
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox

sw_ver = 0x0099
path = ""
file_name = ""
file_path = ""

windows = tkinter.Tk()
windows.title("Handan OTA TS Generator v%x.%02x" %((sw_ver >> 8), (sw_ver & 0x00FF)))
windows.geometry("520x300+100+100")
windows.resizable(0, 0)

windows.option_add("*Dialog.msg.font", "맑은고딕 10")

def file_open():
	if cmb_header.get() == "DN Header":
		tkinter.messagebox.showwarning(title="Warning", message="Please select download header type")
		return
		
	file_path = tkinter.filedialog.askopenfilename(initialdir=".", filetypes=(("bin files", "*.bin"), ("all files", "*.*")), title="Choose a file")
	path, file_name = os.path.split(file_path)

	entry_file.delete(0, tkinter.END)
	entry_file.insert(0, file_name)
	# print(path)

cmb_value = ["Plaintext", "Encrypted"]
cmb_header = tkinter.ttk.Combobox(windows, value=cmb_value, state="readonly")
cmb_header.place(x=10, y=10, width=85, height=30)
cmb_header.set("DN Header")

# if state is readonly or disabled, insert() and delete() method does not executed
entry_file = tkinter.Entry(windows)
entry_file.place(x=100, y=10, width=355, height=30)

btn_file = tkinter.Button(windows, text="File", command=file_open)
btn_file.place(x=460, y=10, height=30)

windows.mainloop()
