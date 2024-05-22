##### Mohammad Ali Mirzaei #####

import random

Computer_Number = random.randint(1,100)
Counter = 0

while True :

    User_Guess = int(input(f"Enter your {Counter + 1} guess : "))
    if User_Guess == Computer_Number :
        print(f"That is correct ✅ | your guesses were {Counter + 1}")
        User = input("Do you want to continue ? (yes or no) ").lower()
        if User == "yes" :
            Computer_Number = random.randint(1,100)
            Counter = 0
            continue
        else:
            print("GoodBye😘")
            break
    elif User_Guess > Computer_Number : 
        print("Go down 🔽")
    elif User_Guess < Computer_Number : 
        print("Go up 🔼")
    Counter += 1


    