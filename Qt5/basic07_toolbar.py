import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon("images/exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction(QIcon("images/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save application")
        saveAction.triggered.connect(qApp.quit)

        self.statusBar()
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)
        self.toolbar = self.addToolBar("Save")
        self.toolbar.addAction(saveAction)

        self.setWindowTitle("Toolbar")
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())