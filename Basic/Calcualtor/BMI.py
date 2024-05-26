##### MohammadAli Mirzaei #####


# Prompt the user to enter their height in centimeters, convert it to a float, then divide by 100 to convert to meters, and store it in CM
CM = float(input("Enter your height in CM: ")) / 100

# Prompt the user to enter their weight in kilograms, convert it to a float, and store it in KG
KG = float(input("Enter your weight in KG: "))

# Calculate the Body Mass Index (BMI) using the formula: weight (KG) divided by the square of height (CM)
BMI = KG / CM ** 2

# Check if the BMI is less than 18.5
if BMI < 18.5:
    # Print "Underweight" if the condition is true
    print("Underweight")

# Check if the BMI is between 18.5 (inclusive) and 24.9 (inclusive)
elif 18.5 <= BMI <= 24.9:
    # Print "Normal Weight" if the condition is true
    print("Normal Weight")

# Check if the BMI is between 25 (inclusive) and 29.9 (inclusive)
elif 25 <= BMI <= 29.9:
    # Print "Overweight" if the condition is true
    print("Overweight")

# Check if the BMI is between 30 (inclusive) and 34.9 (inclusive)
elif 30 <= BMI <= 34.9:
    # Print "Obesity" if the condition is true
    print("Obesity")

# Check if the BMI is between 35 (inclusive) and 39.9 (inclusive)
elif 35 <= BMI <= 39.9:
    # Print "Extreme Obesity" if the condition is true
    print("Extreme Obesity")
