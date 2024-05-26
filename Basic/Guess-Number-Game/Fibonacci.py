##### MohammadAli Mirzaei #####

# Take user input for a number
Number = int(input("Enter a number : "))

# Initialize variables A and B to 1, representing the first two Fibonacci numbers
A, B = 1, 1

# Iterate through a range from 0 to Number - 1
# This loop will generate the Fibonacci sequence up to the specified number of terms
for i in range(Number):
    # Print the current Fibonacci number (variable A)
    print(A, end=" ")
    
    # Update variables A and B to generate the next Fibonacci number
    # The next Fibonacci number is the sum of the previous two numbers
    A, B = B, A + B

