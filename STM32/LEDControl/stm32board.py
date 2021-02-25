import queue
import socket
import threading

class STM32LED:
    def __init__(self, label, state, voltage):
        self.__label   = label
        self.__state   = state
        self.__voltage = voltage

    @property
    def label(self):
        return self.__label

    @property
    def state(self):
        return self.__state

    @property
    def voltage(self):
        return self.__voltage

    @state.setter
    def state(self, state):
        self.__state = state

    @voltage.setter
    def voltage(self, voltage):
        self.__voltage = voltage

class STM32Board:
    def __init__(self):
        self.__led_list = list()

    def get_led(self, label):
        for led in self.__led_list:
            if label == led.label:
                return led
        return None

    def append_led(self, label, state, voltage):
        self.__led_list.append(STM32LED(label, state, voltage))
        
class STM32Receiver(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.daemon = True
        
        self.__queue  = queue
        self.__socket = None
    
    def connect(self, ip, port):
        try :
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect((ip, port));
        except Exception as e:
            print(e)
            return False
        return True

    def run(self):
        while(1):
            data = self.__socket.recv(1024)
            self.__queue.put(data.decode())
            print("received :", data.decode())
        self.__socket.close()


if __name__ == "__main__":
    b = STM32Board()
    b.get_led("a")