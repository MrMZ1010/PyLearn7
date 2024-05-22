#### MohammadAli Mirzae #####

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from main_ui import Ui_mainWindow


class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.cal.clicked.connect(self.getItem)
        self.ui.combo_units.currentTextChanged.connect(self.changeUnit)
        self.ui.combo_from.currentTextChanged.connect(self.changeFrom)

        self.unit = {
            "weight": ["gram", "kilogram", "ton", "pound"],
            "length": ["mm", "cm", "meter", "km", "inch"],
            "temperature": ["centigrade", "fahrenheit", "kelvin"],
            "digital volume": [
                "bit",
                "byte",
                "kilobyte",
                "megabyte",
                "gigabyte",
                "terabyte",
            ],
        }

        self.unit_tabdil = {
            "Weight": {
                "gram": 1,
                "kilogram": 1000,
                "ton": 1000000,
                "pound": 500,
            },
            "length": {
                "mm": 1,
                "cm": 10,
                "meter": 1000,
                "km": 1000000,
                "inch": 25.4,
            },
            "temperature": {"centigrade": 1, "fahrenheit": 32, "kelvin": -273.15},
            "digital volume": {
                "bit": 1,
                "byte": 8,
                "kilobyte": 8000,
                "megabyte": 8000000,
                "gigabyte": 8000000000,
                "terabyte": 8000000000000,
            },
        }

    def getItem(self):
        comboUnit = str(self.ui.combo_units.currentText())
        comboFrom = str(self.ui.combo_from.currentText())
        comboTo = str(self.ui.combo_to.currentText())
        from_num = int(self.ui.text_from.text())
        from_ = self.unit_tabdil[comboUnit][comboFrom]
        to_ = self.unit_tabdil[comboUnit][comboTo]

        if comboUnit == "temperature":
            if comboFrom == "kelvin":
                cel_from = 273.15 + from_num
            elif comboFrom == "fahrenheit":
                cel_from = (from_num - 32) / 9.5
            else:
                cel_from = from_num

            if comboTo == "kelvin":
                cel_to = cel_from - 273.15
            elif comboTo == "fahrenheit":
                cel_to = (cel_from * 9.5) + 32
            else:
                cel_to = cel_from

            self.ui.text_to.setText(str(round(cel_to, 0)))

        else:
            tabdil = float((from_num * from_) / to_)
            self.ui.text_to.setText(str(round(tabdil, 2)))

    def changeUnit(self):
        unit_ = self.ui.combo_units.currentText()
        self.ui.combo_from.clear()
        self.ui.combo_to.clear()
        self.ui.combo_from.addItems(self.unit[unit_])

    def changeFrom(self):
        self.ui.combo_to.clear()
        unit_item = self.ui.combo_units.currentText()
        from_selected_item = self.ui.combo_from.currentIndex()
        self.ui.combo_to.addItems(self.unit[unit_item])
        self.ui.combo_to.removeItem(from_selected_item)


app = QApplication(sys.argv)

converter = Converter()
converter.changeUnit()
converter.show()

app.exec()