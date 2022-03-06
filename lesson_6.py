class Language:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Экземпляр класса Language"
    #
    # def __str__(self):
    #     return f"Я выбрал язык - {self.name}"


ex_1 = Language('Python')
print(ex_1)
