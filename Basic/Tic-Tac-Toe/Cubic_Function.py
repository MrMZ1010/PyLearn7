##### MohammadAli Mirzaei #####

import math

import math  # Module for mathematical operations

def Function_Solver(a, b, c, d):
    # Normalizing coefficients
    a, b, c = b/a, c/a, d/a

    # Calculating coefficients of the depressed cubic
    q = (3*c - (b**2))/9
    r = (9*b*c - 27*d - 2*(b**3))/54
    d = q**3 + r**2

    # Checking discriminant
    if d >= 0:
        # Calculating roots for real discriminant
        s = math.cbrt(r + math.sqrt(d))
        t = math.cbrt(r - math.sqrt(d))

        # Calculating roots
        x1 = -b/3 + (s + t)
        x2 = -b/3 - (s + t)/2 + math.sqrt(3)*(s - t)*1j/2  # Complex root
        x3 = -b/3 - (s + t)/2 - math.sqrt(3)*(s - t)*1j/2  # Complex root

    else:
        # Calculating roots for complex discriminant
        th = math.acos(r/math.sqrt(-(q**3)))
        x1 = 2*math.sqrt(-q)*math.cos(th/3) - b/3
        x2 = 2*math.sqrt(-q)*math.cos((th + 2*math.pi)/3) - b/3
        x3 = 2*math.sqrt(-q)*math.cos((th + 4*math.pi)/3) - b/3

    return (x1, x2, x3)

# Getting coefficients from user
a = int(input(("Enter a : ")))
b = int(input(("Enter b : ")))
c = int(input(("Enter c : ")))
d = int(input(("Enter d : ")))

# Solving the function
Roots = Function_Solver(a, b, c, d)

print(F"Roots: {Roots}")  # Printing the roots
