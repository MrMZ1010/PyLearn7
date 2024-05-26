##### MohammadAli Mirzaei #####

import random  # Import the random module to generate a random number

# Generate a random number between 1 and 100
Computer_Number = random.randint(1, 100)
# Initialize a counter to keep track of the number of guesses
Counter = 0

# Start an infinite loop for the guessing game
while True:
    # Prompt the user to enter their guess, incrementing the counter for each guess
    User_Guess = int(input(f"Enter your {Counter + 1} guess : "))
    
    # Check if the user's guess matches the computer's number
    if User_Guess == Computer_Number:
        # Print a success message along with the number of guesses it took
        print(f"That is correct ✅ | your guesses were {Counter + 1}")
        # Ask the user if they want to continue playing
        User = input("Do you want to continue ? (yes or no) ").lower()
        if User == "yes":
            # If the user wants to continue, generate a new random number and reset the counter
            Computer_Number = random.randint(1, 100)
            Counter = 0
            continue  # Continue to the next iteration of the loop
        else:
            print("GoodBye😘")  # If the user doesn't want to continue, print a goodbye message
            break  # Exit the loop
    # If the user's guess is higher than the computer's number, print "Go down"
    elif User_Guess > Computer_Number:
        print("Go down 🔽")
    # If the user's guess is lower than the computer's number, print "Go up"
    elif User_Guess < Computer_Number:
        print("Go up 🔼")
    
    # Increment the counter for the next guess
    Counter += 1



    