import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from game_ui import Ui_MainWindow


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.game_count = 0
        self.winner = ""
        self.chanse = ['✋','🤚']
        self.ui.inside.clicked.connect(partial(self.start_game, "inside"))
        self.ui.outside.clicked.connect(partial(self.start_game, "outside"))


    def start_game(self, hand):
        if hand == 'outside':
            self.ui.user_select.setText('🤚')
            self.cpu_select()
        elif hand == 'inside':
            self.ui.user_select.setText('✋')
            self.cpu_select()


    def cpu_select(self):
        cpu_choise = random.choice(self.chanse)
        self.ui.cpu_1_select.setText(cpu_choise)
        cpu_choise = random.choice(self.chanse)
        self.ui.cpu_2_select.setText(cpu_choise)
        self.select_winner()


    def select_winner(self):
        if self.ui.user_select.text() == self.ui.cpu_1_select.text() == self.ui.user_select== self.ui.cpu_2_select.text():
            self.savePoints(1,1,1)
            self.ui.groupBox_2.setStyle('background-color: rgb(85, 255, 127);')
            self.ui.groupBox_3.setStyle('background-color: rgb(85, 255, 127);')
            self.ui.groupBox_4.setStyle('background-color: rgb(85, 255, 127);')
        elif self.ui.user_select.text() == self.ui.cpu_1_select.text() != self.ui.cpu_2_select.text():
            self.savePoints(1,1,0)
            self.ui.groupBox_4.setStyle('background-color: rgb(85, 255, 127);')
            self.ui.groupBox_3.setStyle('background-color: rgb(85, 255, 127);')
        elif self.ui.user_select.text() != self.ui.cpu_1_select.text() == self.ui.cpu_2_select.text():
            self.savePoints(0,1,1)
            self.ui.groupBox_3.setStyle('background-color: rgb(85, 255, 127);')
            self.ui.groupBox_2.setStyle('background-color: rgb(85, 255, 127);')


    def savePoints(self,user,cpu1,cpu2):
        user_point = self.ui.user_point.text()
        cpu_1 = self.ui.cpu_1_point.text()
        cpu_2 = self.ui.cpu_2_point.text()
        user_point += user
        cpu_1 += cpu1
        cpu_2 += cpu2
        self.ui.user_point.setText(user_point)
        self.ui.cpu_1_point.setText(cpu_1)
        self.ui.cpu_2_point.setText(cpu_2)

        msgbox = QMessageBox()
        if user_point == 5:
            msgbox.text("User won")
        elif cpu_1 == 5:
            msgbox.text("CPU1 won")
        elif cpu_2 == 5:
            msgbox.text("CPU2 won")
        msgbox.exec()
        self.ui.user_point = 0
        self.ui.cpu_1_point = 0
        self.ui.cpu_2_point = 0
   
if __name__ == "__main__":
         
    app = QApplication(sys.argv)
    window = Game()

    window.show()
    app.exec()
