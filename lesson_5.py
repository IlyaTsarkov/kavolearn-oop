import math
import random


class Calculate:
    PI = math.pi

    def __init__(self, x):
        self.x = 30
        if self.random(x, 100) > 50:
            self.x = x

        print(self.x, self.square_circle(x))

    def square_x(self):
        return self.x ** 2

    @staticmethod
    def random(a, b):
        return random.randint(a, b)

    @classmethod
    def square_circle(cls, r):
        return cls.PI * (r ** 2)


ex_1 = Calculate(4)
print(ex_1.square_x())
ex_2 = Calculate(20)
print(ex_2.square_x())

print(Calculate.square_circle(15))

print(ex_2.random(4, 100))


