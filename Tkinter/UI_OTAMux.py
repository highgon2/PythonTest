import os
import time

import tkinter
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox

sw_ver = 0x0099
path = ""
file_name = ""
file_path = ""
output_file = ""

windows = tkinter.Tk()
windows.title("Handan OTA TS Generator v%x.%02x" %((sw_ver >> 8), (sw_ver & 0x00FF)))
windows.geometry("430x300+100+100")
windows.resizable(0, 0)

ts_mode = tkinter.IntVar()
progress = tkinter.IntVar()

windows.option_add("*Font", "맑은고딕 10")
# windows.option_add("*Dialog.msg.font", "맑은고딕 10")

def file_open():
	# if cmb_header.get() == "DN Header":
	# 	tkinter.messagebox.showwarning(title="Warning", message="Please select download header type")
	# 	return
		
	file_path = tkinter.filedialog.askopenfilename(initialdir=".", filetypes=(("bin files", "*.bin"), ("all files", "*.*")), title="Choose a file")
	path, file_name = os.path.split(file_path)

	output = file_name.split("_")
	output_file = output[1] + "_OTA.bin"

	entry_file.delete(0, tkinter.END)
	entry_file.insert(0, file_name)

	entry_output.delete(0, tkinter.END)
	entry_output.insert(0, output_file)
	# print(path)

def radio_event():
	if ts_mode.get() == 1:
		spin_ota_pid.config(state="normal")
	else:
		spin_ota_pid.config(state="disabled")

def btn_convert_event():
	btn_convert.config(state="disabled")
	for i in range(0, 101):
		progress.set(i)
		time.sleep(0.01)
		windows.update_idletasks()
	btn_convert.config(state="normal")

# cmb_value = ["Plaintext", "Encrypted"]
# cmb_header = tkinter.ttk.Combobox(windows, value=cmb_value, state="readonly", font=("맑은고딕 9 bold"))
# cmb_header.place(x=10, y=10, width=85, height=30)
# cmb_header.set("DN Header")

# if state is readonly or disabled, insert() and delete() method does not executed
entry_file = tkinter.Entry(windows)
entry_file.place(x=10, y=10, width=355, height=30)

btn_file = tkinter.Button(windows, text="File", command=file_open)
btn_file.place(x=370, y=10, height=30)

labelframe = tkinter.LabelFrame(windows, text="options")
labelframe.place(x=10, y=45, width=410, height=180)

lbl_hw = tkinter.Label(labelframe, text="H/W version")
lbl_hw.place(x=10, y=0)

entry_hw_model = tkinter.Entry(labelframe, justify="center")
entry_hw_model.place(x=10, y=25, width=40, height=30)

entry_hw_version = tkinter.Entry(labelframe, justify="center")
entry_hw_version.place(x=50, y=25, width=40, height=30)

lbl_sw = tkinter.Label(labelframe, text="S/W version")
lbl_sw.place(x=105, y=0)

entry_sw_model = tkinter.Entry(labelframe, justify="center")
entry_sw_model.place(x=105, y=25, width=40, height=30)

entry_sw_version = tkinter.Entry(labelframe, justify="center")
entry_sw_version.place(x=145, y=25, width=40, height=30)

lbl_ota_pid = tkinter.Label(labelframe, text="OTA PID(Decimal)")
lbl_ota_pid.place(x=200, y=0)

spin_ota_pid = tkinter.Spinbox(labelframe, from_=32, to=8191, state="disabled")
spin_ota_pid.place(x=200, y=25, width=115, height=30)

lbl_ota_mux = tkinter.Label(labelframe, text="Mux Rate")
lbl_ota_mux.place(x=330, y=0)

spin_ota_mux = tkinter.Spinbox(labelframe, from_=2, to=10, state="readonly")
spin_ota_mux.place(x=330, y=25, width=60, height=30)

radio_psi = tkinter.Radiobutton(labelframe, text="PSI mode", value=0, variable=ts_mode, command=radio_event)
radio_psi.place(x=0, y=70)

radio_psi = tkinter.Radiobutton(labelframe, text="TS mode", value=1, variable=ts_mode, command=radio_event)
radio_psi.place(x=95, y=70)

lbl_output = tkinter.Label(labelframe, text="Output File")
lbl_output.place(x=10, y=110, width=90, height=30)

entry_output = tkinter.Entry(labelframe)
entry_output.place(x=100, y=110, width=290, height=30)

progress_bar = tkinter.ttk.Progressbar(windows, maximum=100, variable=progress)
progress_bar.place(x=10, y=240, width=410, height=10)

btn_convert = tkinter.Button(windows, text="TS Generator", command=btn_convert_event)
btn_convert.place(x=230, y=260, width=190, height=30)

windows.mainloop()
