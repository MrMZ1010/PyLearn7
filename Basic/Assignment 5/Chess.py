##### Mohammad Ali Mirzaei #####

def Table(Row,Colmun):

    for i in range(Row) :
        for j in range(Colmun) :

            if (i + j) % 2 == 0 :
                print("⬛",end="")
            else:
                print("⬜",end="")
        print()

Table(int(input("Enter the row : ")) , int(input("Enter the colmun : ")))

