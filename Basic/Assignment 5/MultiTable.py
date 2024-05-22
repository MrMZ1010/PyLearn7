##### Mohammad Ali Mirzaei #####

def Multi_Table(Row,Column):
    for i in range(Row+1):
        for j in range(Column+1):

            if i == 0 or j == 0:
                continue
            else:
                Number = i * j
                print(Number,end=" ")

        print()

Multi_Table(int(input("Enter the row : ")),int(input("Enter the column : ")))