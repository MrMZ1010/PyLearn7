##### MohammadAli Mirzaei #####

# Prompt the user to enter a number and convert it to an integer
Number = int(input("Enter a number : "))

# Initialize an empty string to store the result
Result = ""

# Iterate from 0 to the entered number
for i in range(Number):
    # Check if the current number (i) is even
    if i % 2 == 0:
        # If the current number is even, add a '*' to the result string
        Result += "*"
    else:
        # If the current number is odd, add a '#' to the result string
        Result += "#"

# Print the resulting string
print(Result)
