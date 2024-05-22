##### Mohammad Ali Mirzaei #####

FirstScore = float(input("Enter the fisrt score : "))
SecondScore = float(input("Enter the second score : "))
ThirdScore = float(input("Enter the third score : "))

Average = (FirstScore + SecondScore + ThirdScore) / 3
if Average >= 17 :
    print(f"Your Average is {Average} and it is great")
elif 17 > Average >= 12 :
    print(f"Your Average is {Average} and it is normal")
elif Average < 12 :
    print(f"Your Average is {Average} and it is a failure")
