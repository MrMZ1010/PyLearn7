##### MohammadAli Mirzaei #####

# Define a function named Carpet that takes a parameter Number
def Carpet(Number):
    # Import the choice function from the random module
    from random import choice
    
    # Define a list of different colored square emojis
    lst = ["🟥","🟧","🟨","🟩","🟦","🟪","🟫"]
    
    # Check if the input number is odd
    if Number % 2 != 0:
        # Loop through each row up to the value of Number
        for i in range(Number):
            # Loop through each column up to the value of Number
            for j in range(Number):
                # Check if the column index is even
                if j % 2 == 0:
                    # Randomly select a color from the list and print it
                    ch = choice(lst)
                    print(ch, end="")
                else:
                    # Randomly select a color from the list and print it
                    ch = choice(lst)
                    print(ch, end="")
            # Move to the next line after printing a row
            print()
    else:
        # Print a message indicating that an odd number is required for a wonderful carpet
        print("If you want a wonderful carpet, you should enter an odd number")

# Continuously prompt the user to enter a number and call the Carpet function with the input number
while True:
    Carpet(int(input("Enter a number: ")))
