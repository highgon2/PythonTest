import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")

        self.setWindowTitle("Statusbar")
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == "__main__":
    app    = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())
    