##### Mohammad Ali Mirzaei #####

import random

Words_Bank = ["finance","english","work","play","cash","woman","life","freedom","iran","python"]
User_Hearts = 6
Right_Chars = []
Wrong_Chars = []

Word = random.choice(Words_Bank)

while User_Hearts > 0:

    print(f"Your hearts : {User_Hearts}")

    if sorted("".join(set(Right_Chars))) == sorted([*("".join(set(Word)))]):
                print("You did it!")
                break

    for i in range(len(Word)):
        if Word[i] in Right_Chars:
           print(Word[i] , end=" ")
        else: 
           print("- " , end="")

    User_Char = input("Please write your guess : ").lower()
    if len(User_Char) == 1:
        if User_Char in Word:
            Right_Chars.append(User_Char)
            print("Nice✅")
        else:
            Wrong_Chars.append(User_Char)
            User_Hearts -= 1
            print("Wrong❌")
    else:
        print("Please enter only one character🚫 ")

if User_Hearts == 0:
    print("You lost💔")
