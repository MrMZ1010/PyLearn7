##### Mohammad Ali Mirzaei #####

Number = int(input("Enter a number : "))
Result = ""

for i in range(Number):
    if i % 2 == 0 :
        Result += "*"
    else:
        Result += "#"
print(Result)