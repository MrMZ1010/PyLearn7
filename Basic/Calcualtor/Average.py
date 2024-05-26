##### MohammadAli Mirzaei #####

# Prompt the user to enter the first score, convert the input to a float, and store it in FirstScore
FirstScore = float(input("Enter the first score : "))

# Prompt the user to enter the second score, convert the input to a float, and store it in SecondScore
SecondScore = float(input("Enter the second score : "))

# Prompt the user to enter the third score, convert the input to a float, and store it in ThirdScore
ThirdScore = float(input("Enter the third score : "))

# Calculate the average of the three scores and store it in Average
Average = (FirstScore + SecondScore + ThirdScore) / 3

# Check if the average score is greater than or equal to 17
if Average >= 17 :
    # Print a message indicating the average score is great
    print(f"Your Average is {Average} and it is great")

# Check if the average score is between 12 (inclusive) and 17 (exclusive)
elif 17 > Average >= 12 :
    # Print a message indicating the average score is normal
    print(f"Your Average is {Average} and it is normal")

# Check if the average score is less than 12
elif Average < 12 :
    # Print a message indicating the average score is a failure
    print(f"Your Average is {Average} and it is a failure")
