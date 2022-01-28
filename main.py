import time
from datetime import datetime, timedelta
import threading
from speech import recognize
from api.weather import get_weather_data
from PyQt5 import QtCore, QtGui, QtWidgets
from api.gcal import gcal, create
from notification import notify

years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
         "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


class Ui_Form(object):
    def setupUi(self, Form):
        """
        UI Creation
        :param Form:
        :return:
        """
        Form.setObjectName("Form")
        Form.resize(1227, 882)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 901))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 691, 791))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_52 = QtWidgets.QLabel(self.tab_5)
        self.label_52.setGeometry(QtCore.QRect(10, 10, 371, 601))
        self.label_52.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_52.setObjectName("label_52")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_53 = QtWidgets.QLabel(self.tab_6)
        self.label_53.setGeometry(QtCore.QRect(10, 10, 371, 601))
        self.label_53.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_53.setObjectName("label_53")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_54 = QtWidgets.QLabel(self.tab_7)
        self.label_54.setGeometry(QtCore.QRect(10, 10, 371, 601))
        self.label_54.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_54.setObjectName("label_54")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_55 = QtWidgets.QLabel(self.tab_8)
        self.label_55.setGeometry(QtCore.QRect(10, 10, 371, 601))
        self.label_55.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_55.setObjectName("label_55")
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 761, 871))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.calendarWidget_13 = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget_13.setGeometry(QtCore.QRect(10, 20, 741, 541))
        self.calendarWidget_13.setObjectName("calendarWidget_13")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 90, 231, 141))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_2.setGeometry(QtCore.QRect(250, 90, 231, 141))
        self.calendarWidget_2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_2.setNavigationBarVisible(False)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget_3 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_3.setGeometry(QtCore.QRect(490, 90, 231, 141))
        self.calendarWidget_3.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_3.setNavigationBarVisible(False)
        self.calendarWidget_3.setObjectName("calendarWidget_3")
        self.calendarWidget_4 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_4.setGeometry(QtCore.QRect(10, 270, 231, 141))
        self.calendarWidget_4.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_4.setNavigationBarVisible(False)
        self.calendarWidget_4.setObjectName("calendarWidget_4")
        self.calendarWidget_5 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_5.setGeometry(QtCore.QRect(250, 270, 231, 141))
        self.calendarWidget_5.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_5.setNavigationBarVisible(False)
        self.calendarWidget_5.setObjectName("calendarWidget_5")
        self.calendarWidget_6 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_6.setGeometry(QtCore.QRect(490, 270, 231, 141))
        self.calendarWidget_6.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_6.setNavigationBarVisible(False)
        self.calendarWidget_6.setObjectName("calendarWidget_6")
        self.calendarWidget_7 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_7.setGeometry(QtCore.QRect(10, 450, 231, 141))
        self.calendarWidget_7.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_7.setNavigationBarVisible(False)
        self.calendarWidget_7.setObjectName("calendarWidget_7")
        self.calendarWidget_8 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_8.setGeometry(QtCore.QRect(490, 450, 231, 141))
        self.calendarWidget_8.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_8.setNavigationBarVisible(False)
        self.calendarWidget_8.setObjectName("calendarWidget_8")
        self.calendarWidget_9 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_9.setGeometry(QtCore.QRect(250, 450, 231, 141))
        self.calendarWidget_9.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_9.setNavigationBarVisible(False)
        self.calendarWidget_9.setObjectName("calendarWidget_9")
        self.calendarWidget_10 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_10.setGeometry(QtCore.QRect(490, 630, 231, 141))
        self.calendarWidget_10.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_10.setNavigationBarVisible(False)
        self.calendarWidget_10.setObjectName("calendarWidget_10")
        self.calendarWidget_11 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_11.setGeometry(QtCore.QRect(250, 630, 231, 141))
        self.calendarWidget_11.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_11.setNavigationBarVisible(False)
        self.calendarWidget_11.setObjectName("calendarWidget_11")
        self.calendarWidget_12 = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_12.setGeometry(QtCore.QRect(10, 630, 231, 141))
        self.calendarWidget_12.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_12.setNavigationBarVisible(False)
        self.calendarWidget_12.setObjectName("calendarWidget_12")
        self.label_36 = QtWidgets.QLabel(self.tab_4)
        self.label_36.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_4)
        self.label_37.setGeometry(QtCore.QRect(250, 70, 61, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab_4)
        self.label_38.setGeometry(QtCore.QRect(490, 70, 61, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tab_4)
        self.label_39.setGeometry(QtCore.QRect(10, 250, 61, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab_4)
        self.label_40.setGeometry(QtCore.QRect(250, 250, 61, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab_4)
        self.label_41.setGeometry(QtCore.QRect(490, 250, 61, 16))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.tab_4)
        self.label_42.setGeometry(QtCore.QRect(10, 430, 61, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.tab_4)
        self.label_43.setGeometry(QtCore.QRect(250, 430, 61, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.tab_4)
        self.label_44.setGeometry(QtCore.QRect(490, 430, 61, 16))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.tab_4)
        self.label_45.setGeometry(QtCore.QRect(10, 610, 61, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.tab_4)
        self.label_46.setGeometry(QtCore.QRect(250, 610, 61, 16))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.tab_4)
        self.label_47.setGeometry(QtCore.QRect(490, 610, 61, 16))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.tab_4)
        self.label_48.setGeometry(QtCore.QRect(290, 10, 81, 51))
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(810, 140, 51, 21))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(850, 140, 81, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setObjectName("dateEdit")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(980, 70, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(810, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(850, 170, 81, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1010, 110, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(980, 40, 71, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(810, 210, 47, 13))
        self.label_7.setObjectName("label_7")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(810, 280, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(810, 170, 51, 21))
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(820, 230, 141, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1020, 190, 81, 111))
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(810, 390, 281, 311))
        self.label_35.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_35.setObjectName("label_35")
        self.label_49 = QtWidgets.QLabel(Form)
        self.label_49.setGeometry(QtCore.QRect(810, 340, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(Form)
        self.label_50.setGeometry(QtCore.QRect(1040, 40, 101, 21))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(Form)
        self.label_51.setGeometry(QtCore.QRect(1040, 70, 101, 21))
        self.label_51.setObjectName("label_51")
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_2.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_3.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_4.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_5.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_6.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_7.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_8.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_9.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_10.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_11.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget_12.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(280, 5, 90, 40))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(years)
        timer = QtCore.QTimer(Form)
        timer.timeout.connect(self.showTimeThread)
        timer2 = QtCore.QTimer(Form)
        timer2.setInterval(1000 * 3600 * 60)
        timer2.timeout.connect(self.showWeatherThread)
        timer.start(1000)
        timer2.start(1000 * 3)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        UI Initialization Configuration
        :param Form:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Smart Calendar App"))
        self.comboBox.setCurrentText(_translate("Form", "2022"))
        self.label_52.setText(_translate("Form", "Empty"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("Form", "Today"))
        self.label_53.setText(_translate("Form", "Empty"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("Form", "Next 7 Days"))
        self.label_54.setText(_translate("Form", "Empty"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("Form", "Next 30 Days"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("Form", "From Google"))
        self.label_55.setText(_translate("Form", "Empty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Agenda"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "Month"))
        self.label_36.setText(_translate("Form", "January"))
        self.label_37.setText(_translate("Form", "February"))
        self.label_38.setText(_translate("Form", "March"))
        self.label_39.setText(_translate("Form", "May"))
        self.label_40.setText(_translate("Form", "May"))
        self.label_41.setText(_translate("Form", "June"))
        self.label_42.setText(_translate("Form", "July"))
        self.label_43.setText(_translate("Form", "August"))
        self.label_44.setText(_translate("Form", "September"))
        self.label_45.setText(_translate("Form", "October"))
        self.label_46.setText(_translate("Form", "November"))
        self.label_47.setText(_translate("Form", "December"))
        # self.label_48.setText(_translate("Form", "2021"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Calendar"))
        self.label_5.setText(_translate("Form", "Date:"))
        # self.label_9.setText(_translate("Form", "Weather   :"))
        self.label_4.setText(_translate("Form", "Add Reminder:"))
        self.pushButton.setText(_translate("Form", "🎤"))
        # self.label_8.setText(_translate("Form", "Time         :"))
        self.label_7.setText(_translate("Form", "Task:"))
        self.label_6.setText(_translate("Form", "Time:"))
        self.label.setText(_translate("Form", "Speech"))
        self.label_35.setText(_translate("Form", "Empty"))
        self.label_49.setText(datetime.today().strftime("%m/%d/%Y"))
        self.label_50.setText(_translate("Form", "TimeVariable"))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("""
    QLabel {
        color: red;
    }
    """)
        self.label_51.setText(_translate("Form", "Getting Weather..."))
        self.pushButton.clicked.connect(self.rec_thread)
        self.dateEdit.setDate(datetime.today())
        self.calendarWidget_13.clicked.connect(self.clickDateThread)
        self.update()
        self.buttonBox.accepted.connect(self.addCalendar)
        self.comboBox.activated.connect(self.update)

    def rec_thread(self):
        """
        Start Speech Recognition Thread
        :return:
        """
        x = threading.Thread(target=self.recognizer)
        x.start()
    def recognizer(self):
        """
        Say, "Thing" today/tomorrow at "time"
        e.g. "Buy a milk today at 6:30pm"

        Crate Events With Voice
        Currently, it only works for Today and Tomorrow
        :return:
        """
        self.label.setText("Listening...")
        r_text = recognize()
        self.label.setText(r_text)
        print(r_text)
        summary = None
        date = datetime.now()
        time = None
        if "today at" in r_text:
            summary = r_text.split("today at")[0]
            time = r_text.split("today at")[1]

        if "tomorrow at" in r_text:
            summary = r_text.split("tomorrow at")[0]
            time = r_text.split("tomorrow at")[1]
            date = datetime.now()+timedelta(days=1)

        file = open('events', 'a')
        text = date.strftime('%m/%d/%Y') +"#"+time+"#"+summary
        file.writelines(text + '\n')
        file.close()
        self.update()

    def update(self):
        """
        Thread for updating the Complete UI
        :return:
        """
        x = threading.Thread(target=self.updateAll)
        x.start()

    def updateAll(self):
        """
        Updating the Complete UI
        :return:
        """
        self.showTodayCal()
        self.showTodayAgenda()
        self.showWeekAgenda()
        self.showMonthAgenda()
        self.changeYear()
        self.cloud_showAgenda()

    def changeYear(self):
        """
        Change the Year for Year-view
        :return:
        """
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "01" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "02" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_2.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "03" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_3.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "04" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_4.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "05" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_5.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "06" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_6.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "07" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_7.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "08" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_8.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "09" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_9.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "10" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_10.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "11" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_11.setSelectedDate(qtDate)
        qtDate = QtCore.QDate.fromString(self.comboBox.currentText() + "-" + "12" + "-" + "01", 'yyyy-MM-dd')
        self.calendarWidget_12.setSelectedDate(qtDate)

    def addCalendar(self):
        """
        Create Local Event
        :return:
        """
        file = open('events', 'a')
        summary = self.timeEdit.text()
        if summary == "": summary = "Untitled"
        text = self.dateEdit.date().toPyDate().strftime(
            '%m/%d/%Y') + "#" + summary + "#" + self.plainTextEdit.toPlainText()
        file.writelines(text + '\n')
        file.close()
        self.update()

    def showTodayCal(self):
        self.label_49.setText(datetime.today().strftime("%m/%d/%Y"))
        """
        Show today's agenda in Main Window - Sidebar
        :return:
        """
        events = self.checkEvents()
        string = ""
        for event in events:
            string += event.split("#")[1] + " " + event.split("#")[2] + "\n"
        self.label_35.setText(string)

    def showTodayAgenda(self):
        """
        Show today's agenda in agenda view
        :return:
        """
        events = self.checkEvents()
        string = ""
        for event in events:
            string += event.split("#")[1] + " " + event.split("#")[2]+"\n"
        self.label_52.setText(string)



    def showMonthAgenda(self):
        """
        Show month's agenda in agenda view
        :return:
        """
        events = self.checkEvents(duration=30)
        string = ""
        for event in events:
            string += event
        self.label_53.setText(string)



    def showWeekAgenda(self):
        """
        Show week's agenda in agenda view
        :return:
        """
        events = self.checkEvents(duration=7)
        string = ""
        for event in events:
            string += event
        self.label_54.setText(string)

    def cloud_showAgenda(self):
        """
        Show events from Google in From Google View
        returns date and time in UTC+iso format
        :return:
        """
        day = datetime.utcnow().isoformat()
        lst = gcal()
        string = ""
        for l in lst:
            string += l[0] + " " + l[1] + "\n"
        self.label_55.setText(string)

    def showTimeThread(self):
        """
        Thread for the clock
        :return:
        """
        x = threading.Thread(target=self.showTime)
        x.start()

    def showTime(self):
        """
        Show Red Coloured time in the main UI
        :return:
        """
        # 01/19/2022#12:00 AM#
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('h:mm:ss')
        string=datetime.today().strftime("%m/%d/%Y")+"#"+label_time[:4]
        event = self.checkEventForNotification(string)
        if event and label_time[5:]=="00":
            notify(event.split("#")[1],event)
            return self.update()

        self.label_50.setText(label_time)

    def checkEventForNotification(self, string):
        """
        Check if current time and any event time matches or not
        :param string:
        :return:
        """
        file = open('events','r')
        read = file.readlines()
        for line in read:
            if string in line:
                return line
        return False

    def clickDateThread(self):
        """
        Thread for finding Events
        :return:
        """
        x = threading.Thread(target=self.clickDate)
        x.start()

    def clickDate(self):
        """
        Function for next events after clicking a particular date in monthly calendar
        :return:
        """
        self.label_49.setText(self.calendarWidget_13.selectedDate().toString("MM/dd/yyyy"))
        self.dateEdit.setDate(self.calendarWidget_13.selectedDate())
        self.showOnDate()



    def showOnDate(self):
        """
        Function for showing  events after clicking a particular date in monthly calendar
        :return:
        """
        date = self.calendarWidget_13.selectedDate().toPyDate().strftime('%m/%d/%Y')
        events = self.checkEvents(date=date)
        string = ""
        for event in events:
            string += event.split("#")[1] + " " + event.split("#")[2] + "\n"
        self.label_35.setText(string)

    def showWeatherThread(self):
        """
        Thread for showing weather
        :return:
        """
        x = threading.Thread(target=self.showWeather)
        x.start()

    def showWeather(self):
        """
        Show Current Temperature in Fahrenheit
        :return:
        """
        current_temp = get_weather_data()
        self.label_51.setText(str(current_temp) + "° F")

    def checkEvents(self, duration=None, date=None):
        """
        Function for checking Events in a particular interval
        :param: duration (int), date (date)
        :return:
        """
        if duration == None and date == None:
            date = datetime.today().strftime('%m/%d/%Y')
            return self.checkOnDate(date)
        elif duration is None and date is not None:
            return self.checkOnDate(date)

        if duration is not None:
            lst = []
            for d in range(0, duration + 1):
                date = datetime.today() + timedelta(days=d)
                date = date.strftime('%m/%d/%Y')
                eventsOneDay = self.checkOnDate(date)
                for event in eventsOneDay:
                    lst.append(event)
            return lst

    def checkOnDate(self, date):
        """
        function for retrieving events on a particular date
        :param date:
        :return:
        """
        file = open('events', 'r')
        events = file.readlines()
        lst = []

        for event in events:
            if event.split("#")[0] == date:
                lst.append(event)
        return lst


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

"""
Functions which will be useful for date-interval-based events collection from Google Calendar
"""
'''
    def cloud_showOnDate(self):
        lst = gcal(onlyTime=True, date=self.calendarWidget_13.selectedDate().toPyDate().isoformat() + 'T00:00:00.00000',
                   days=0)
        for l in lst:
            self.label_35.setText(l[0] + " " + l[1] + "\n")
    
    def cloud_clickDate(self):
        x = threading.Thread(target=self.showOnDate)
        x.start()
        self.dateEdit.setDate(self.calendarWidget_13.selectedDate())
        self.label_49.setText(self.calendarWidget_13.selectedDate().toString("dd/MM/yyyy"))
        print(self.calendarWidget_13.selectedDate().toPyDate().isoformat() + 'T00:00:00.00000')
    
    def cloud_showMonthAgenda(self):
        lst = gcal(onlyTime=False, days=30)
        string = ""
        for l in lst:
            string += l[0] + " " + l[1] + "\n"
        self.label_53.setText(string)

    def cloud_showTodayCal(self):
        lst = gcal(onlyTime=True)
        string = ""
        for l in lst:
            string += l[0] + " " + l[1] + "\n"
        self.label_35.setText(string)

    def cloud_showTodayAgenda(self):
        lst = gcal(onlyTime=True)
        string = ""
        for l in lst:
            string += l[0] + " " + l[1] + "\n"
        self.label_52.setText(string)
'''