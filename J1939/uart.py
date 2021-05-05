import time
import serial
import threading

class Protocol(threading.Thread):
    def __init__(self, port, queue):
        threading.Thread.__init__(self)
        device = str(port).split("-")[0].strip()

        self.__is_run  = 1
        self.__queue   = queue
        self.__serial = serial.Serial(device, 115200, timeout=0)
        # self.__serial = serial.Serial("/dev/ttyUSB0", 115200, timeout=0)

    def tx_message(self, message):
        for c in message:
            self.__serial.write(c.encode())
            time.sleep(0.005)
        self.__serial.write(b'\r')

    def run(self):
        buf   = list()
        null  = bytes(0x00)
        count = 0
        while self.__is_run:
            c = self.__serial.read()
            if c == null: continue

            # print(c)
            buf.append(c.decode("utf-8"))
            if buf[len(buf)-2] == '\r' and buf[len(buf)-1] == '\n':
                s = "".join(buf)
                if s.find("PCAN_") < 0:
                    # print("RECV({}) :: {}".format(len(s), s))
                    self.__queue.put(s)
                buf.clear()

    def stop(self):
        self.__is_run = False

    def close(self):
        for c in "rst":
            self.__serial.write(c.encode())
            time.sleep(0.005)
        self.__serial.write(b'\r')
        self.__serial.close()

