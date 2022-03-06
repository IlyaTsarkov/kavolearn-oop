class Dollar:
    def __init__(self, dollar, dollar_course=77):
        self.__dol = dollar
        self.__dol_course = dollar_course
        self.__my_balance = None

    @property
    def dol(self):
        return self.__dol

    @dol.setter
    def dol(self, value):
        self.__dol = value
        self.__my_balance = None

    @property
    def my_rub_balance(self):
        if self.__my_balance is None:
            self.__my_balance = self.__dol * self.__dol_course
        return self.__my_balance


vasya = Dollar(300)
print(vasya.my_rub_balance)
vasya.dol = 500
print(vasya.my_rub_balance)


