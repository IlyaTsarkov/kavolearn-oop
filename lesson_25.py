class Employee:
    __slots__ = ('name', 'age', 'post')

    def __init__(self, name, age, post):
        self.name = name
        self.age = age
        self.post = post


class NewWorker(Employee):
    __slots__ = ()

    def info(self):
        return f"{self.name}, {self.age}, {self.post}"


ex_1 = NewWorker('Vanya', 25, 'junior_developer')
# ex_1.lastname = 'Ivanov'
print(ex_1.info())
# print(ex_1.__dict__)

