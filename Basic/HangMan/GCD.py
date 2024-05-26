##### MohammadAli Mirzaei #####

# Prompt the user to enter the first number and convert it to an integer, then store it in the variable 'First_Number'
First_Number = int(input("Enter the first number : "))

# Prompt the user to enter the second number and convert it to an integer, then store it in the variable 'Second_Number'
Second_Number = int(input("Enter the second number : "))

# Check if the first number is greater than the second number
if First_Number > Second_Number:
    # If the condition is true, swap the values of 'First_Number' and 'Second_Number'
    First_Number, Second_Number = Second_Number, First_Number

# Initialize a variable to store the greatest common divisor (GCD) of the two numbers
# Start with 1 since the GCD can't be less than 1
GCD = 1

# Iterate through the range of numbers from 1 to the smaller of the two numbers (First_Number)
for i in range(1, First_Number + 1):
    # Check if both 'First_Number' and 'Second_Number' are divisible by the current number (i)
    if First_Number % i == 0 and Second_Number % i == 0:
        # If both are divisible by 'i', update the GCD to the current value of 'i'
        GCD = i

# Print the result, which is the GCD of the two numbers
print(f"GCD of {First_Number} and {Second_Number} is : {GCD} ")
