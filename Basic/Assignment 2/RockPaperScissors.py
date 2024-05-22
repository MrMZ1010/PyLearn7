##### Mohammad Ali Mirzaei #####

import random

Computer_Score = 0
User_Score = 0
Choices_List = ["rock" , "paper" , "scissors"]

while True :

    Computer_Choice = random.choice(Choices_List)
    User_Choice = input("Enter your choice (rock | paper | scissors) (exit = exit) : ").lower()

    if User_Choice == "exit" :
        break
    print(f"Computer : {Computer_Choice}")

    if Computer_Choice == "paper" and User_Choice == "rock":
        Computer_Score += 1
    
    elif Computer_Choice == "rock" and User_Choice == "scissors":
        Computer_Score += 1
    
    elif Computer_Choice == "scissors" and User_Choice == "paper":
        Computer_Score  += 1

    elif Computer_Choice == "paper" and User_Choice == "scissors":
        User_Score += 1

    elif Computer_Choice == "rock" and User_Choice == "paper":
        User_Score += 1

    elif Computer_Choice == "scissors" and User_Choice == "rock":
        User_Score += 1

    elif Computer_Choice == "paper" and User_Choice == "paper":
        continue
        
    elif Computer_Choice == "rock" and User_Choice == "rock":
        continue
       
    elif Computer_Choice == "scissors" and User_Choice == "scissors":
        continue

    print(f"You : {User_Score}")
    print(f"Computer : {Computer_Score}")

print("GoodBye😘")
