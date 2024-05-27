#### MohammadAli Mirzaei ####
import sys  # Importing the sys module for system-specific parameters and functions
from PySide6.QtWidgets import *  # Importing the necessary widgets from PySide6
from main_window import Ui_MainWindow  # Importing the UI class from main_window.py
from PySide6.QtCore import QRect, Qt  # Importing required Qt modules for core functionalities
from PySide6.QtGui import QFont, QColor  # Importing required Qt modules for GUI functionalities
from sudoku import Sudoku  # Importing the Sudoku class for game logic
from functools import partial  # Importing functools for creating partial functions
import random  # Importing the random module for generating random numbers

# Redundant import, the 'main_window' UI class is already imported above
from main_window import Ui_MainWindow  

# Defining the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Calling the constructor of the parent class
        global font, cell_font, selected_mode, flag  # Defining global variables for font and mode
        selected_mode = 0  # Initializing the selected mode
        flag = 0  # Initializing the flag variable
        self.ui = Ui_MainWindow()  # Creating an instance of the UI class
        self.ui.setupUi(self)  # Setting up the UI components
        
        # Connecting menu actions to their respective methods
        self.ui.menu_new.triggered.connect(self.new_game)  
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.ui.actionSolve_Table.triggered.connect(self.solve_puzzle)
        self.ui.actionAbout_Game.triggered.connect(self.about)
        self.ui.menuHelp.triggered.connect(self.help)
        self.ui.pushButton.clicked.connect(self.darkmode)
        self.ui.pushButton_2.clicked.connect(self.lightmode)
        self.ui.actionExit.triggered.connect(self.exit)
        
        # Setting up fonts for the UI components
        font = QFont()
        font.setPointSize(16)
        cell_font = QFont()
        cell_font.setFamily(u"Dosis ExtraBold")
        cell_font.setPointSize(12)
        
        # Creating line edit widgets for each cell in the Sudoku grid
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.ui.grid_Layout.addWidget(new_cell, i, j, 1, 1)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
                
                # Configuring size policy and styling for each cell
                sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                sizePolicy.setHeightForWidth(new_cell.sizePolicy().hasHeightForWidth())
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                new_cell.setGeometry(QRect(0, 0, 40, 40))
                new_cell.setEnabled(True)
                new_cell.setSizePolicy(sizePolicy)
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setFont(font)
        
        self.new_game()  # Starting a new game upon initialization

    # Method to start a new Sudoku game
    def new_game(self):
        global puzzle  # Declaring the puzzle variable as global
        # Generating a new Sudoku puzzle with a specified difficulty level
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        # Displaying the initial state of the puzzle on the UI
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] != None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    # Method to open a Sudoku puzzle from a file
    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open File...")[0]  # Getting the file path
            f = open(file_path, "r")  # Opening the file in read mode
            file_text = f.read()  # Reading the content of the file
            rows = file_text.split("\n")  # Splitting the file content by new line
            puzzle_board = [[None for i in range(9)] for j in range(9)]  # Creating a 2D array for puzzle board
            for i in range(len(rows)):
                cells = rows[i].split(" ")  # Splitting each row by space
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])  # Converting cell values to integers
            # Updating the UI with the puzzle from the file
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setReadOnly(False)  # Making all cells editable
                    if puzzle_board[i][j] != 0:
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))  # Setting non-empty cells
                        self.line_edits[i][j].setReadOnly(True)  # Making non-empty cells read-only
                    else:
                        self.line_edits[i][j].setText("")  # Clearing empty cells
        except:
            print("Error!")  # Handling errors if any occur during file opening/reading

    # Method to validate the Sudoku grid
    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")  # Clearing invalid input
        if self.check() == True:
            msg_box = QMessageBox()  # Creating a message box for displaying the result
            msg_box.setText("You won")  # Setting the message box text
            msg_box.exec()  # Displaying the message box

    # Method to check the validity of the Sudoku grid
    def check(self):
        # Implementing Sudoku rules checking logic
        # Checking for duplicate numbers in rows and highlighting them if found
        # Returning False if duplicate is found, True otherwise
        pass  # Placeholder for the actual implementation

    # Method to solve the Sudoku puzzle
    def solve_puzzle(self):
        # Solving the Sudoku puzzle using the Sudoku class solve() method
        # Displaying the solution in a separate window
        pass  # Placeholder for the actual implementation

    # Method to switch to dark mode
    def darkmode(self):
        global flag  # Declaring the flag variable as global
        flag = 1  # Setting the flag to indicate dark mode
        # Setting the palette and styling for dark mode
        self.setPalette(QColor(26, 26, 26))
        for i in range(0, 9):
            for j in range(0, 9):
                                # Configuring the stylesheet for dark mode
                self.line_edits[i][j].setStyleSheet(
                    u"color: rgb(0, 0, 91);\n"
                    "background-color: rgb(143, 193, 255);\n"
                    "border-radius: 5px;\n"
                    "font: 75 16pt \"Dosis ExtraBold\";"
                )

    # Method to switch to light mode
    def lightmode(self):
        # Setting the palette and styling for light mode
        self.setPalette(QColor(217, 245, 255))
        for i in range(0, 9):
            for j in range(0, 9):
                self.line_edits[i][j].setStyleSheet(
                    u"color: rgb(0, 0, 91);\n"
                    "background-color: rgb(255, 255, 255);\n"
                    "border-radius: 5px;\n"
                    "font: 75 16pt \"Dosis ExtraBold\";"
                )

    # Method to display information about the game
    def about(self):
        # Creating a message box with information about the game rules
        msg = QMessageBox(text="How to play:\n"
                                "The rules for sudoku are simple.\n"
                                "A 9×9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically.\n"
                                "To challenge you more, there are 3×3 squares marked out in the grid, and each of these squares can't have any repeat numbers either",
                          parent=self)
        msg.exec()  # Displaying the message box

    # Method to display help information
    def help(self):
        # Creating a message box with a link to sudoku rules
        msg = QMessageBox(text="Please follow the below link:\n"
                               "https://sudoku.com/sudoku-rules/", parent=self)
        msg.exec()  # Displaying the message box

    # Method to exit the application
    def exit(self):
        self.close()  # Closing the application window

# Main method to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Creating the QApplication instance
    window = MainWindow()  # Creating the main window instance
    window.show()  # Displaying the main window
    sys.exit(app.exec())  # Executing the application event loop

