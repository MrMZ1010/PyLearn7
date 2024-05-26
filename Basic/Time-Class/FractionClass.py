##### MohammadAli Mirzaei #####

# Import the gcd function from the math module
from math import gcd

# Define a class named Fraction
class Fraction:
    
    # Define the constructor method to initialize a Fraction object with numerator (n) and denominator (d)
    def __init__(self, n, d):
        self.Numerator = n
        self.Denominator = d
    
    # Define a method to perform addition of two fractions
    def Sum(self, other):
        Result_Numerator = other.Numerator * self.Denominator + other.Denominator * self.Numerator
        Result_Denominator = self.Denominator * other.Denominator
        return Fraction(Result_Numerator, Result_Denominator)
    
    # Define a method to perform multiplication of two fractions
    def Mul(self, other):
        Result_Numerator = self.Numerator * other.Numerator
        Result_Denominator = self.Denominator * other.Denominator
        return Fraction(Result_Numerator, Result_Denominator)
    
    # Define a method to perform subtraction of two fractions
    def Minus(self, other):
        Numerator = (self.Numerator * other.Denominator)
        Numerator2 = (other.Numerator * self.Denominator)
        Result_Numerator = Numerator - Numerator2
        Result_Denominator = self.Denominator * other.Denominator
        return Fraction(Result_Numerator, Result_Denominator)
    
    # Define a method to perform division of two fractions
    def Divide(self, other):
        Result_Numerator = self.Numerator * other.Denominator
        Result_Denominator = self.Denominator * other.Numerator
        return Fraction(Result_Numerator, Result_Denominator)
    
    # Define a method to convert a fraction to a floating-point number
    def Fraction_To_Int(self):
        return self.Numerator / self.Denominator
    
    # Define a method to simplify the fraction by finding the greatest common divisor (GCD)
    def Simplify(self):
        GCD = gcd(self.Numerator, self.Denominator)
        return Fraction(self.Numerator // GCD, self.Denominator // GCD)

    
    