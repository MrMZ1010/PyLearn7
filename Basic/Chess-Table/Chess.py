##### MohammadAli Mirzaei #####

def Table(Row, Colmun):  # Defines a function named Table with two parameters, Row and Column.
    
    for i in range(Row):  # Iterates over each row.
        for j in range(Colmun):  # Iterates over each column.
            
            if (i + j) % 2 == 0:  # Checks if the sum of current row index and column index is even.
                print("⬛", end="")  # Prints a black square if the sum is even.
            else:
                print("⬜", end="")  # Prints a white square if the sum is odd.
        print()  # Moves to the next line after printing all columns in a row.

Table(int(input("Enter the row : ")), int(input("Enter the column : ")))  # Calls the Table function, taking user input for the number of rows and columns.

