##### MohammadAli Mirzaei #####

# Import the random module for generating random numbers
import random

# Prompt the user to enter a number and convert it to an integer
Number = int(input("Enter a number : "))

# Initialize an empty list to store unique random numbers
Numbers_List = []

# Iterate from 0 to the entered number
for i in range(Number):
    # Check if the current number (i) is not already in the Numbers_List
    if i not in Numbers_List:
        # If the current number is not in the list, append a random integer between 1 and 100 to the Numbers_List
        Numbers_List.append(random.randint(1, 100))

# Print the list of unique random numbers
print(Numbers_List)
