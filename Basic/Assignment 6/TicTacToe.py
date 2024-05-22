##### Mohammad Ali Mirzaei #####

import datetime
import random
import pyfiglet
from colorama import Fore


def Menu():

    tittle = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
    print(tittle)
    print("Choose one of the following two modes:")
    print("1. Player VS Cpu")
    print("2. Player VS Player")


def Game_Mode():

    user_choice = int(input())
    return user_choice


def Board():
    
    for Row in game_board:
        for cell in Row:
            if cell == "X":
                print(Fore.RED + "X", end = " ")
            elif cell == "O":
                print(Fore.BLUE + "O", end = " ")
            else:
                print(Fore.RESET + cell, end = " ")
        print(Fore.RESET)


def Inputs(role, temp):

    while True:
        print(f"\n{role}")

        if role == "Cpu":
           
            Row = random.randint(0, 2)
            Col = random.randint(0, 2)
            if game_board[Row][Col] == "-":
                game_board[Row][Col] = temp
                print("Row:", Row + 1)
                print("Col:", Col + 1)
                break
        else:
            Row = int(input("Row (1 - 3): "))
            Col = int(input("Col (1 - 3): "))

            if 1 <= Row <= 3 and 1 <= Col <= 3:
                if game_board[Row - 1][Col - 1] == "-":
                    game_board[Row - 1][Col - 1] = temp
                    break
                else:
                    print("This cell is filled! Please try again.")
            else:
                print("Row and Column must be between (1,3)!")
            

def Checker(role: str, temp: str, startTime: int):
    if Win(temp) == True:
        print(f"\n{role} wins!")
        endTime = datetime.datetime.now().replace(microsecond =0 )
        print("Game Duration:", endTime - startTime)
        exit()
    else:
        if Draw() == True:
            print("\nDraw!")
            endTime = datetime.datetime.now().replace(microsecond = 0)
            print("Game Duration:", endTime - startTime)
            exit()
            
            
def Win(temp: str):
    win = False

    for i in range(3):
        if (game_board[i][0] == game_board[i][1] == game_board[i][2] == temp) or (game_board[0][i] == game_board[1][i] == game_board[2][i] == temp):
            win = True
            break
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] == temp) or (game_board[0][2] == game_board[1][1] == game_board[2][0] == temp):
        win = True
    
    return win


def Draw():
    if not any("-" in i for i in game_board):
        return True
    else:
        return False


def Game_Play(user_choice):
    Board()
    startTime = datetime.datetime.now().replace(microsecond = 0)

    if user_choice == 1:
        while True:
            Inputs("Player", "X")
            Board()
            Checker("Player", "X", startTime)
            
            Inputs("Cpu", "O")
            Board()
            Checker("Cpu", "O", startTime)

    elif user_choice == 2:
        while True:
            Inputs("Player1", "X")
            Board()
            Checker("Player1", "X", startTime)

            Inputs("Player2", "O")
            Board()
            Checker("Player2", "O", startTime)

    else:
        while True:
            print("The input is not valid!")
            choice = Game_Mode()

            if user_choice == 1:
                break
            elif user_choice == 2:
                break
            
        Game_Play(user_choice)
               

game_board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

Menu()
Game_Play(Game_Mode())