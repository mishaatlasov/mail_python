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
        print("loh")

    def __add__(self, other):
        return Fraction(
            self.a * other.b + other.a * self.b,
            self.b * other.b
        )

# print(Fraction(2, 4))
# print(Fraction(3, -9))
# print(Fraction(24, 12))
# print(Fraction(1, 3))
# print(Fraction(2, 4))
# print(Fraction(30, -90))
# print(Fraction(8, 2))
