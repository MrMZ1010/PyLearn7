#### MohammadAli Mirzae #####

import sys
from PySide6.QtWidgets import QMainWindow,QApplication
from main_ui import Ui_MainWindow
import pyperclip



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.line_breaker= self.ui.btn_line_breaker
        self.copy_to_clipboard= self.ui.btn_copy_to_clipboard
        self.line_breaker.clicked.connect(self.convert)
        self.copy_to_clipboard.clicked.connect(self.copy)


    def convert(self):
        new_text=''
        new_text=self.ui.input.toPlainText()

        if self.line_breaker.isChecked():
            new_text=new_text.replace("\n","")

        elif self.ui.p_breaker.isChecked():
            new_text=new_text.replace("\r\n","")
            new_text=new_text.replace("\n","")
        
        self.ui.output.clear()
        self.ui.output.setPlainText(new_text)

    def copy(self):
        pyperclip.copy(self.ui.output.toPlainText())


app=QApplication(sys.argv)

main_window=Mainwindow()
main_window.show()

app.exec()