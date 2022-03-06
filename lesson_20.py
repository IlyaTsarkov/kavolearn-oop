class Number:
    def __init__(self, x):
        self.x = x

    def __or__(self, other):
        return self.x | other.x

    def __xor__(self, other):
        return self.x ^ other.x

    def __and__(self, other):
        return self.x & other.x


ex_1 = Number(13)
ex_2 = Number(10)
print(ex_1 | ex_2)
print(ex_1 ^ ex_2)
print(ex_2 & ex_1)

