##### Mohammad Ali Mirzaei #####

Number = int(input("Please enter a number : "))

Result = False
First = 1

for num in range(1,Number+1) :

    First *= num
    if First == Number :
        Result = True
print(Result)        
