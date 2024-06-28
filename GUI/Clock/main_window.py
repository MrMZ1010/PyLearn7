# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 463)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 250, 240);")  # FloralWhite background
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 30, 481, 411))
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setPointSize(10)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"border-bottom-color: rgb(50, 205, 50);\n"
                                     u"color: rgb(0, 0, 0);\n"
                                     u"background-color: rgb(255, 239, 213);\n"  # PapayaWhip
                                     u"border-radius: 15px ;")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.ir = QPushButton(self.tab_2)
        self.ir.setObjectName(u"ir")
        self.ir.setGeometry(QRect(50, 110, 191, 61))
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        self.ir.setFont(font1)
        self.ir.setStyleSheet(u"border: 2px solid rgb(255, 99, 71);\n"  # Tomato border
                              u"background-color: rgb(255, 182, 193);\n"  # LightPink
                              u"color: rgb(0, 0, 0);\n"
                              u"border-radius: 10px ;")
        self.gr = QPushButton(self.tab_2)
        self.gr.setObjectName(u"gr")
        self.gr.setGeometry(QRect(50, 170, 191, 61))
        self.gr.setFont(font1)
        self.gr.setStyleSheet(u"border: 2px solid rgb(255, 99, 71);\n"
                              u"background-color: rgb(255, 182, 193);\n"
                              u"color: rgb(0, 0, 0);\n"
                              u"border-radius: 10px ;")
        self.usa = QPushButton(self.tab_2)
        self.usa.setObjectName(u"usa")
        self.usa.setGeometry(QRect(50, 230, 191, 61))
        self.usa.setFont(font1)
        self.usa.setStyleSheet(u"border: 2px solid rgb(255, 99, 71);\n"
                               u"background-color: rgb(255, 182, 193);\n"
                               u"color: rgb(0, 0, 0);\n"
                               u"border-radius: 10px ;")
        self.gr_time = QPushButton(self.tab_2)
        self.gr_time.setObjectName(u"gr_time")
        self.gr_time.setGeometry(QRect(240, 170, 191, 61))
        font2 = QFont()
        font2.setFamilies([u"Dosis ExtraBold"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        self.gr_time.setFont(font2)
        self.gr_time.setStyleSheet(u"border: 2px solid rgb(50, 205, 50);\n"  # LimeGreen border
                                   u"background-color: rgb(144, 238, 144);\n"  # LightGreen
                                   u"color: rgb(0, 0, 0);\n"
                                   u"border-radius: 10px ;")
        self.us_time = QPushButton(self.tab_2)
        self.us_time.setObjectName(u"us_time")
        self.us_time.setGeometry(QRect(240, 230, 191, 61))
        self.us_time.setFont(font2)
        self.us_time.setStyleSheet(u"border: 2px solid rgb(50, 205, 50);\n"
                                   u"background-color: rgb(144, 238, 144);\n"
                                   u"color: rgb(0, 0, 0);\n"
                                   u"border-radius: 10px ;")
        self.ir_time = QPushButton(self.tab_2)
        self.ir_time.setObjectName(u"ir_time")
        self.ir_time.setGeometry(QRect(240, 110, 191, 61))
        self.ir_time.setFont(font2)
        self.ir_time.setStyleSheet(u"border: 2px solid rgb(50, 205, 50);\n"
                                   u"background-color: rgb(144, 238, 144);\n"
                                   u"color: rgb(0, 0, 0);\n"
                                   u"border-radius: 10px ;")
        self.title = QLabel(self.tab_2)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(130, 40, 221, 41))
        font3 = QFont()
        font3.setFamilies([u"Dosis ExtraBold"])
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setItalic(False)
        self.title.setFont(font3)
        self.title.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                 u"border-radius: 3px ;")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 200, 281, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Dosis ExtraBold"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.tb_new_task_title = QLineEdit(self.gridLayoutWidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        self.tb_new_task_title.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_new_task_title.sizePolicy().hasHeightForWidth())
        self.tb_new_task_title.setSizePolicy(sizePolicy1)
        self.tb_new_task_title.setStyleSheet(u"background-color: rgb(255, 255, 224);\n"  # LightYellow
                                             u"font: 11pt \"MS Shell Dlg 2\";\n"
                                             u"border-radius: 5px;")

        self.gridLayout.addWidget(self.tb_new_task_title, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                    u"background-color: rgb(255, 255, 224);")  # LightYellow

        self.gridLayout.addWidget(self.comboBox, 5, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.gridLayoutWidget)
        self.timeEdit.setObjectName(u"timeEdit")
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.timeEdit.setFont(font5)
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 224);\n"
                                    u"font: 10pt \"MS Shell Dlg 2\";")
        self.timeEdit.setMaximumDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.timeEdit, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.btn_new_alarm = QPushButton(self.tab)
        self.btn_new_alarm.setObjectName(u"btn_new_alarm")
        self.btn_new_alarm.setGeometry(QRect(370, 230, 71, 71))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_new_alarm.sizePolicy().hasHeightForWidth())
        self.btn_new_alarm.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamilies([u"Dosis ExtraBold"])
        font6.setPointSize(40)
        font6.setBold(True)
        self.btn_new_alarm.setFont(font6)
        self.btn_new_alarm.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_alarm.setStyleSheet(u"border-radius: 35px;\n"
                                         u"color: rgb(0, 0, 0);\n"
                                         u"background-color: rgb(255, 99, 71);\n"  # Tomato
                                         u"border: 2px solid rgb(220, 20, 60);\n")  # Crimson
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 20, 421, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(100, 20, 281, 161))
        font7 = QFont()
        font7.setFamilies([u"Seven Segment"])
        font7.setPointSize(70)
        font7.setBold(False)
        self.label_stopwatch.setFont(font7)
        self.label_stopwatch.setStyleSheet(u"color: rgb(255, 69, 0);")  # OrangeRed
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(100, 210, 81, 81))
        self.btn_start_stopwatch.setFont(font4)
        self.btn_start_stopwatch.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                               u"border-radius: 10px ;\n"
                                               u"background-color: rgb(255, 182, 193);\n"  # LightPink
                                               u"border: 2px solid rgb(255, 99, 71);")  # Tomato
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(200, 210, 81, 81))
        self.btn_stop_stopwatch.setFont(font4)
        self.btn_stop_stopwatch.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                              u"border-radius: 10px ;\n"
                                              u"background-color: rgb(255, 182, 193);\n"
                                              u"border: 2px solid rgb(255, 99, 71);")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_stopwatch.setFont(font4)
        self.btn_reset_stopwatch.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                               u"border-radius: 10px ;\n"
                                               u"background-color: rgb(255, 182, 193);\n"
                                               u"border: 2px solid rgb(255, 99, 71);")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textbox_hour_timer = QLineEdit(self.tab_4)
        self.textbox_hour_timer.setObjectName(u"textbox_hour_timer")
        self.textbox_hour_timer.setGeometry(QRect(80, 60, 101, 91))
        font8 = QFont()
        font8.setFamilies([u"Seven Segment"])
        font8.setPointSize(50)
        self.textbox_hour_timer.setFont(font8)
        self.textbox_hour_timer.setStyleSheet(u"color: rgb(255, 69, 0);")  # OrangeRed
        self.textbox_hour_timer.setAlignment(Qt.AlignCenter)
        self.textbox_minute_timer = QLineEdit(self.tab_4)
        self.textbox_minute_timer.setObjectName(u"textbox_minute_timer")
        self.textbox_minute_timer.setGeometry(QRect(190, 60, 101, 91))
        self.textbox_minute_timer.setFont(font8)
        self.textbox_minute_timer.setStyleSheet(u"color: rgb(255, 69, 0);")
        self.textbox_minute_timer.setAlignment(Qt.AlignCenter)
        self.textbox_second_timer = QLineEdit(self.tab_4)
        self.textbox_second_timer.setObjectName(u"textbox_second_timer")
        self.textbox_second_timer.setGeometry(QRect(300, 60, 101, 91))
        self.textbox_second_timer.setFont(font8)
        self.textbox_second_timer.setStyleSheet(u"color: rgb(255, 69, 0);")
        self.textbox_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(100, 210, 81, 81))
        self.btn_start_timer.setFont(font4)
        self.btn_start_timer.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                           u"border-radius: 10px ;\n"
                                           u"background-color: rgb(144, 238, 144);\n"  # LightGreen
                                           u"border: 2px solid rgb(50, 205, 50);")  # LimeGreen
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(200, 210, 81, 81))
        self.btn_stop_timer.setFont(font4)
        self.btn_stop_timer.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                          u"border-radius: 10px ;\n"
                                          u"background-color: rgb(144, 238, 144);\n"
                                          u"border: 2px solid rgb(50, 205, 50);")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(300, 210, 81, 81))
        self.btn_reset_timer.setFont(font4)
        self.btn_reset_timer.setStyleSheet(u"color: rgb(0, 0, 0);\n"
                                           u"border-radius: 10px ;\n"
                                           u"background-color: rgb(144, 238, 144);\n"
                                           u"border: 2px solid rgb(50, 205, 50);")
        self.pushButton = QPushButton(self.tab_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 30, 101, 28))
        font9 = QFont()
        font9.setFamilies([u"Dosis ExtraBold"])
        font9.setPointSize(13)
        font9.setBold(True)
        self.pushButton.setFont(font9)
        self.pushButton.setStyleSheet(u"border-radius: 3px;\n"
                                      u"color: rgb(0, 0, 0);")
        self.pushButton_2 = QPushButton(self.tab_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 30, 101, 28))
        self.pushButton_2.setFont(font9)
        self.pushButton_2.setStyleSheet(u"border-radius: 3px;\n"
                                        u"color: rgb(0, 0, 0);")
        self.pushButton_3 = QPushButton(self.tab_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 30, 101, 28))
        self.pushButton_3.setFont(font9)
        self.pushButton_3.setStyleSheet(u"border-radius: 3px;\n"
                                        u"color: rgb(0, 0, 0);")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ir.setText(QCoreApplication.translate("MainWindow", u"IRAN", None))
        self.gr.setText(QCoreApplication.translate("MainWindow", u"GERMANY", None))
        self.usa.setText(QCoreApplication.translate("MainWindow", u"USA", None))
        self.gr_time.setText("")
        self.us_time.setText("")
        self.ir_time.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alarm Title :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
#if QT_CONFIG(tooltip)
        self.btn_new_alarm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>press to add new task</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_new_alarm.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.gridLayoutWidget_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"border-bottom-color: rgb(50, 205, 50);\n"
                                              u"color: rgb(0, 0, 0);\n"
                                              u"background-color: rgb(255, 239, 213);\n"
                                              u"border-radius: 15px ;", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.textbox_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_minute_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Hour", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Minute", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Second", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi
