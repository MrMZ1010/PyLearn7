# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 538)
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_new.setFont(font)
        self.menu_new.setPriority(QAction.NormalPriority)
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSolve_Table = QAction(MainWindow)
        self.actionSolve_Table.setObjectName(u"actionSolve_Table")
        self.actionAbout_Game = QAction(MainWindow)
        self.actionAbout_Game.setObjectName(u"actionAbout_Game")
        self.actionAbout_Game.setFont(font)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionHelp.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 30, 411, 371))
        self.grid_Layout = QGridLayout(self.gridLayoutWidget)
        self.grid_Layout.setObjectName(u"grid_Layout")
        self.grid_Layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(60, 430, 411, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 531, 22))
        font2 = QFont()
        font2.setFamilies([u"Dosis ExtraBold"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.menubar.setFont(font2)
        self.menubar.setStyleSheet(u"background-color:  rgb(250, 253, 137);\n"
"color: rgb(0, 0, 0);")
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuGame.setFont(font)
        self.menuGame.setStyleSheet(u"background-color:  rgb(250, 253, 137);")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setFont(font)
        self.menuAbout.setStyleSheet(u"background-color:   rgb(250, 253, 137);\n"
"color: rgb(0, 0, 0);")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addAction(self.menu_openfile)
        self.menuGame.addAction(self.actionSolve_Table)
        self.menuGame.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Game)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSolve_Table.setText(QCoreApplication.translate("MainWindow", u"Solve Table ", None))
        self.actionAbout_Game.setText(QCoreApplication.translate("MainWindow", u"About Game...", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help !", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

