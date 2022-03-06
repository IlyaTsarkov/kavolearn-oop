class PC:
    def __init__(self, oc, ram, color):
        self.oc = oc
        self.RAM = ram
        self.color = color

    @staticmethod
    def some_def():
        print('Вызов метода родительского класса')


class Computer(PC):

    def __init__(self, oc, ram, color, operating_time=3):
        super().__init__(oc, ram, color)
        super().some_def()
        self.ot = operating_time

    def about(self):
        return f"Computer {self.oc}, {self.RAM}, {self.color}, {self.ot}"


class Laptop(PC):

    def __init__(self, oc, ram, color, price=70000):
        super().__init__(oc, ram, color)
        self.price = price

    def about(self):
        return f"Laptop {self.oc}, {self.RAM}, {self.color}, {self.price}"


ex_computer = Computer('linux', 8, 'black')
ex_laptop = Laptop('linux', 8, 'white')
print(ex_computer.about())
print(ex_laptop.about())

