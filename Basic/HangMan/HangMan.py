##### Mohammad Ali Mirzaei #####

# Import the random module for generating random numbers and making random selections
import random

# Define a list of words for the user to guess
Words_Bank = ["finance", "english", "work", "play", "cash", "woman", "life", "freedom", "iran", "python"]

# Initialize the number of chances the user has
User_Hearts = 6
# Initialize a list to store correctly guessed characters
Right_Chars = []
# Initialize a list to store incorrectly guessed characters
Wrong_Chars = []

# Randomly select a word from the Words_Bank list
Word = random.choice(Words_Bank)

# Start a loop that continues until the user runs out of chances
while User_Hearts > 0:
    # Print the number of remaining chances (hearts) to the user
    print(f"Your hearts : {User_Hearts}")

    # Check if all unique characters in the word have been correctly guessed
    if sorted("".join(set(Right_Chars))) == sorted([*("".join(set(Word)))]):
        # If all characters have been guessed, print a success message and exit the loop
        print("You did it!")
        break

    # Iterate through each character in the word
    for i in range(len(Word)):
        # Check if the character has been correctly guessed
        if Word[i] in Right_Chars:
            # If the character has been guessed, print it
            print(Word[i], end=" ")
        else:
            # If the character has not been guessed, print a dash
            print("- ", end="")

    # Prompt the user to input a guess and convert it to lowercase
    User_Char = input("Please write your guess : ").lower()

    # Check if the user's input is a single character
    if len(User_Char) == 1:
        # Check if the guessed character is in the word
        if User_Char in Word:
            # If the guess is correct, add the character to the list of correct guesses
            Right_Chars.append(User_Char)
            # Print a success message
            print("Nice✅")
        else:
            # If the guess is incorrect, add the character to the list of incorrect guesses,
            # decrement the number of chances, and print a failure message
            Wrong_Chars.append(User_Char)
            User_Hearts -= 1
            print("Wrong❌")
    else:
        # If the user's input is not a single character, print a message asking for a single character
        print("Please enter only one character🚫 ")

# Check if the user has run out of chances
if User_Hearts == 0:
    # If the user has run out of chances, print a message indicating that they lost
    print("You lost💔")

