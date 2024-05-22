# MohammadAli Mirzaei

import sys
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from PySide6.QtCore import QRect , Qt 
from PySide6.QtGui import QFont , QColor 
from sudoku import Sudoku
from functools import partial 
import random 
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self ):
        super().__init__()
        global font  , cell_font , selected_mode , flag
        selected_mode = 0
        flag = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self )
        self.ui.menu_new.triggered.connect(self.new_game) 
        self.line_edits =  [[None for i in range(9)] for j in range(9)]
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.ui.actionSolve_Table.triggered.connect(self.solve_puzzle)
        self.ui.actionAbout_Game.triggered.connect(self.about)
        self.ui.menuHelp.triggered.connect(self.help)
        self.ui.pushButton.clicked.connect(self.darkmode)
        self.ui.pushButton_2.clicked.connect(self.lightmode)
        self.ui.actionExit.triggered.connect(self.exit)
        font = QFont()
        font.setPointSize(16)
        cell_font =QFont()
        cell_font.setFamily(u"Dosis ExtraBold")
        cell_font.setPointSize(12)
        
        for i in range(9):
            for j in range(9): 
                new_cell =  QLineEdit()
                self.ui.grid_Layout.addWidget(new_cell , i , j  , 1 , 1)
                new_cell.textChanged.connect(partial(self.validation , i , j))
                self.line_edits[i][j] = new_cell

                sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                sizePolicy.setHeightForWidth(new_cell.sizePolicy().hasHeightForWidth())
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                self.grid_Layout = QGridLayout()
                self.grid_Layout.setSpacing(0)
                self.grid_Layout.setContentsMargins(0, 0, 0, 0)
                self.grid_Layout.setHorizontalSpacing(0)
                self.grid_Layout.setVerticalSpacing(0)
                new_cell.setGeometry(QRect(  0 ,0 ,40, 40))
                new_cell.setEnabled(True)
                new_cell.setSizePolicy(sizePolicy)
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setFont(font)
        self.new_game()

    def new_game(self) :
        global puzzle
        puzzle = Sudoku(3 , seed = random.randint(1 , 1000)).difficulty(0.5)  
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] != None :
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else :
                    self.line_edits[i][j].setText("")

    def open_file(self):
        try :
            file_path = QFileDialog.getOpenFileName(self , "Open File...")[0]
            f = open(file_path , "r")
            file_text = f.read()
            rows = file_text.split("\n")
            puzzle_board = [ [ None for i in range(9)] for j in range(9)]
            for i in range(len(rows)) :
                cells = rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setReadOnly(False)
                    if puzzle_board[i][j] != 0 :
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edits[i][j].setReadOnly(True)
                    else :
                        self.line_edits[i][j].setText("")
        except:
            print("Error!")


    def check(self):
        for i in range(0 , 9):      
            x = 0         
            num1 = self.line_edits[i][x].text()                 
            if self.line_edits[i][x].text() != None or self.line_edits[i][x].text() != "" or self.line_edits[i][x].text() != 'None' :
                for j in range(1,9) :
                    other_numbers_in_row = self.line_edits[i][j].text()
                    if other_numbers_in_row != None :
                        if num1 == other_numbers_in_row and num1 != None and num1 != "":
                            self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                            self.line_edits[i][x].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                            
                            return False
                        elif flag == 0  :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                        elif flag == 1 :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
            
            x = 1
            for x in range(1,9) : 
                num1 = self.line_edits[i][x].text()                 
                if self.line_edits[i][x].text() != None or self.line_edits[i][x].text() != "" or self.line_edits[i][x].text() != 'None' :
                    for j in range(1,9) :
                        if x != j :
                            other_numbers_in_row = self.line_edits[i][j].text()
                            if other_numbers_in_row != None :
                                if num1 == other_numbers_in_row and num1 != None and num1 != "" and x < j :
                                    self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                                    self.line_edits[i][x].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                   
                                    if x > j :
                                        self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")    
                                        self.line_edits[i][x].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                   
                                    return False
                                elif flag == 0 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")           
                                elif flag == 1 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                                                     
        for j in range(0 , 9):      
            x = 0         
            num1 = self.line_edits[x][j].text()                 
            if self.line_edits[x][j].text() != None or self.line_edits[x][j].text() != "" or self.line_edits[x][j].text() != 'None' :
                for i in range(1,9) :
                    other_numbers_in_row = self.line_edits[i][j].text()
                    if other_numbers_in_row != None :
                        if num1 == other_numbers_in_row and num1 != None and num1 != "":
                            self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                            self.line_edits[x][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                        
                            return False
                        elif flag == 0  :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")           
                        elif flag == 1 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
            
            x = 1
            for x in range(1,9) : 
                num1 = self.line_edits[x][j].text()                 
                if self.line_edits[x][j].text() != None or self.line_edits[x][j].text() != "" or self.line_edits[x][j].text() != 'None' :
                    for i in range(1,9) :
                        if x != i :
                            other_numbers_in_row = self.line_edits[i][j].text()
                            if other_numbers_in_row != None :
                                if num1 == other_numbers_in_row and num1 != None and num1 != "" and x < i :
                                    self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95));\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")
                                    self.line_edits[x][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                   
                                    if x > j :
                                        self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")    
                                        self.line_edits[x][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")                                        
                                    return False
                                elif flag == 0  :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")           
                                elif flag == 1 :
                                    self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")

        array=  []
        num1 = self.line_edits[i][j]
        x = 0 
        y = 3
        for i in range (x , y):  
            for j in range (x , y ) :     
                for i in range(3):
                    for j in range(3):
                        if num1 not in array :
                            array.append( self.line_edits[i][j].text() )
                        else :
                            self.line_edits[i][j].setStyleSheet(u"color:  rgb(95, 0, 95);\n""background-color: rgb(255, 185, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")    
                x+= 3
                y+= 3
            x+=3
            y+=3


    def validation(self , i , j , text):  
        if text not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"] :
            self.line_edits[i][j].setText("")

        if self.check() == True :
             msg_box = QMessageBox()
             msg_box.setText("You won")
             msg_box.exec()

    def solve_puzzle(self):
        solution = puzzle.solve()
        solution.show()
        print(solution)
    
    def darkmode(self):
        global flag 
        flag = 1 
        self.setPalette(QColor(26, 26, 26 ))
        for i in range(0 , 9):
            for j in range( 0 ,9 ):
                self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 91);\n""background-color: rgb(143, 193, 255);\n""border-radius: 5px;\n""font: 75 16pt \"Dosis ExtraBold\";")

    def lightmode(self):
        self.setPalette(QColor(217, 245, 255))

    def about(self):
        msg = QMessageBox(text="How to play:\nThe rules for sudoku are simple.\nA 9×9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically.\nTo challenge you more, there are 3×3 squares marked out in the grid, and each of these squares can't have any repeat numbers either" , parent= self)
        msg.exec()

    def help(self):
        msg = QMessageBox(text="Please follow the bellow link :\nhttps://sudoku.com/sudoku-rules/" , parent= self)
        msg.exec()


    def exit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWindow()
    window.show()
    app.exec()