##### MohammadAli Mirzaei #####

def Multi_Table(Row, Column):  # Defines a function named Multi_Table with two parameters, Row and Column.
    for i in range(Row + 1):  # Iterates over each row index from 0 to Row.
        for j in range(Column + 1):  # Iterates over each column index from 0 to Column.

            if i == 0 or j == 0:  # Checks if the current position is on the first row or first column.
                continue  # Skips printing multiplication results for cells in the first row or first column.
            else:
                Number = i * j  # Calculates the multiplication result for the current row and column.
                print(Number, end=" ")  # Prints the multiplication result followed by a space.

        print()  # Moves to the next line after printing all columns in a row.

Multi_Table(int(input("Enter the row : ")), int(input("Enter the column : ")))  # Calls the Multi_Table function, taking user input for the number of rows and columns.
