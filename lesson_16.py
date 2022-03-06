class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __pos__(self):
    #     return +self.b
    #
    # def __neg__(self):
    #     return -self.b

    def __invert__(self):
        self.a, self.b = self.b, self.a
        return self.a, self.b


ex_1 = Numbers(5, -10)
print(ex_1.__invert__())
