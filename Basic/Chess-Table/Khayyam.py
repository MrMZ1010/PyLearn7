##### MohammadAli Mirzaei #####

def Pascal(number):  # Defines a function named Pascal with one parameter, 'number'.
    
    Triangle = []  # Initializes an empty list to store rows of Pascal's triangle.

    # Generates each row of Pascal's triangle.
    for i in range(number):  # Iterates over each row index from 0 to 'number - 1'.
        row = [1] * (i + 1)  # Creates a list with 'i + 1' elements, all initialized to 1.

        # Calculates the elements of the current row based on the previous row.
        for j in range(1, i):  # Iterates over each index of the current row except the first and last.
            row[j] = Triangle[i - 1][j - 1] + Triangle[i - 1][j]  # Calculates the element based on the elements of the previous row.

        Triangle.append(row)  # Appends the current row to the Pascal's triangle list.

    # Prints Pascal's triangle.
    for row in Triangle:  # Iterates over each row in Pascal's triangle.
        print(*row)  # Prints each element of the row separated by a space.

Pascal(int(input("Enter your number : ")))  # Calls the Pascal function, taking user input for the number of rows in Pascal's triangle.
