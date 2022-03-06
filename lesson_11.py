class Params:
    def __init__(self, height, width):
        self.h = height
        self.w = width

    def __bool__(self):
        return self.h != 0 or self.w != 0


ex_1 = Params(200, 300)
ex_2 = Params(0, 0)
print(bool(ex_1))
print(bool(ex_2))

