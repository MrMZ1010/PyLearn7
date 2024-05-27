#### MohammadAli Mirzae #####

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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(332, 225)
        mainWindow.setMinimumSize(QSize(332, 225))
        mainWindow.setMaximumSize(QSize(332, 225))
        mainWindow.setStyleSheet(u"background-color : rgb(255, 170, 255)")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 311, 51))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 21))
        font = QFont()
        font.setFamilies([u"Yekan Bakh FaNum"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.combo_units = QComboBox(self.groupBox)
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.setObjectName(u"combo_units")
        self.combo_units.setGeometry(QRect(100, 10, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Yekan Bakh FaNum"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.combo_units.setFont(font1)
        self.combo_units.setLayoutDirection(Qt.RightToLeft)
        self.combo_units.setStyleSheet(u"background-color : rgb(255, 255, 127)")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 70, 311, 151))
        self.combo_from = QComboBox(self.groupBox_2)
        self.combo_from.setObjectName(u"combo_from")
        self.combo_from.setGeometry(QRect(0, 10, 151, 31))
        self.combo_from.setFont(font1)
        self.combo_from.setLayoutDirection(Qt.RightToLeft)
        self.combo_from.setStyleSheet(u"background-color : rgb(255, 255, 127)")
        self.combo_to = QComboBox(self.groupBox_2)
        self.combo_to.setObjectName(u"combo_to")
        self.combo_to.setGeometry(QRect(0, 70, 151, 31))
        self.combo_to.setFont(font1)
        self.combo_to.setLayoutDirection(Qt.RightToLeft)
        self.combo_to.setStyleSheet(u"background-color : rgb(255, 255, 127)")
        self.cal = QPushButton(self.groupBox_2)
        self.cal.setObjectName(u"cal")
        self.cal.setGeometry(QRect(4, 110, 301, 41))
        self.cal.setFont(font1)
        self.cal.setStyleSheet(u"background-color : rgb(85, 255, 127)")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 40, 21, 21))
        self.label_2.setFont(font)
        self.text_from = QLineEdit(self.groupBox_2)
        self.text_from.setObjectName(u"text_from")
        self.text_from.setGeometry(QRect(170, 10, 131, 31))
        self.text_from.setFont(font)
        self.text_from.setStyleSheet(u"background-color : rgb(255, 170, 127)")
        self.text_to = QLineEdit(self.groupBox_2)
        self.text_to.setObjectName(u"text_to")
        self.text_to.setEnabled(False)
        self.text_to.setGeometry(QRect(170, 70, 131, 31))
        self.text_to.setFont(font)
        self.text_to.setStyleSheet(u"background-color : rgb(255, 170, 127)")
        self.text_to.setReadOnly(True)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Unit Converter", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"CHOOSE: ", None))
        self.combo_units.setItemText(0, QCoreApplication.translate("mainWindow", u"weight", None))
        self.combo_units.setItemText(1, QCoreApplication.translate("mainWindow", u"length", None))
        self.combo_units.setItemText(2, QCoreApplication.translate("mainWindow", u"temperature", None))
        self.combo_units.setItemText(3, QCoreApplication.translate("mainWindow", u"digital volume", None))

        self.groupBox_2.setTitle("")
        self.cal.setText(QCoreApplication.translate("mainWindow", u"COMPUTE", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"=", None))
    # retranslateUi

