import tkinter
import tkinter.ttk as ttk

class Parameter(tkinter.Frame):
    def __init__(self, index, frame):
        row_index = ((int)(index / 3) * 9) + 2
        col_index = (index % 3) * 10
        
        self.__root     = frame
        self.__index    = index

        self.__json     = None
        self.__spn_list = [None for _ in range(8)]
        self.__val_list = [None for _ in range(8)]
        self.__lbl_list = [None for _ in range(8)]
        self.__ent_list = [None for _ in range(8)]

        self.__lbl_can  = tkinter.Label(self.__root, text="CAN ID", anchor="w")
        self.__cmb_para = ttk.Combobox(self.__root, state="readonly")
        self.__cmb_para.bind("<<ComboboxSelected>>", self.__cb_event_para_selected)

        for i in range(8):
            self.__spn_list[i] = tkinter.StringVar(value="")
            self.__val_list[i] = tkinter.StringVar()
            self.__lbl_list[i] = tkinter.Label(self.__root, textvariable=self.__spn_list[i], anchor="w")
            self.__ent_list[i] = tkinter.Entry(self.__root, textvariable=self.__val_list[i], state="readonly", readonlybackground="white")

            # self.__lbl_list[i].grid(row=i+1, column=0, columnspan=4, sticky="news", padx=5, pady=2)
            # self.__ent_list[i].grid(row=i+1, column=4, columnspan=6, sticky="news", padx=5, pady=1)

        for i in range(10):
            self.__root.columnconfigure(i, pad=1)
            self.__root.columnconfigure(i, weight=1)

        self.__lbl_can.grid(row=0, column=0, columnspan=4, sticky="news", padx=5, pady=1)
        self.__cmb_para.grid(row=0, column=4, columnspan=6, sticky="news", padx=5, pady=1)
        self.__root.grid(row=row_index, column=col_index, rowspan=9, columnspan=10, sticky="news",padx=1, pady=5)
    
    def __cb_event_para_selected(self, event):
        for i in range(8):
            self.__spn_list[i].set("")
            self.__val_list[i].set("")
            self.__lbl_list[i].grid_forget()
            self.__ent_list[i].grid_forget()

        # if self.__uart and self.__cmb_para.get() != "":
        #     self.__uart.tx_message("PCAN_" + self.__cmb_para.get())

    @property
    def parameter(self):
        return self.__cmb_para.get()

    def set_json(self, json_data):
        if self.__json == json_data:
            print("{} : same json data".format(self.__index))
            return

        for i in range(8):
            self.__spn_list[i].set("")
            self.__val_list[i].set("")
            self.__lbl_list[i].grid_forget()
            self.__ent_list[i].grid_forget()

        obj      = json_data.get(self.__cmb_para.get())
        key_list = list(obj.keys())
        for i, key in enumerate(key_list):
            self.__spn_list[i].set(key)
            self.__val_list[i].set(obj.get(key))

            self.__lbl_list[i].grid(row=i+1, column=0, columnspan=4, sticky="news", padx=5, pady=2)
            self.__ent_list[i].grid(row=i+1, column=4, columnspan=6, sticky="news", padx=5, pady=1)

    def update_parameter_list(self, para_list):
        if not para_list:
            self.__cmb_para.set("")
            self.__cmb_para.config(values=list())

            for i in range(8):
                self.__spn_list[i].set("")
                self.__val_list[i].set("")
                self.__lbl_list[i].grid_forget()
                self.__ent_list[i].grid_forget()
        else:
            self.__cmb_para.config(values=para_list)
            if self.__index == 0:   self.__cmb_para.set("AMB")
            elif self.__index == 1: self.__cmb_para.set("AT1T1I")
            elif self.__index == 2: self.__cmb_para.set("DPFC1")
            elif self.__index == 3: self.__cmb_para.set("EEC1")
            elif self.__index == 4: self.__cmb_para.set("EFLP1")
            elif self.__index == 5: self.__cmb_para.set("ET1")
