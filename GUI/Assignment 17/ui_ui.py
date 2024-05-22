##### MohammadAli Mirzaei #####


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import btn_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(256, 455)
        Form.setMinimumSize(QSize(256, 0))
        Form.setMaximumSize(QSize(256, 16777215))
        Form.setBaseSize(QSize(0, -1))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setAcceptDrops(False)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color:#cacaca")
        self.sqrt = QPushButton(Form)
        self.sqrt.setObjectName(u"sqrt")
        self.sqrt.setGeometry(QRect(210, 160, 41, 41))
        self.sqrt.setCursor(QCursor(Qt.PointingHandCursor))
        self.sqrt.setStyleSheet(u"background-color: #f2a33c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.div = QPushButton(Form)
        self.div.setObjectName(u"div")
        self.div.setGeometry(QRect(210, 210, 41, 41))
        self.div.setCursor(QCursor(Qt.PointingHandCursor))
        self.div.setStyleSheet(u"background-color: #f2a33c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:20px;")
        self.mul = QPushButton(Form)
        self.mul.setObjectName(u"mul")
        self.mul.setGeometry(QRect(210, 260, 41, 41))
        self.mul.setCursor(QCursor(Qt.PointingHandCursor))
        self.mul.setStyleSheet(u"background-color: #f2a33c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:20px;")
        self.neg = QPushButton(Form)
        self.neg.setObjectName(u"neg")
        self.neg.setGeometry(QRect(210, 310, 41, 41))
        self.neg.setCursor(QCursor(Qt.PointingHandCursor))
        self.neg.setStyleSheet(u"background-color: #f2a33c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:20px;")
        self.plus = QPushButton(Form)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(210, 360, 41, 41))
        self.plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.plus.setStyleSheet(u"background-color: #f2a33c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:20px;")
        self.equal = QPushButton(Form)
        self.equal.setObjectName(u"equal")
        self.equal.setGeometry(QRect(10, 410, 241, 41))
        self.equal.setCursor(QCursor(Qt.PointingHandCursor))
        self.equal.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:20px;")
        self.MP = QPushButton(Form)
        self.MP.setObjectName(u"MP")
        self.MP.setGeometry(QRect(110, 160, 41, 41))
        self.MP.setCursor(QCursor(Qt.PointingHandCursor))
        self.MP.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.MM = QPushButton(Form)
        self.MM.setObjectName(u"MM")
        self.MM.setGeometry(QRect(60, 160, 41, 41))
        self.MM.setCursor(QCursor(Qt.PointingHandCursor))
        self.MM.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.MR = QPushButton(Form)
        self.MR.setObjectName(u"MR")
        self.MR.setGeometry(QRect(10, 160, 41, 41))
        self.MR.setCursor(QCursor(Qt.PointingHandCursor))
        self.MR.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.sin = QPushButton(Form)
        self.sin.setObjectName(u"sin")
        self.sin.setGeometry(QRect(160, 160, 41, 41))
        self.sin.setCursor(QCursor(Qt.PointingHandCursor))
        self.sin.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.cos = QPushButton(Form)
        self.cos.setObjectName(u"cos")
        self.cos.setGeometry(QRect(160, 210, 41, 41))
        self.cos.setCursor(QCursor(Qt.PointingHandCursor))
        self.cos.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.tan = QPushButton(Form)
        self.tan.setObjectName(u"tan")
        self.tan.setGeometry(QRect(160, 260, 41, 41))
        self.tan.setCursor(QCursor(Qt.PointingHandCursor))
        self.tan.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.cot = QPushButton(Form)
        self.cot.setObjectName(u"cot")
        self.cot.setGeometry(QRect(160, 310, 41, 41))
        self.cot.setCursor(QCursor(Qt.PointingHandCursor))
        self.cot.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.log = QPushButton(Form)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(160, 360, 41, 41))
        self.log.setCursor(QCursor(Qt.PointingHandCursor))
        self.log.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b7 = QPushButton(Form)
        self.b7.setObjectName(u"b7")
        self.b7.setGeometry(QRect(10, 210, 41, 41))
        self.b7.setCursor(QCursor(Qt.PointingHandCursor))
        self.b7.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b8 = QPushButton(Form)
        self.b8.setObjectName(u"b8")
        self.b8.setGeometry(QRect(60, 210, 41, 41))
        self.b8.setCursor(QCursor(Qt.PointingHandCursor))
        self.b8.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b9 = QPushButton(Form)
        self.b9.setObjectName(u"b9")
        self.b9.setGeometry(QRect(110, 210, 41, 41))
        self.b9.setCursor(QCursor(Qt.PointingHandCursor))
        self.b9.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b5 = QPushButton(Form)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(60, 260, 41, 41))
        self.b5.setCursor(QCursor(Qt.PointingHandCursor))
        self.b5.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b4 = QPushButton(Form)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(10, 260, 41, 41))
        self.b4.setCursor(QCursor(Qt.PointingHandCursor))
        self.b4.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b6 = QPushButton(Form)
        self.b6.setObjectName(u"b6")
        self.b6.setGeometry(QRect(110, 260, 41, 41))
        self.b6.setCursor(QCursor(Qt.PointingHandCursor))
        self.b6.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b2 = QPushButton(Form)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(60, 310, 41, 41))
        self.b2.setCursor(QCursor(Qt.PointingHandCursor))
        self.b2.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b1 = QPushButton(Form)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(10, 310, 41, 41))
        self.b1.setCursor(QCursor(Qt.PointingHandCursor))
        self.b1.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.b3 = QPushButton(Form)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(110, 310, 41, 41))
        self.b3.setCursor(QCursor(Qt.PointingHandCursor))
        self.b3.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.z = QPushButton(Form)
        self.z.setObjectName(u"z")
        self.z.setGeometry(QRect(60, 360, 41, 41))
        self.z.setCursor(QCursor(Qt.PointingHandCursor))
        self.z.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.zz = QPushButton(Form)
        self.zz.setObjectName(u"zz")
        self.zz.setGeometry(QRect(10, 360, 41, 41))
        self.zz.setCursor(QCursor(Qt.PointingHandCursor))
        self.zz.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.point = QPushButton(Form)
        self.point.setObjectName(u"point")
        self.point.setGeometry(QRect(110, 360, 41, 41))
        self.point.setCursor(QCursor(Qt.PointingHandCursor))
        self.point.setStyleSheet(u"background-color: #717172;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.c = QPushButton(Form)
        self.c.setObjectName(u"c")
        self.c.setGeometry(QRect(10, 110, 91, 41))
        self.c.setCursor(QCursor(Qt.PointingHandCursor))
        self.c.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.round = QPushButton(Form)
        self.round.setObjectName(u"round")
        self.round.setGeometry(QRect(110, 110, 91, 41))
        self.round.setCursor(QCursor(Qt.PointingHandCursor))
        self.round.setStyleSheet(u"background-color: #555556;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 221, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(170, 0, 127);")
        self.temp = QLineEdit(Form)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(10, 50, 241, 41))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.temp.setFont(font1)
        self.temp.setLayoutDirection(Qt.RightToLeft)
        self.temp.setMaxLength(32767)
        self.temp.setFrame(True)
        self.temp.setEchoMode(QLineEdit.Normal)
        self.temp.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculator", None))
        self.sqrt.setText(QCoreApplication.translate("Form", u"\u221a", None))
        self.div.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.mul.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.neg.setText(QCoreApplication.translate("Form", u"-", None))
        self.plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.MP.setText(QCoreApplication.translate("Form", u"M+", None))
        self.MM.setText(QCoreApplication.translate("Form", u"M-", None))
        self.MR.setText(QCoreApplication.translate("Form", u"MR", None))
        self.sin.setText(QCoreApplication.translate("Form", u"sin", None))
        self.cos.setText(QCoreApplication.translate("Form", u"cos", None))
        self.tan.setText(QCoreApplication.translate("Form", u"tan", None))
        self.cot.setText(QCoreApplication.translate("Form", u"cot", None))
        self.log.setText(QCoreApplication.translate("Form", u"log", None))
        self.b7.setText(QCoreApplication.translate("Form", u"7", None))
        self.b8.setText(QCoreApplication.translate("Form", u"8", None))
        self.b9.setText(QCoreApplication.translate("Form", u"9", None))
        self.b5.setText(QCoreApplication.translate("Form", u"5", None))
        self.b4.setText(QCoreApplication.translate("Form", u"4", None))
        self.b6.setText(QCoreApplication.translate("Form", u"6", None))
        self.b2.setText(QCoreApplication.translate("Form", u"2", None))
        self.b1.setText(QCoreApplication.translate("Form", u"1", None))
        self.b3.setText(QCoreApplication.translate("Form", u"3", None))
        self.z.setText(QCoreApplication.translate("Form", u"0", None))
        self.zz.setText(QCoreApplication.translate("Form", u"00", None))
        self.point.setText(QCoreApplication.translate("Form", u".", None))
        self.c.setText(QCoreApplication.translate("Form", u"C", None))
        self.round.setText(QCoreApplication.translate("Form", u"ROUND", None))
        self.label.setText("")
        self.temp.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

