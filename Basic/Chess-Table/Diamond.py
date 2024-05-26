##### MohammadAli Mirzaei #####

def Show_Diamond(number):  # Defines a function named Show_Diamond with one parameter, 'number'.
    
    # Loop to print the upper half of the diamond.
    for num in range(number):  # Iterates over numbers from 0 to 'number' (exclusive).
        print(' ' * (number - num - 1), end='')  # Prints spaces to align the '*' characters properly.
        print('*' * (2 * num + 1))  # Prints '*' characters to form the diamond pattern.

    # Loop to print the lower half of the diamond.
    for num in range(number - 2, -1, -1):  # Iterates over numbers from 'number - 2' down to 0 in reverse order.
        print(' ' * (number - num - 1), end='')  # Prints spaces to align the '*' characters properly.
        print('*' * (2 * num + 1))  # Prints '*' characters to form the diamond pattern.

Show_Diamond(int(input("Enter your number : ")))  # Calls the Show_Diamond function, taking user input for the size of the diamond.
