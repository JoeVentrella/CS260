
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


# Fraction Class
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        if self.den == 0:
            raise ZeroDivisionError("Cant use 0 in denominator")


    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherFraction):

        newNum = self.num *otherFraction.den + self.den *otherFraction.num
        newDen = self.den *otherFraction.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __mul__(self, other):

        newNum = self.num * other.num
        newDen = self.den * other.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __sub__(self, other):

        newNum = self.num*other.den - self.den *other.num
        newDen = self.den *other.den
        common = gcd(newNum, newDen)

        return Fraction(newNum//common, newDen//common)

    def __eq__(self, other):

        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum == secondNum

    def __lt__(self, other):

        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum < secondNum

    def __gt__(self, other):

        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum > secondNum




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
f14 = Fraction(2,3)

'''
if __name__ == "__main__": This line should be in all files
Testing a comment change
Making another change from my computer
'''
