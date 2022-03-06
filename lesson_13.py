class Params:
    def __init__(self, height, width):
        self.h = height
        self.w = width

    def __getattr__(self, item):
        return f"__getattr__ {self} - {item}"

    # def __getattribute__(self, item):
    #     return f"__getattribute__ {self} - {item}"

    def __setattr__(self, key, value):
        print(f'__setattr__ {key} = {value}')
        return object.__setattr__(self, key, value)

    def __delattr__(self, item):
        print(f'__delattr__ {item}')


ex_1 = Params(100, 200)
ex_2 = Params(300, 400)
print(ex_2.__dict__)
print(ex_2.w)
print(ex_1.f)
del ex_2.h


