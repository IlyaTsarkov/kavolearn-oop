class Employee:
    def __init__(self, name, age, post):
        super().__init__()
        self.name = name
        self.age = age
        self.post = post

    def info(self):
        return f"employee {self.name}, age {self.age}, on post {self.post}"


class Control:
    sequence = 0

    def __init__(self):
        Control.sequence += 1
        self.seq = self.sequence


class NewWorker(Employee, Control):

    def about(self):
        return f"{self.name} with id {self.seq}"


employee_1 = NewWorker('Vanya', 25, 'junior_developer')
employee_2 = NewWorker('Petya', 27, 'middle_developer')
print(employee_1.info())
print(employee_2.info())
print(employee_1.about())
print(employee_2.about())

print(NewWorker.__mro__)

