##### MohammadAli Mirzaei #####

import sys
from functools import partial
import random
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

# Function to check for winning conditions or a tie
def Check():
    global Player, win_game, msg_box
    checklist = ["X", "O"]
    for j in range(len(checklist)):
        for i in range(3):
            # Check rows, columns, and diagonals for a winning pattern
            if buttons[i][0].text() == checklist[j] and buttons[i][1].text() == checklist[j] and buttons[i][2].text() == checklist[j] or \
                buttons[0][i].text() == checklist[j] and buttons[1][i].text() == checklist[j] and buttons[2][i].text() == checklist[j] or \
                buttons[0][0].text() == checklist[j] and buttons[1][1].text() == checklist[j] and buttons[2][2].text() == checklist[j] or \
                buttons[0][2].text() == checklist[j] and buttons[1][1].text() == checklist[j] and buttons[2][0].text() == checklist[j]:
                # Display winner message box and update scores
                msg_box = QMessageBox(text=f"PLAYER{j+1} is the winner!")
                win_game = 1
                msg_box.show()
                if j + 1 == 1:
                    text = main_window.xscore.text()
                    text1 = text.split(":")
                    main_window.xscore.setText(f"X SCORE: {int(text1[1]) + 1}")
                    Player = 1
                    break
                elif j + 1 == 2:
                    text = main_window.oscore.text()
                    text1 = text.split(":")
                    main_window.oscore.setText(f"O SCORE: {int(text1[1]) + 1}")
                    Player = 2
                    break
    # Check for a tie
    if len(button_clicked) == 9 and win_game != 1:
        msg_box = QMessageBox(text="TIES!")
        text = main_window.oscore.text()
        text1 = text.split(":")
        main_window.tie.setText(f"TIES: {int(text1[1]) + 1}")
        win_game = 2
        msg_box.show()
    if Player == 2:
        cpu()

# Function to handle player's move
def play(row, col):
    global Player, win_game
    global buttons
    if win_game == 0:
        for i in button_clicked:
            if i == buttons[row][col]:
                break
        else:
            if Player == 1:
                buttons[row][col].setText("X")
                buttons[row][col].setStyleSheet("color: rgb(255, 0, 0);")
                main_window.turn.setText("O`s Turn")
                Player = 2
            elif Player == 2:
                buttons[row][col].setText("O")
                buttons[row][col].setStyleSheet("color: rgb(0, 0, 255);")
                main_window.turn.setText("X`s Turn")
                Player = 1
            button_clicked.append(buttons[row][col])

        Check()

# Function to display about box
def about():
    about_box = QMessageBox(text="This game has been created by MohammadAli Mirzaei")
    about_box.setWindowTitle("Tic Tac Toe")
    about_box.exec()

# Function to handle CPU's move
def cpu():
    global win_game, Player
    if main_window.cpu.isChecked() and win_game == 0:
        if len(button_clicked) == 0:
            btn_cpu = buttons[random.randint(0, 2)][random.randint(0, 2)]
            btn_cpu.setText("O")
            btn_cpu.setStyleSheet("color: rgb(0, 0, 255);")
        else:
            while True:
                btn_cpu = buttons[random.randint(0, 2)][random.randint(0, 2)]
                for k in button_clicked:
                    if btn_cpu == k:
                        break
                else:
                    btn_cpu.setText("O")
                    btn_cpu.setStyleSheet("color: rgb(0, 0, 255);")
                    break
        main_window.turn.setText("X`s Turn")
        Player = 1
        button_clicked.append(btn_cpu)
        Check()

# Function to start a new game
def new_game():
    global win_game, Player
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("background-color: rgb(51, 214, 206); border-radius: 10px; border-style: outset; border-width: 3px; border-color: rgb(255, 255, 255);")
    button_clicked.clear()
    win_game = 0
    if Player == 1:
        main_window.turn.setText("X`s Turn")
    elif Player == 2:
        main_window.turn.setText("O`s Turn")
    if Player == 2 and main_window.cpu.isChecked():
        Check()

# Load UI and start application
loader = QUiLoader()
app = QApplication(sys.argv)
Player = 1
win_game = 0

main_window = loader.load("ui.ui")
main_window.show()
main_window.setWindowTitle("Tic Tac Toe")

button_clicked = []
buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3], 
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

# Connect buttons to play function
for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))
   
main_window.about.clicked.connect(about)
main_window.newgame.clicked.connect(new_game)       
app.exec()
