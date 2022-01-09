import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget

from Event import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.current_date = datetime.now().date
        self.title = " Smart Calender Application"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 500

        self.CalendarUI()
        self.Initwindow()

    def Initwindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def CalendarUI(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setFixedWidth(400)
        self.calendar.setFixedHeight(300)
        self.calendar.move(100, 100)
        self.calendar.setGridVisible(False)
        self.calendar.setSelectedDate(datetime.now())
        self.calendar.clicked.connect(self.get_selected_date)

    def get_selected_date(self, qDate):
        Event.add_reminder(qDate)





App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())
