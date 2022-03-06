class Callable:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def __call__(self, *args, **kwargs):
        print('Вызов экземпляра', self.name)
        return self.name.title()


ex_1 = Callable('first')
print(ex_1())
ex_2 = Callable('second')
print(ex_2())
