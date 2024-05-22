##### Mohammad Ali Mirzaei #####

import random

while True :

    User = input("Enter (roll) or (exit) : ").lower()

    if User == "exit" :
        print("GoodBye😘")
        break
    else :
        Dice_Number = random.randint(1,6)
        print(f"Dice = {Dice_Number}")
        if Dice_Number == 6 :
            print("Congratulations!, here , take another one")
            Dice_Number = random.randint(1,6)
            print(f"Dice = {Dice_Number}")
    



