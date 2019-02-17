import tkinter

windows = tkinter.Tk()
windows.title("Spinbox Test")
windows.geometry("480x320+100+100")
windows.resizable(0, 0)

label = tkinter.Label(windows, text="Input number : ", height=3)
label.pack()

def value_check(self):
	label.config(text="Input number :")
	valid = False

	if self.isdigit():
		if (int(self) <= 50 and int(self) >= 0):
			valid = True
		elif self == '':
			valid = True

	return valid

def value_error(self):
	label.config(text="You have input number is " + str(self) + "\nPlease valid input number : ")

validate_command = (windows.register(value_check), '%P')
invalid_command = (windows.register(value_error), '%P')

# state="readonly"
spinbox = tkinter.Spinbox(windows, from_=0, to=50, validate="all", state="disabled", validatecommand=validate_command, invalidcommand=invalid_command)
spinbox.pack()

windows.mainloop()
