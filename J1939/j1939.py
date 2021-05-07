import os
import sys
import json

import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

import queue
import serial
import serial.tools.list_ports as sp
import screeninfo

import uart
import j1939_data

class J1939(tkinter.Frame):
    def __init__(self, root):
        if sys.platform == "win32":
            app_x, app_y, app_width, app_height = 0, 0, 1200, 610
        else:
            app_x, app_y, app_width, app_height = 0, 0, 1200, 620

        for m in screeninfo.get_monitors():
            if m.x == 0 and m.y == 0:
                app_x = (m.width - app_width) // 2
                app_y = (m.height -app_height) // 2
                break
        geometry = "{}x{}+{}+{}".format(app_width, app_height, app_x, app_y)

        self.__root = root
        self.__root.resizable(0, 0)
        self.__root.geometry(geometry)
        self.__root.title("J1939 Monitor")
        self.__root.option_add("*Font", "맑은고딕 10")

        try:
			# sys.MEIPASS is temp directory for pyinstaller
            icon_path = os.path.join(getattr(sys, '_MEIPASS'), "j1939.png")
        except:
            icon_path = os.path.join(os.path.abspath("."), "j1939.png")
        self.__root.iconphoto(True, tkinter.PhotoImage(file=icon_path))    

        self.__can_list   = [tkinter.StringVar() for _ in range(6)]
        self.__para_list  = [None for _ in range(6)]

        self.__uart       = None
        self.__queue      = queue.Queue()
        self.__con_string = tkinter.StringVar(value="Connect")
        self.__ucount     = 0

        self.__lbl_port = tkinter.Label(self.__root, text="Serial Port", anchor="e")
        self.__cmb_port = ttk.Combobox(self.__root, values=sp.comports())
        self.__btn_conn = tkinter.Button(self.__root, textvariable=self.__con_string, command=self.__cb_btn_conn)
        self.__seperat1 = ttk.Separator(self.__root, orient="horizontal")

        for i in range(30):
            if i < 20:
                self.__root.rowconfigure(i, pad=1)
                self.__root.rowconfigure(i, weight=1)
                self.__root.rowconfigure(i, minsize=30)

            self.__root.columnconfigure(i, pad=1)
            self.__root.columnconfigure(i, weight=1)
            self.__root.columnconfigure(i, minsize=40)

        self.__lbl_port.grid(row=0, column=20, columnspan=3, sticky="news", padx=1,pady=3)
        self.__cmb_port.grid(row=0, column=23, columnspan=4, sticky="news", padx=1,pady=3)
        self.__btn_conn.grid(row=0, column=27, columnspan=3, sticky="news", padx=1,pady=3)
        self.__seperat1.grid(row=1, column=0, columnspan=30, sticky="ew")

        for i in range(6): self.__para_list[i] = j1939_data.Parameter(i, tkinter.LabelFrame(self.__root, text="Parameter {}".format(i)))

    def __update_data(self):
        if self.__queue.qsize() > 0:
            json_string = self.__queue.get()
            try:
                j_data   = json.loads(json_string)
                key_list = list(j_data.keys())
                if "CAN_ID" in key_list:
                    for i in range(6): self.__para_list[i].update_parameter_list(list(j_data.get("CAN_ID")))
                else:
                    for i in range(6):
                        if key_list[0] == self.__para_list[i].parameter:
                            self.__para_list[i].set_json(j_data)
            except json.JSONDecodeError as e:
                print("JSONDecodeError")
                print("json_string :", json_string)
            except Exception as e:
                print(e.with_traceback())
        else:
            if self.__uart: 
                self.__uart.tx_message("PCAN_" + self.__para_list[self.__ucount%6].parameter)
                self.__ucount += 1
        self.__root.after(50, self.__update_data)

    def __cb_btn_conn(self):
        if self.__con_string.get() == "Connect":
            try:
                self.__uart = uart.Protocol(self.__cmb_port.get(), self.__queue)
                self.__uart.daemon = True
                self.__uart.start()
                self.__uart.tx_message("PCAN_ID")
                self.__root.after(50, self.__update_data)
                self.__con_string.set("Disconnect")
            except serial.SerialException as e:
                messagebox.showerror(title="ERROR", message="Serial port can't connect : {}".format(self.__cmb_port.get()))
        else:
            self.__uart.stop()
            self.__uart.join()
            self.__uart.close()
            self.__uart = None
            self.__ucount = 0
            self.__con_string.set("Connect")

            for i in range(6):
                self.__can_list[i].set("")
                self.__para_list[i].update_parameter_list(None)

if __name__ == "__main__":
    root = tkinter.Tk()
    j1939 = J1939(root)
    root.mainloop()
