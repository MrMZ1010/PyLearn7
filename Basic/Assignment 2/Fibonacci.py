##### Mohammad Ali Mirzaei #####


Number = int(input("Enter a number : "))
A , B = 1 , 1
for i in range(Number) :
    print(A , end=" ")
    A , B = B , A + B
