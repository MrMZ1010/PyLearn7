##### MohammadAli Mirzaei #####

import sys
import random
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from main_ui import Ui_MainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.araye = ["number", "special", "upper", "lower"]
        self.number = "1234567890"
        self.special = "!@#$%^&*(){<>?}[=-]|"
        self.upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.lower = self.upper.lower()

        self.ui.btn_generate.clicked.connect(self.generate_pass)

    def generate_pass(self):
        self.password = ""
        r_standard = self.ui.radio_standard.isChecked()
        r_strong = self.ui.radio_strong.isChecked()
        r_super = self.ui.radio_super.isChecked()

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

        self.lower_count = self.strlen - (
            self.number_count + self.special_count + self.upper_count
        )

        num = random.choices(self.number, k=self.number_count)
        spe = random.choices(self.special, k=self.special_count)
        upp = random.choices(self.upper, k=self.upper_count)
        lower = random.choices(self.lower, k=self.lower_count)
        ramz_list = num + spe + upp + lower

        self.password = '' . join(random.sample(ramz_list, len(ramz_list)))

        self.ui.password.setText(self.password)


app = QApplication(sys.argv)
pg = PasswordGenerator()
pg.show()
app.exec()