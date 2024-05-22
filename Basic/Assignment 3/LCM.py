##### Mohammad Ali Mirzaei #####

First_Number = int(input("Enter the first number : "))
Second_Number = int(input("Enter the second number : "))

if First_Number > Second_Number:
  First_Number, Second_Number = Second_Number, First_Number

for i in range(1,First_Number+1):
  if First_Number % i == 0 and Second_Number % i == 0:
    GCD = i

LCM = int((First_Number * Second_Number) / GCD)

print(f"LCM of {First_Number} and {Second_Number} is : {LCM} " )