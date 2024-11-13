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

    def __repr__(self):
        if self.b == 1:
            return f"{self.a}"
        else:
            return f"{self.a}/{self.b}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.a * other.b + other.a * self.b,
            self.b * other.b
        )

    def __radd__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.b * other.a + other.b * self.a,
            self.b * other.b)

    def __pos__(self):
        return Fraction(abs(self.a), abs(self.b))

    def __sub__(self, other):
        if not isinstance(other, Fraction):
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

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            self.a * other.a,
            self.b * other.b)

    def __rmul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(
            other.a * self.a,
            other.b * self.b)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        other.a, other.b = other.b, other.a
        return Fraction(
            self.a * other.a,
            self.b * other.b)

    def __rtruediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        self.a, self.b = self.b, self.a
        return Fraction(
            other.a * self.a,
            other.b * self.b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.a * other.b == other.a * self.b:
            return True
        else:
            return False

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.a * other.b != other.a * self.b:
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.a * other.b > other.a * self.b:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.a * other.b < other.a * self.b:
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.a * other.b >= other.a * self.b:
            return True
        else:
            return False

    def __le__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.a * other.b <= other.a * self.b:
            return True
        else:
            return False

    def max_aliquot(self):
        c = (self.b + self.a - 1) // self.a
        return Fraction(1, c)

    def egyptian_decomposition(self):
        aliquotes_list = []
        x = Fraction(self.a, self.b)
        while x != 0:
            aliquotes_list.append(x.max_aliquot())
            x -= aliquotes_list[-1]
        print("+".join(map(str, aliquotes_list)))
        return aliquotes_list

    def turn(self):
        return Fraction(self.b, self.a)

    @staticmethod
    def from_continued(terms):
        all_summ = Fraction(1, terms[-1])
        for j in range(2, len(terms) + 1):
            all_summ = terms[-j] + all_summ
            all_summ = all_summ.turn()
        all_summ = all_summ.turn()
        return all_summ
