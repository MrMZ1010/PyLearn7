##### MohammadAli Mirzaei #####

from random import randint
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize the main window and set up the user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Initialize list to store numbers and count for the empty cell
        self.list = []
        self.count = 0
        # 2D list to store buttons
        self.buttons = [
            [self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4],
            [self.ui.btn5, self.ui.btn6, self.ui.btn7, self.ui.btn8],
            [self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12],
            [self.ui.btn13, self.ui.btn14, self.ui.btn15, self.ui.btn16]
        ]
        # Fill the list with numbers 1 to 16
        for i in range(16):
            self.list.append(i + 1)
        # Place numbers randomly on buttons and connect button clicks
        for i in range(4):
            for j in range(4):
                r = randint(0, 15 - self.count)
                self.buttons[i][j].setText(str(self.list[r]))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                # If the number is 16, store its coordinates and hide the button
                if self.list[r] == 16:
                    self.empty_i = i
                    self.empty_j = j
                    self.buttons[i][j].setVisible(False)
                self.list.pop(r)
                self.count += 1

    def play(self, i, j):
        # Function to handle button clicks
        # If the clicked button is adjacent to the empty cell, swap their positions
        if (abs(j - self.empty_j) == 1 and i == self.empty_i) or ((abs(i - self.empty_i) == 1) and j == self.empty_j):
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.empty_i = i
            self.empty_j = j
        # Check if the player has won
        if self.check_win():
            msg_box = QMessageBox()
            msg_box.setText("You Win!")
            msg_box.exec()

    def check_win(self):
        # Function to check if the player has won
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True

# Create the application instance
app = QApplication(sys.argv)
# Create an instance of the MainWindow class
main_window = MainWindow()
# Show the main window
main_window.show()
# Start the application event loop
app.exec()
