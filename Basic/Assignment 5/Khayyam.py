##### Mohammad Ali Mirzaei #####

def Pascal(number):

    Triangle = []

    for i in range(number):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = Triangle[i - 1][j - 1] + Triangle[i - 1][j]

        Triangle.append(row)

    for row in Triangle:
        print(*row)

Pascal(int(input("Enter your number : ")))