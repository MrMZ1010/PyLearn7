#### MohammadAli Mirzae #####

import sys  # Importing the sys module to access system-specific parameters and functions.

# Importing necessary classes from PySide6.QtWidgets module for GUI development.
from PySide6.QtWidgets import QMainWindow, QApplication

# Importing the UI layout created in Qt Designer and converted to Python code using PySide6's uic module.
from main_ui import Ui_MainWindow  # Assuming main_ui.py contains the UI layout.

# Importing the pyperclip module for clipboard operations.
import pyperclip  

# Creating a custom QMainWindow class to handle the application's main window.
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Creating an instance of the UI layout class.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Setting up the UI layout for the main window.

        # Accessing UI elements defined in the layout and storing them as attributes.
        self.line_breaker = self.ui.btn_line_breaker  # Assuming btn_line_breaker is a QPushButton.
        self.copy_to_clipboard = self.ui.btn_copy_to_clipboard  # Assuming btn_copy_to_clipboard is a QPushButton.

        # Connecting signals from UI elements to slots (functions) in the Mainwindow class.
        self.line_breaker.clicked.connect(self.convert)  # Connects the clicked signal of line_breaker button to convert method.
        self.copy_to_clipboard.clicked.connect(self.copy)  # Connects the clicked signal of copy_to_clipboard button to copy method.

    # Method to handle text conversion based on user selection.
    def convert(self):
        new_text = self.ui.input.toPlainText()  # Retrieving text from the input text edit widget.

        # Checking the state of line_breaker button and applying corresponding text processing.
        if self.line_breaker.isChecked():
            new_text = new_text.replace("\n", "")  # Removes line breaks (\n) from the text.

        # Checking the state of p_breaker button and applying corresponding text processing.
        elif self.ui.p_breaker.isChecked():
            new_text = new_text.replace("\r\n", "")  # Removes Windows-style line breaks (\r\n) from the text.
            new_text = new_text.replace("\n", "")    # Removes Unix-style line breaks (\n) from the text.

        # Clearing the output text edit widget and setting the processed text.
        self.ui.output.clear()
        self.ui.output.setPlainText(new_text)

    # Method to copy text from output text edit widget to the clipboard.
    def copy(self):
        pyperclip.copy(self.ui.output.toPlainText())  # Copies the text from output text edit widget to the clipboard.

# Creating a QApplication instance to manage the GUI application.
app = QApplication(sys.argv)

# Creating an instance of the Mainwindow class.
main_window = Mainwindow()

# Displaying the main window.
main_window.show()

# Entering the application's event loop.
app.exec()
