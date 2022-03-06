class CarPrice:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @price.deleter
    def price(self):
        del self.__price

    # price = property()
    # price = price.getter(get_price)       ==  price = property(price)
    # price = price.setter(set_price)       ==  price = price.setter(price)
    # price = price.deleter(del_price)      ==  price = price.deleter(price)


car_1 = CarPrice('audi', 300000)
print(car_1.price)
car_1.price = 400000
print(car_1.price)
del car_1.price

