def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, a, b):
        g = gcd(a, b)
        self.a = a // g
        self.b = b // g

    def __str__(self):
        if self.b == 1:
            return f"{self.a}"
        else:
            return f"{self.a}/{self.b}"

    def __add__(self, other):
        return Fraction(
            self.a * other.b + other.a * self.b,
            self.b * other.b
        )
