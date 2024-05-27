##### MohammadAli Mirzaei #####

import sys
import random
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from main_ui import Ui_MainWindow

# Import necessary libraries and modules
# PySide6.QtWidgets is used for creating the graphical user interface (GUI)
# main_ui contains the user interface design created with Qt Designer

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize the PasswordGenerator class, inheriting from QMainWindow
        # Set up the UI defined in main_ui.py using PySide6
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Define character sets for generating passwords
        self.araye = ["number", "special", "upper", "lower"]
        self.number = "1234567890"
        self.special = "!@#$%^&*(){<>?}[=-]|"
        self.upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.lower = self.upper.lower()

        # Connect the button click event to the method that generates passwords
        self.ui.btn_generate.clicked.connect(self.generate_pass)

    def generate_pass(self):
        # Method to generate passwords
        self.password = ""
        # Check which radio button is selected for password strength
        r_standard = self.ui.radio_standard.isChecked()
        r_strong = self.ui.radio_strong.isChecked()
        r_super = self.ui.radio_super.isChecked()

        # Determine password length and counts of different character types based on selected strength
        if r_standard == True:
            self.strlen = 8
            self.number_count = 1
            self.special_count = 1
            self.upper_count = 1
        elif r_strong == True:
            self.strlen = 12
            self.number_count = 2
            self.special_count = 2
            self.upper_count = 2
        elif r_super == True:
            self.strlen = 20
            self.number_count = 3
            self.special_count = 3
            self.upper_count = 3

        # Calculate the count of lowercase letters based on the difference
        self.lower_count = self.strlen - (
            self.number_count + self.special_count + self.upper_count
        )

        # Generate random characters from each character set based on their respective counts
        num = random.choices(self.number, k=self.number_count)
        spe = random.choices(self.special, k=self.special_count)
        upp = random.choices(self.upper, k=self.upper_count)
        lower = random.choices(self.lower, k=self.lower_count)
        
        # Combine all characters into a single list
        ramz_list = num + spe + upp + lower

        # Shuffle the combined list and join the characters to form the password
        self.password = '' . join(random.sample(ramz_list, len(ramz_list)))

        # Display the generated password in the UI
        self.ui.password.setText(self.password)


# Create the application instance
app = QApplication(sys.argv)

# Create an instance of the PasswordGenerator class
pg = PasswordGenerator()

# Show the main window
pg.show()

# Start the application event loop
app.exec()
