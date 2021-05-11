import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My First Application")
        self.move(300, 300)
        self.resize(400, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())