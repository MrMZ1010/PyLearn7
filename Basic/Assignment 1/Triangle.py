##### Mohammad Ali Mirzaei #####

First_Angle = int(input("Enter the first angle : "))
Second_Angle = int(input("Enter the second angle : "))
Third_Angle = int(input("Enter the third angle : "))

if Third_Angle < (First_Angle + Second_Angle) and Second_Angle < (Third_Angle + First_Angle) and First_Angle < (Second_Angle + Third_Angle) :
    print("Possible")
else:
    print("Impossible")