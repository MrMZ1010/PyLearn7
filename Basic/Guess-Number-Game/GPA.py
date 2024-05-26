##### Mohammad Ali Mirzaei #####

# Initialize Counter to keep track of the number of scores entered
Counter = 0
# Initialize Scores to keep track of the sum of scores entered
Scores = 0

# Start an infinite loop
while True:
    # Prompt the user to enter a score, incrementing the counter for each input
    User = input(f"Enter the {Counter + 1}th score (exit = exit) : ").lower()

    # Check if the user wants to exit
    if User == "exit":
        break  # Exit the loop if the user inputs 'exit'
    else:
        # Add the entered score to the total Scores after converting it to an integer
        Scores += int(User)
        # Increment the Counter
        Counter += 1

# Calculate the GPA (average score) by dividing the total score by the number of scores entered
# Ensure Counter is not zero to avoid division by zero error
if Counter != 0:
    print(f"Your GPA is {Scores / Counter}")  # Print the GPA
else:
    print("No scores entered.")  # Print a message if no scores were entered



