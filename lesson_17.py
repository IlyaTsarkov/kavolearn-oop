import math


class Rounding:
    def __init__(self, a):
        self.a = a

    def __round__(self, n=None):     # == def round(self):
        return round(self.a, n)             # return round(self.a)

    def __floor__(self):             # == def floor(self):            ==   def floor(self):
        return math.floor(self.a)           # return int(self.a)               return math.float(self.a)

    def __ceil__(self):              # == def ceil(self):             ==   def ceil(self):
        return math.ceil(self.a)            # return int(self.a)               return math.ceil(self.a)

    def __trunc__(self):             # == def trunc(self):            ==   def trunc(self):
        return math.trunc(self.a)           # return int(self.a) + 1           return math.trunc(self.a)


ex_1 = Rounding(3.14159)
print(ex_1.__round__(3))
print(ex_1.__floor__())
print(ex_1.__ceil__())
print(ex_1.__trunc__())




