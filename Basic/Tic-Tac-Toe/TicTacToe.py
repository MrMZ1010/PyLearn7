##### MohammadAli Mirzaei #####

import datetime  # Module for working with dates and times
import random  # Module for generating random numbers
import pyfiglet  # Module for creating ASCII art text
from colorama import Fore  # Module for adding color to text in terminals


def Menu():
    # Generate ASCII art text for the game title
    title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
    print(title)
    print("Choose one of the following two modes:")
    print("1. Player VS Cpu")
    print("2. Player VS Player")


def Game_Mode():
    # Function to get the game mode choice from the user
    user_choice = int(input())  # Get user input as integer
    return user_choice


def Board():
    # Function to display the current state of the game board
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + "X", end=" ")  # Print 'X' in red color
            elif cell == "O":
                print(Fore.BLUE + "O", end=" ")  # Print 'O' in blue color
            else:
                print(Fore.RESET + cell, end=" ")  # Reset color and print empty cell
        print(Fore.RESET)  # Reset color at the end of each row


def Inputs(role, temp):
    # Function to get user input for placing marks on the board
    while True:
        print(f"\n{role}")

        if role == "Cpu":
            # For CPU role, generate random row and column
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game_board[row][col] == "-":  # Check if the cell is empty
                game_board[row][col] = temp  # Place mark in the empty cell
                print("Row:", row + 1)  # Print CPU's chosen row
                print("Col:", col + 1)  # Print CPU's chosen column
                break
        else:
            row = int(input("Row (1 - 3): "))  # Get row input from the player
            col = int(input("Col (1 - 3): "))  # Get column input from the player

            if 1 <= row <= 3 and 1 <= col <= 3:  # Check if input is within board range
                if game_board[row - 1][col - 1] == "-":  # Check if the cell is empty
                    game_board[row - 1][col - 1] = temp  # Place mark in the empty cell
                    break
                else:
                    print("This cell is filled! Please try again.")  # Inform player of filled cell
            else:
                print("Row and Column must be between (1,3)!")  # Inform player of invalid input


def Checker(role: str, temp: str, startTime: int):
    # Function to check for a winner or a draw
    if Win(temp) == True:  # Check if the current player has won
        print(f"\n{role} wins!")  # Print winner message
        endTime = datetime.datetime.now().replace(microsecond=0)  # Get current time
        print("Game Duration:", endTime - startTime)  # Print game duration
        exit()  # Exit the game
    else:
        if Draw() == True:  # Check if the game is a draw
            print("\nDraw!")  # Print draw message
            endTime = datetime.datetime.now().replace(microsecond=0)  # Get current time
            print("Game Duration:", endTime - startTime)  # Print game duration
            exit()  # Exit the game


def Win(temp: str):
    # Function to check if there's a winning condition on the board
    win = False

    for i in range(3):
        if (game_board[i][0] == game_board[i][1] == game_board[i][2] == temp) or (game_board[0][i] == game_board[1][i] == game_board[2][i] == temp):
            win = True
            break
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] == temp) or (game_board[0][2] == game_board[1][1] == game_board[2][0] == temp):
        win = True
    
    return win


def Draw():
    # Function to check if the game is a draw
    if not any("-" in i for i in game_board):
        return True
    else:
        return False


def Game_Play(user_choice):
    # Function to start the game
    Board()  # Display initial game board
    startTime = datetime.datetime.now().replace(microsecond=0)  # Get current time

    if user_choice == 1:  # Player VS CPU mode
        while True:
            Inputs("Player", "X")  # Get player's input
            Board()  # Display updated board
            Checker("Player", "X", startTime)  # Check for win or draw
            
            Inputs("Cpu", "O")  # Get CPU's input
            Board()  # Display updated board
            Checker("Cpu", "O", startTime)  # Check for win or draw

    elif user_choice == 2:  # Player VS Player mode
        while True:
            Inputs("Player1", "X")  # Get first player's input
            Board()  # Display updated board
            Checker("Player1", "X", startTime)  # Check for win or draw

            Inputs("Player2", "O")  # Get second player's input
            Board()  # Display updated board
            Checker("Player2", "O", startTime)  # Check for win or draw

    else:
        while True:
            print("The input is not valid!")  # Inform about invalid input
            choice = Game_Mode()  # Get valid input from the user

            if user_choice == 1:  # If user chose Player VS CPU mode
                break
            elif user_choice == 2:  # If user chose Player VS Player mode
                break
            
        Game_Play(user_choice)  # Start the game again with valid input


# Initialize the game board
game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

Menu()  # Display the game menu
Game_Play(Game_Mode())  # Start the game with user's choice
