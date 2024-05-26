##### MohammadAli Mirzaei #####

import random  # Import the random module to generate random numbers

# Start an infinite loop
while True:
    # Ask the user to input either 'roll' or 'exit', convert the input to lowercase
    User = input("Enter (roll) or (exit) : ").lower()

    # Check if the user wants to exit
    if User == "exit":
        print("GoodBye😘")
        break  # Exit the loop if the user inputs 'exit'
    else:
        # Generate a random number between 1 and 6 to simulate rolling a dice
        Dice_Number = random.randint(1, 6)
        print(f"Dice = {Dice_Number}")  # Print the result of the dice roll
        # Check if the dice roll resulted in a 6
        if Dice_Number == 6:
            print("Congratulations!, here, take another one")
            # Roll another dice if the result is 6
            Dice_Number = random.randint(1, 6)
            print(f"Dice = {Dice_Number}")  # Print the result of the second dice roll

    



