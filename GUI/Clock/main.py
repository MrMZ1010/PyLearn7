import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QPushButton, QMessageBox, QToolTip
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt
from functools import partial
from my_time import MyTime
from timer import TimerThread
from stopwatch import StopWatchThread
from world_clock import WorldTimeThread
from main_window import Ui_MainWindow
from database import Database
from plyer import notification
from alarm import Alarm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_variables()
        self.setup_fonts()
        self.setup_ui_elements()
        self.setup_connections()

    def initialize_variables(self):
        self.array = [0, 0, 0]
        self.mylist = []
        self.del_list = []
        self.active_alarm_list = []
        self.labels = []
        self.alarm_time_list = []
        self.alarm_date_list = []
        self.date_list = []
        self.edit_list = []
        self.db = Database()
        self.read_from_database()

    def setup_fonts(self):
        id = QFontDatabase.addApplicationFont("Seven Segment.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        date_list = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.ui.comboBox.addItems(date_list)
        QToolTip.setFont(QFont('Arial', 13))

    def setup_ui_elements(self):
        self.ui.comboBox.activated.connect(self.current_text)
        self.ui.label_stopwatch.setText("0:0:0")
        self.ui.textbox_hour_timer.setText("0")
        self.ui.textbox_minute_timer.setText("0")
        self.ui.textbox_second_timer.setText("0")

    def setup_connections(self):
        self.thread_stopwatch = StopWatchThread()
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)
        self.thread_stopwatch.signal_send.connect(self.show_time_stopwatch)

        self.thread_timer = TimerThread()
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.thread_timer.signal_send.connect(self.show_time_timer)

        self.ir_time_thread = WorldTimeThread()
        self.gr_time_thread = WorldTimeThread()
        self.us_time_thread = WorldTimeThread()
        self.start_Wclock()

        self.ir_time_thread.signal_send_i.connect(self.show_time_Wclock1)
        self.gr_time_thread.signal_send_g.connect(self.show_time_Wclock2)
        self.us_time_thread.signal_send_u.connect(self.show_time_Wclock3)

        self.alarm_thread = Alarm()
        self.alarm_thread.start()
        self.ui.btn_new_alarm.clicked.connect(self.new_alarm)

    def current_text(self, _):
        global ctext
        ctext = self.ui.comboBox.currentText()
        print("Current text", ctext)
        return ctext

    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
        self.ui.label_stopwatch.setText("0:0:0")

    def show_time_stopwatch(self, time):
        self.ui.label_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")

    def start_timer(self):
        hour = int(self.ui.textbox_hour_timer.text())
        minute = int(self.ui.textbox_minute_timer.text())
        second = int(self.ui.textbox_second_timer.text())
        self.thread_timer.get(hour, minute, second)
        self.thread_timer.start()

    def stop_timer(self):
        self.thread_timer.terminate()

    def reset_timer(self):
        self.thread_timer.reset()
        self.ui.textbox_hour_timer.setText(str(self.thread_timer.time.hour))
        self.ui.textbox_minute_timer.setText(str(self.thread_timer.time.minute))
        self.ui.textbox_second_timer.setText(str(self.thread_timer.time.second))

    def show_time_timer(self, time):
        self.ui.textbox_hour_timer.setText(str(time.hour))
        self.ui.textbox_minute_timer.setText(str(time.minute))
        self.ui.textbox_second_timer.setText(str(time.second))
        if time.hour == 0 and time.minute == 0 and time.second == 0:
            self.thread_timer.terminate()
            notification.notify(title="Alarm Clock", message="Time is Over")

    def start_Wclock(self):
        self.ir_time_thread.start()
        self.gr_time_thread.start()
        self.us_time_thread.start()

    def show_time_Wclock1(self, time1):
        self.ui.ir_time.setText(f"{time1.hour}:{time1.minute}:{time1.second}")

    def show_time_Wclock2(self, time2):
        self.ui.gr_time.setText(f"{time2.hour}:{time2.minute}:{time2.second}")

    def show_time_Wclock3(self, time3):
        self.ui.us_time.setText(f"{time3.hour}:{time3.minute}:{time3.second}")

    def new_alarm(self):
        new_title = self.ui.tb_new_task_title.text()
        new_time = self.ui.timeEdit.text()
        new_date = ctext
        active = 0
        feedback = self.db.add_new_alarm(active, new_title, new_time, new_date)
        if feedback:
            self.read_from_database()
            self.ui.tb_new_task_title.setText("")
        else:
            msg_box = QMessageBox()
            msg_box.setText("AN ERROR HAS OCCURRED")
            msg_box.exec()

    def read_from_database(self):
        global alarms
        alarms = self.db.get_alarm_from_db()
        self.read_data(alarms)
        print(alarms)

    def read_data(self, alarms):
        global new_checkbox, recyclebin_btn, alarm_title, alarm_time, alarm_date, edit_btn
        for i in range(len(alarms)):
            new_checkbox = QCheckBox()
            new_checkbox.setFixedWidth(80)
            alarm_title = QLabel()
            alarm_title.setText(alarms[i][2])
            alarm_time = QLabel()
            alarm_time.setText(alarms[i][3])
            alarm_date = QLabel()
            alarm_date.setText(alarms[i][4])
            recyclebin_btn = QPushButton("🗑")
            recyclebin_btn.setFixedWidth(30)
            edit_btn = QPushButton("📝")
            edit_btn.setFixedWidth(30)
            self.active_alarm_list.append(alarms[i][1])
            space = QLabel()
            space.setText("")

            self.set_alarm_styles(new_checkbox, alarm_title, alarm_time, alarm_date)

            font2 = QFont()
            font2.setFamily("Dosis ExtraBold")
            font2.setPointSize(12)
            font3 = QFont()
            font3.setFamily("Dosis ExtraBold")
            font3.setPointSize(10)
            alarm_title.setFont(font2)
            alarm_time.setFont(font3)
            alarm_date.setFont(font3)

            self.labels.append(alarm_title)
            self.mylist.append(new_checkbox)
            self.del_list.append(recyclebin_btn)
            self.edit_list.append(edit_btn)
            self.alarm_time_list.append(alarm_time)
            self.alarm_date_list.append(alarm_date)

            new_checkbox.toggled.connect(self.check)
            recyclebin_btn.clicked.connect(partial(self.delete, i))
            edit_btn.clicked.connect(partial(self.edit, i))

            self.ui.gridLayout_2.addWidget(new_checkbox, i, 1)
            self.ui.gridLayout_2.addWidget(alarm_title, i, 2)
            self.ui.gridLayout_2.addWidget(alarm_time, i, 4)
            self.ui.gridLayout_2.addWidget(alarm_date, i, 5)
            self.ui.gridLayout_2.addWidget(edit_btn, i, 6)
            self.ui.gridLayout_2.addWidget(recyclebin_btn, i, 7)
            self.ui.gridLayout_2.addWidget(space, i, 3)

        self.update_alarm_status()

    def set_alarm_styles(self, checkbox, title, time, date):
        checkbox.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));"
        )
        title.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));"
        )
        time.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));"
        )
        date.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));"
        )

    def update_alarm_status(self):
        c = 0
        for item in self.active_alarm_list:
            if item == '1':
                self.mylist[c].setText("On")
                self.mylist[c].setChecked(1)
            else:
                self.mylist[c].setChecked(False)
                self.mylist[c].setText(" ")
            c += 1

    def edit(self, i):
        self.editable = True
        id = i + 1
        title = alarm_title.text()
        atime = alarm_time.text()
        date = alarm_date.text()
        self.db.edit_alarm(id, title, atime, date)
        self.read_data(alarms)

    def check(self):
        for i in range(len(alarms)):
            alarm_title = alarms[i][1]
            if self.mylist[i].isChecked():
                self.mylist[i].setText("On")
                self.mylist[i].setChecked(1)
                self.db.alarm_done(alarm_title)
            else:
                self.mylist[i].setText(" ")

    def delete(self, i):
        if self.db.remove_alarm(i + 1):
            for btn in self.del_list:
                self.del_list[i].deleteLater()
                self.edit_list[i].deleteLater()
                self.mylist[i].deleteLater()
            self.labels[i].clear()
            self.alarm_time_list[i].clear()
            self.alarm_date_list[i].clear()

    def closeEvent(self, event):
        self.ir_time_thread.terminate()
        self.us_time_thread.terminate()
        self.gr_time_thread.terminate()
        self.alarm_thread.terminate()
        self.thread_stopwatch.terminate()
        self.thread_timer.terminate()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
