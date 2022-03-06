class DollarInRuble:
    def __init__(self, count, course=83):
        self.count = count
        self.course = course

    def currency_in_rouble(self):
        return self.count * self.course


class EuroUnRuble:
    def __init__(self, count, course=93):
        self.count = count
        self.course = course

    def currency_in_rouble(self):
        return self.count * self.course


ex_d_1 = DollarInRuble(70)
ex_d_2 = DollarInRuble(500)
ex_e_1 = EuroUnRuble(400)
ex_e_2 = EuroUnRuble(200)
print(ex_d_1.currency_in_rouble(), ex_d_2.currency_in_rouble())
print(ex_e_1.currency_in_rouble(), ex_e_2.currency_in_rouble(), '\n')

investors = [ex_d_1, ex_d_2, ex_e_1, ex_e_2]
for i in investors:
    print(i.currency_in_rouble())

