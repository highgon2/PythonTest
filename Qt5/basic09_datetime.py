import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()
print(now.toString())
print(now.toString("d.M.yy"))
print(now.toString("dd.MM.yyyy"))
print(now.toString("dd.MMMM.yyyy"))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

time_now = QTime.currentTime()
print(time_now.toString())
print(time_now.toString("h.m.s"))
print(time_now.toString("hh:mm:ss"))
print(time_now.toString(Qt.DefaultLocaleLongDate))
print(time_now.toString(Qt.DefaultLocaleShortDate))

date_time = QDateTime.currentDateTime()
print(date_time.toString())
print(date_time.toString("d.M.yy hh:mm:ss"))
print(date_time.toString("dd.MM.yy, hh:mm:ss"))
print(date_time.toString(Qt.DefaultLocaleLongDate))
print(date_time.toString(Qt.DefaultLocaleShortDate))

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle("Date")
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())