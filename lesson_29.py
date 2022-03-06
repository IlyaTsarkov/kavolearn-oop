class Truediv:
    def __init__(self, number):
        self.number = number

    @classmethod
    def validate(cls, other):
        if type(other) != Truediv:
            raise TypeError('Действие доступно только с экземплярами класса')

    def __truediv__(self, other):
        self.validate(other)
        return self.number / other.number

    raise ZeroDivisionError('Нельзя')


ex_1 = Truediv(50)
ex_2 = Truediv(20)
ex_3 = Truediv(0)
print(ex_1 / ex_2)
print(ex_1 / ex_3)
print(ex_1 / 100)

