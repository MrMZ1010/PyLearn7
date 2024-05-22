##### Mohammad Ali Mirzaei #####

from math import gcd

class Fraction:

    def __init__(self, n, d):

        self.Numerator = n
        self.Denominator = d

    def Sum(self, other):

        Result_Numerator = other.Numerator * self.Denominator + other.Denominator * self.Numerator
        Result_Denominator = self.Denominator * other.Denominator
        return Fraction(Result_Numerator, Result_Denominator)

    def Mul(self, other):

        Result_Numerator = self.Numerator * other.Numerator
        Result_Denominator = self.Denominator * other.Denominator
        return Fraction(Result_Numerator, Result_Denominator)

    def Minus(self, other):

        Numerator = (self.Numerator * other.Denominator)
        Numerator2 = (other.Numerator * self.Denominator)
        Result_Numerator = Numerator - Numerator2
        Result_Denominator = self.Denominator * other.Denominator
        return Fraction(Result_Numerator, Result_Denominator)

    def Divide(self, other):

        Result_Numerator = self.Numerator * other.Denominator
        Result_Denominator = self.Denominator * other.Numerator
        return Fraction(Result_Numerator, Result_Denominator)

    def Fraction_To_Int(self):


        return self.Numerator / self.Denominator

    def Simplify(self):

        GCD = gcd(self.Numerator, self.Denominator)
        return Fraction(self.Numerator // GCD, self.Denominator // GCD)

    
    