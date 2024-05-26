##### MohammadAli Mirzaei #####

# Prompt the user to enter the first number and convert it to an integer
First_Number = int(input("Enter the first number : "))
# Prompt the user to enter the second number and convert it to an integer
Second_Number = int(input("Enter the second number : "))

# Ensure that First_Number is smaller than or equal to Second_Number
if First_Number > Second_Number:
    # Swap the values if First_Number is greater than Second_Number
    First_Number, Second_Number = Second_Number, First_Number

# Initialize a variable to store the greatest common divisor (GCD) of the two numbers
GCD = 1

# Find the greatest common divisor (GCD) of the two numbers using Euclid's algorithm
for i in range(1, First_Number + 1):
    if First_Number % i == 0 and Second_Number % i == 0:
        GCD = i

# Calculate the least common multiple (LCM) using the formula: LCM = (First_Number * Second_Number) / GCD
LCM = int((First_Number * Second_Number) / GCD)

# Print the result, which is the least common multiple (LCM) of the two numbers
print(f"LCM of {First_Number} and {Second_Number} is : {LCM} ")
