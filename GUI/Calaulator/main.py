##### MohammadAli Mirzaei #####

import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

# Initialize variables
First_Num = 0
opr = ''

# Function to display result on the calculator interface
def Show_Result(num):
    window.temp.setText(num)

# Function to set numbers on the calculator display
def SetNum(nums):
    c = window.temp.text()
    if c == "0":
        window.temp.setText(nums)
    else:
        window.temp.setText(window.temp.text() + nums)

# Function to handle arithmetic operators
def Operator(operator):
    global First_Num, opr
    First_Num = window.temp.text()
    opr = operator
    window.temp.setText("")

# Function to perform arithmetic operations when equal button is pressed
def equal():
    global First_Num, opr
    b = window.temp.text()
    # Perform arithmetic operations based on the selected operator
    match opr:
        case '+':
            c = round(float(First_Num) + float(b), 10)
        case '-':
            c = round(float(First_Num) - float(b), 10)
        case '*':
            c = round(float(First_Num) * float(b), 10)
        case '/':
            c = round(float(First_Num) / float(b), 10)
    
    window.temp.setText(str(c))

# Function to clear the calculator display
def Clean():
    global First_Num 
    First_Num = ''
    window.temp.setText('')

# Function to perform trigonometric and logarithmic operations
def Triangle(func):
    temp = int(window.temp.text())
    x = 0
    # Perform trigonometric and logarithmic operations based on the selected function
    match func:
        case 'sin':
            x = math.sin(math.radians(temp))
        case 'cos':
            x = math.cos(math.radians(temp))
        case 'tan':
            x = math.tan(math.radians(temp))
        case 'cot':
            x = 1 / math.tan(math.radians(temp))
        case 'log':
            x = math.log10(temp)
    
    window.temp.setText(str(x))

# Function to calculate square root
def sqrt():
    x = float(window.temp.text())
    window.temp.setText(str(math.sqrt(x)))

# Load UI and set up connections
loader = QUiLoader()
app = QApplication([])
window = loader.load("ui.ui")

# Connect number buttons to SetNum function
window.b1.clicked.connect(partial(SetNum, "1"))
window.b2.clicked.connect(partial(SetNum, "2"))
window.b3.clicked.connect(partial(SetNum, "3"))
window.b4.clicked.connect(partial(SetNum, "4"))
window.b5.clicked.connect(partial(SetNum, "5"))
window.b6.clicked.connect(partial(SetNum, "6"))
window.b7.clicked.connect(partial(SetNum, "7"))
window.b8.clicked.connect(partial(SetNum, "8"))
window.b9.clicked.connect(partial(SetNum, "9"))
window.point.clicked.connect(partial(SetNum, "."))
window.z.clicked.connect(partial(SetNum, "0"))
window.zz.clicked.connect(partial(SetNum, "00"))

# Connect arithmetic operator buttons to Operator function
window.plus.clicked.connect(partial(Operator, '+'))
window.neg.clicked.connect(partial(Operator, '-'))
window.mul.clicked.connect(partial(Operator, '*'))
window.div.clicked.connect(partial(Operator, '/'))

# Connect equal button to equal function
window.equal.clicked.connect(equal)

# Connect trigonometric and logarithmic function buttons to Triangle function
window.sin.clicked.connect(partial(Triangle, 'sin'))
window.cos.clicked.connect(partial(Triangle, 'cos'))
window.tan.clicked.connect(partial(Triangle, 'tan'))
window.cot.clicked.connect(partial(Triangle, 'cot'))
window.log.clicked.connect(partial(Triangle, 'log'))

# Connect square root button to sqrt function
window.sqrt.clicked.connect(sqrt)

# Connect clear button to Clean function
window.c.clicked.connect(Clean)

# Show the calculator interface
window.show()

# Execute the application event loop
app.exec()

