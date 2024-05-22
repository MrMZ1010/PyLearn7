##### Mohammad Ali Mirzaei #####


CM = float(input("Enter your height in CM : ")) / 100
KG = float(input("Enter your weight in KG : "))
BMI = KG / CM ** 2

if BMI < 18.5 :
    print("Underweight")
elif 18.5 <= BMI <= 24.9 :
    print("Normal Weight")
elif 25 <= BMI <= 29.9 :
    print("Overweight")
elif 30 <= BMI <= 34.9 :
    print("Obesity")
elif 35 <= BMI <= 39.9 :
    print("Extreme Obesity")