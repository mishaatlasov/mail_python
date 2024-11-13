def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            a = args[0]
            b = args[1]
        if len(args) == 1:
            a = args[0]
            b = 1
        if len(args) == 0:
            a = 0
            b = 1
        g = gcd(a, b)
        self.a = a // g
        self.b = b // g

    def __str__(self):
        if self.b == 1:
            return f"{self.a}"
        else:
            return f"{self.a}/{self.b}"

    def __add__(self, other):
        if type(self) is not Fraction:
            self = Fraction(self)
        if type(other) is not Fraction:
            other = Fraction(other)
        return Fraction(
            self.a * other.b + other.a * self.b,
            self.b * other.b)

    def __radd__(self, other):
        if type(self) is not Fraction:
            self = Fraction(self)
        if type(other) is not Fraction:
            other = Fraction(other)
        return Fraction(
            self.a * other.b + other.a * self.b,
            self.b * other.b)

    def __pos__(self):
        return Fraction(abs(self.a), abs(self.b))

    def __sub__(self, other):
        if type(self) is not Fraction:
            self = Fraction(self)
        if type(other) is not Fraction:
            other = Fraction(other)
        return Fraction(
            self.a * other.b - other.a * self.b,
            self.b * other.b)

    def __rsub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            other.a * self.b - self.a * other.b,
            self.b * other.b)

    def __neg__(self):
        return Fraction(-self.a, self.b)
