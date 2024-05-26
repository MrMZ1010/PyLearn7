##### MohammadAli Mirzaei #####

import random  # Import the random module to make random choices

# Initialize variables to keep track of scores
Computer_Score = 0
User_Score = 0

# List of choices for the game
Choices_List = ["rock", "paper", "scissors"]

# Start an infinite loop for the game
while True:
    # Generate a random choice for the computer
    Computer_Choice = random.choice(Choices_List)
    # Prompt the user to enter their choice
    User_Choice = input("Enter your choice (rock | paper | scissors) (exit = exit) : ").lower()

    # Check if the user wants to exit the game
    if User_Choice == "exit":
        break
    
    # Print the computer's choice
    print(f"Computer : {Computer_Choice}")

    # Determine the winner and update scores based on choices
    if (Computer_Choice == "paper" and User_Choice == "rock") or \
       (Computer_Choice == "rock" and User_Choice == "scissors") or \
       (Computer_Choice == "scissors" and User_Choice == "paper"):
        Computer_Score += 1
    elif (Computer_Choice == "paper" and User_Choice == "scissors") or \
         (Computer_Choice == "rock" and User_Choice == "paper") or \
         (Computer_Choice == "scissors" and User_Choice == "rock"):
        User_Score += 1

    # If both choices are the same, it's a tie, so no scores are updated

    # Print the current scores
    print(f"You : {User_Score}")
    print(f"Computer : {Computer_Score}")

# Print a goodbye message when the user decides to exit the game
print("GoodBye😘")
