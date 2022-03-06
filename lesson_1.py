class Computer:
    # def __new__(cls, *args, **kwargs):
    #     print("Конструктор" + str(cls))

    def __init__(self, os, top, ram=4):
        self.operation_system = os
        self.type_of_computer = top
        self.RAM = ram
        self.color = 'black'

    def info(self):
        return f"Мой ПК - {self.type_of_computer}, {self.operation_system}, {self.RAM}"

    def computer_clor(self):
        return f"{self.color}"

    def __del__(self):
        print('Удаление экземпляра' + str(self))


ex = Computer('linux', 'desktop', 8)
ex_2 = Computer('windows', 'notebook')

print(ex.info())
print(ex_2.info())

print(ex.computer_clor())


