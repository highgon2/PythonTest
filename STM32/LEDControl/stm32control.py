
import tkinter
import tkinter.ttk
import tkinter.font

import json
import queue
import screeninfo

from stm32board import *

class LEDController:
    def __init__(self):
        self.__queue      = queue.Queue()
        self.__stm32board = STM32Board();
        self.__stm32recv  = None

        app_x, app_y, app_width, app_height = 0, 0, 360, 285
        for m in screeninfo.get_monitors():
            if m.x == 0 and m.y == 0:
                app_x = (m.width - app_width) // 2
                app_y = (m.height -app_height) // 2
                break
        geometry = '{}x{}+{}+{}'.format(app_width, app_height, app_x, app_y)

        self.__root = tkinter.Tk()
        self.__root.title("STM32 LED Controlor")
        self.__root.resizable(0, 0)
        self.__root.geometry(geometry)
        self.__root.option_add("*Font", "맑은고딕 10")

        self.__init_widget();
        self.__add_widget();
        
    def __init_widget(self):
        _font = tkinter.font.Font(family="맑은고딕", size=10, weight="bold")
        self.__host = tkinter.StringVar(value="192.168.0.17")
        self.__port = tkinter.IntVar(value=3079)

        self.__lbl_host    = tkinter.Label(self.__root, font=_font, text="Host", anchor="w")
        self.__ent_host    = tkinter.Entry(self.__root, textvariable=self.__host);
        self.__lbl_port    = tkinter.Label(self.__root, font=_font, text="Port",anchor="w")
        self.__ent_port    = tkinter.Entry(self.__root, textvariable=self.__port);
        self.__btn_conn    = tkinter.Button(self.__root, text="Connect", command=self.__connect_device)
        self.__lbf_ctrl    = tkinter.LabelFrame(self.__root, text="LED List")
        self.__lbl_label   = list()
        self.__lbl_state   = list()
        self.__lbl_voltage = list()
        self.__btn_led_on  = list()
        self.__btn_led_off = list()
        self.__btn_disconn = tkinter.Button(self.__root, text="Disconnect", state="disabled")
        
        for i in range(4):
            self.__lbl_label.append(tkinter.Label(self.__lbf_ctrl, font=_font, text="LED {}".format(i+1), anchor="w"))
            self.__lbl_state.append(tkinter.Label(self.__lbf_ctrl, relief="solid"));
            self.__lbl_voltage.append(tkinter.Label(self.__lbf_ctrl, text="TBD", relief="solid"))
            self.__btn_led_on.append(tkinter.Button(self.__lbf_ctrl, text="ON"))
            self.__btn_led_off.append(tkinter.Button(self.__lbf_ctrl, text="OFF"))

    def __set_widget_config(self):
        for i in range(4):
            led = self.__stm32board.get_led("LED {}".format(i+1))
            if led.state: self.__lbl_state[i].config(bg="lightgreen")
            else:         self.__lbl_state[i].config(bg="black")

    def __add_widget(self):
        self.__lbl_host.place(x=5, y=5, width=40, height=30)
        self.__ent_host.place(x=45, y=5, width=130, height=30)
        self.__lbl_port.place(x=180, y=5, width=40, height=30)
        self.__ent_port.place(x=220, y=5, width=50, height=30)
        self.__btn_conn.place(x=275, y=5, width=75, height=30)

        relative_y = 40
        self.__lbf_ctrl.place(x=10, y=45, width=340, height=190)
        for i in range(4):
            self.__lbl_label[i].place(x=5, y=5+(i*relative_y), width=60, height=30)
            self.__lbl_state[i].place(x=60, y=5+(i*relative_y), width=50, height=30)
            self.__lbl_voltage[i].place(x=115, y=5+(i*relative_y), width=50, height=30)        
            self.__btn_led_on[i].place(x=170, y=5+(i*relative_y), width=70, height=30)
            self.__btn_led_off[i].place(x=245, y=5+(i*relative_y), width=70, height=30)
        self.__btn_disconn.place(x=260, y=245, width=90, height=30)

    def __connect_device(self):
        self.__stm32recv = STM32Receiver(self.__queue)
        if self.__stm32recv.connect(self.__host.get(), self.__port.get()):
            self.__stm32recv.start()
            self.__process_queue()

            self.__btn_conn.config(state="disabled")
            self.__btn_disconn.config(state="normal")

    def __process_queue(self):
        try:
            # {"message":"info_state","leds":[{"label":"LED 1","state":0,"voltage":0},{"label":"LED 2","state":0,"voltage":0},{"label":"LED 3","state":0,"voltage":0},{"label":"LED 4","state":1,"voltage":0}]}
            json_string = self.__queue.get(0)
            json_data = json.loads(json_string)

            if json_data.get("message") == "info_state":
                for led in json_data.get("leds"):
                    label   = led.get("label")
                    state   = led.get("state")
                    voltage = led.get("voltage")

                    if not self.__stm32board.get_led(label):
                        self.__stm32board.append_led(label, state, voltage)
                self.__set_widget_config()

        except queue.Empty:
            self.__root.after(100, self.__process_queue)


    def run(self):
        self.__root.mainloop()

if __name__ == "__main__":
    ledc = LEDController()
    ledc.run();