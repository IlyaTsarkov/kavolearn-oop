class Number:
    def __init__(self, x):
        self.x = x

    def __lshift__(self, other):
        if isinstance(other, int):
            return self.x << other

    def __rshift__(self, other):
        if isinstance(other, int):
            return self.x >> other


ex_1 = Number(20)
print(ex_1 << 1)
print(ex_1 << 2)
print(ex_1 << 3, '\n')
print(ex_1 >> 1)
print(ex_1 >> 2)
print(ex_1 >> 3)

