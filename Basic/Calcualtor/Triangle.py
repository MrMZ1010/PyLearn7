##### MohammadAli Mirzaei #####

# Prompt the user to enter the first angle, convert the input to an integer, and store it in First_Angle
First_Angle = int(input("Enter the first angle: "))

# Prompt the user to enter the second angle, convert the input to an integer, and store it in Second_Angle
Second_Angle = int(input("Enter the second angle: "))

# Prompt the user to enter the third angle, convert the input to an integer, and store it in Third_Angle
Third_Angle = int(input("Enter the third angle: "))

# Check if the sum of any two angles is greater than the third angle
# This condition checks if the angles can form a valid triangle
if Third_Angle < (First_Angle + Second_Angle) and Second_Angle < (Third_Angle + First_Angle) and First_Angle < (Second_Angle + Third_Angle):
    # Print "Possible" if the angles satisfy the triangle inequality theorem
    print("Possible")
else:
    # Print "Impossible" if the angles do not satisfy the triangle inequality theorem
    print("Impossible")
