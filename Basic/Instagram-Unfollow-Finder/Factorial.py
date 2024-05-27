##### MohammadAli Mirzaei #####

# Prompt the user to enter a number and convert the input to an integer
Number = int(input("Please enter a number : "))

# Initialize a variable to store the result of the check
Result = False

# Initialize a variable to keep track of the product of numbers
First = 1

# Iterate over a range of numbers from 1 to the input number (inclusive)
for num in range(1, Number + 1):
    # Multiply the current value of First by the current number in the loop
    First *= num
    # Check if the product is equal to the input number
    if First == Number:
        # If the product is equal to the input number, set the Result variable to True
        Result = True

# Print the result of the check (True if the input number is a factorial, False otherwise)
print(Result)
      
