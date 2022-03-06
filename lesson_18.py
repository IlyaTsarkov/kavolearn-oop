class Number:
    def __init__(self, x):
        self.x = x

    def __floordiv__(self, other):
        if isinstance(other, Number):
            return self.x // other.x

    def __mod__(self, other):
        if isinstance(other, Number):
            return self.x % other.x

    def __pow__(self, power, modulo=None):
        if isinstance(power, Number):
            return self.x ** power.x


ex_1 = Number(20)
ex_2 = Number(5)
print(ex_1 // ex_2)
print(ex_1 % ex_2)
print(ex_1 ** ex_2)
print(Number.__pow__(ex_1, ex_1, ex_1))


