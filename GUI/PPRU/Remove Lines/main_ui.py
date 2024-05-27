# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(483, 366)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"color: rgb(255, 161, 107);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(255, 255, 127);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 50px ;")

        self.gridLayout.addWidget(self.output, 6, 0, 1, 1)

        self.p_breaker = QRadioButton(self.centralwidget)
        self.p_breaker.setObjectName(u"p_breaker")
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setPointSize(13)
        self.p_breaker.setFont(font)
        self.p_breaker.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.p_breaker, 1, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.l_breaker = QRadioButton(self.centralwidget)
        self.l_breaker.setObjectName(u"l_breaker")
        self.l_breaker.setFont(font)
        self.l_breaker.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.l_breaker, 0, 0, 1, 1)

        self.input = QTextEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setStyleSheet(u"border: 10px;\n"
"background-color:rgb(255, 255, 127);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 50px ;")

        self.gridLayout.addWidget(self.input, 4, 0, 1, 1)

        self.btn_copy_to_clipboard = QPushButton(self.centralwidget)
        self.btn_copy_to_clipboard.setObjectName(u"btn_copy_to_clipboard")
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btn_copy_to_clipboard.setFont(font1)
        self.btn_copy_to_clipboard.setStyleSheet(u"border: 10px;\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 10px ;")

        self.gridLayout.addWidget(self.btn_copy_to_clipboard, 7, 0, 1, 1)

        self.btn_line_breaker = QPushButton(self.centralwidget)
        self.btn_line_breaker.setObjectName(u"btn_line_breaker")
        self.btn_line_breaker.setFont(font1)
        self.btn_line_breaker.setStyleSheet(u"border: 10px;\n"
"background-color:rgb(85, 170, 255);\n"
"color: rgb(50, 50, 50);\n"
"border-radius: 10px ;")

        self.gridLayout.addWidget(self.btn_line_breaker, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Remove Lines", None))
        self.p_breaker.setText(QCoreApplication.translate("MainWindow", u"REMOVE LINE BREAKS AND PARAGRAPH BREAKS", None))
        self.l_breaker.setText(QCoreApplication.translate("MainWindow", u"REMOVE LINE BREAKS ONLY", None))
        self.btn_copy_to_clipboard.setText(QCoreApplication.translate("MainWindow", u"COPY TO CLIPBOARD", None))
        self.btn_line_breaker.setText(QCoreApplication.translate("MainWindow", u"REMOVE LINE BREAKS", None))
    # retranslateUi

