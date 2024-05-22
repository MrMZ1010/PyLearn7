##### Mohammad Ali Mirzaei #####

Counter = 0
Scores = 0

while True :


    User = input(f"Enter the {Counter + 1}th score (exit = exit) : ").lower()

    if User == "exit" : 
        break
    else:
        Scores += int(User)
        Counter += 1

print(f"Your GPA is {Scores / Counter}")


