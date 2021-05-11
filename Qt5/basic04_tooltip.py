import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('맑은고딕', 10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle("Tooltip")
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == "__main__":
    app    = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())
    