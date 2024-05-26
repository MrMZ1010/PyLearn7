##### MohammadAli Mirzaei #####

import math  # Import the math module to perform mathematical operations

# Print welcome message and instructions
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

# Prompt the user to choose an operation from the list and convert the input to lowercase
operation = input("Well, now choose your operation from above: ").lower()

# Check if the operation is one of the basic arithmetic operations
if operation == "+" or operation == "-" or operation == "*" or operation == "/":
    # Prompt the user to enter the first number and convert it to a float, store it in A
    A = float(input("Enter the first number: "))
    # Prompt the user to enter the second number and convert it to a float, store it in B
    B = float(input("Enter the second number: "))
else:
    # For other operations, prompt the user to enter one number and convert it to a float, store it in C
    C = float(input("Enter a number: "))

# Perform the operation based on the user's choice
if operation == "+":
    # Add A and B
    result = A + B
elif operation == "-":
    # Subtract B from A
    result = A - B
elif operation == "*":
    # Multiply A and B
    result = A * B
elif operation == "/":
    # Check if B is zero to avoid division by zero error
    if B == 0:
        result = "Error! Division by zero"
    else:
        # Divide A by B
        result = A / B
elif operation == "sin":
    # Convert C to radians and calculate the sine
    radians = math.radians(C)
    result = math.sin(radians)
elif operation == "cos":
    # Convert C to radians and calculate the cosine
    radians = math.radians(C)
    result = math.cos(radians)
elif operation == "tan":
    # Convert C to radians and calculate the tangent
    radians = math.radians(C)
    result = math.tan(radians)
elif operation == "cot":
    # Convert C to radians and calculate the cotangent (1 / tan)
    radians = math.radians(C)
    result = 1 / math.tan(radians)
elif operation == "log":
    # Calculate the natural logarithm of C
    result = math.log(C)
elif operation == "sqrt":
    # Calculate the square root of C
    result = math.sqrt(C)
elif operation == "factorial":
    # Calculate the factorial of C, convert C to an integer
    result = math.factorial(int(C))

# Print the result of the operation
print(f"Result: {result}")
