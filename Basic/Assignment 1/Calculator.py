##### Mohammad Ali Mirzaei #####

import math

print("Welcome to my calculator dear")
print("============================")
print("+ : sum")
print("- : sub")
print("* : multiple")
print("/ : divide")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("sqrt")
print("factorial")

operation = input("Well, now choose your operation from above: ").lower()

if operation =="+" or operation =="-" or operation =="*" or operation =="/":
    A = float(input("Enter the fisrt number : "))
    B = float(input("Enter the second number : "))
else:
    C = float(input("Enter a number : "))

if operation == "+":
    result = A + B
elif operation == "-":
    result = A - B
elif operation == "*":
    result = A * B
elif operation == "/":
    if B == 0:
        result = print("Error! try again")
    else:
        result = A / B
elif operation == "sin":
    radians = math.radians(C)
    result = math.sin(radians)
elif operation == "cos":
    radians = math.radians(C)
    result = math.cos(radians)
elif operation == "tan":
    radians = math.radians(C)
    result = math.tan(radians)
elif operation == "cot":
    radians = math.radians(C)
    result = 1 / math.tan(radians)
elif operation == "log":
    result = math.log(C)
elif operation == "sqrt":
    result = math.sqrt(C)
elif operation == "factorial" :
    result = math.factorial(int(C))

print(f"Result: {result}")