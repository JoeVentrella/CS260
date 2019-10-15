
# Fraction Class
class Fraction:
    def __init__(self, top, bottom):
        """"
        Constructor for fraction
        Throws value error for zero denominators
        """
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise TypeError("Numerator and denominator must be of type int")

        if bottom == 0:
            raise ValueError("Denominators must not be zero.")

        if bottom < 0:
            if top < 0:
                top = abs(top)
            else:
                top *= -1
            bottom = abs(bottom)
        self.num = top
        self.den = bottom


    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        """"
        Returns a string representation of the fraction
        """
        return str(self.num) + "/" + str(self.den)

    def gcd(m, n):
        """
        Returns the GCD to help reduce fractions
        """
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, otherFraction):
        """
        Adds Fractions and reduces the answer
        """
        newNum = self.num *otherFraction.den + self.den *otherFraction.num
        newDen = self.den *otherFraction.den
        common = Fraction.gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __mul__(self, other):
        """
        Multiplies fractions and reduces the answer
        """
        newNum = self.num * other.num
        newDen = self.den * other.den
        common = Fraction.gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __sub__(self, other):
        """
        Subtraction for fraction class returns reduced answer
        """
        newNum = self.num*other.den - self.den *other.num
        newDen = self.den *other.den
        common = Fraction.gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __eq__(self, other):
        """
        Compares two fractions returns true if they are equal
        """
        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum == secondNum

    def __lt__(self, other):
        """
        Compares two fractions returns true if first fraction is less than second
        """
        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum < secondNum

    def __gt__(self, other):
        """
        Compares two fractions returns true if first is greater than second
        """
        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum > secondNum



def main():

    myF = Fraction(3,5)
    myF.show()
    print("I ate aproximately ", myF, "of the remaining Ice Cream")
    f1 = Fraction(1, 10)
    f2 = Fraction(3, 5)
    f3 = f1 +f2
    print(f3)
    f4 = f1 *f2
    print(f4)
    f5 = Fraction(1 ,2)
    f6 = Fraction(1 ,4)
    f7 = f5 - f6
    print(f7)
    f10 = Fraction(3 ,5)
    f11 = Fraction(3 ,5)
    print(f10 == f11)
    print(f10 < f11)
    f12 = Fraction(4,5)
    f13 = Fraction(2,3)
    print(f12 > f13)
    f14 = Fraction(-2,-1)
    print(f14)

main()
