class BankCard:
    def __init__(self, card_id, cvv, name='Ivan Ivanov', end_date='24.05.2025'):
        self._id = card_id
        self._cvv = cvv
        self.name = name
        self.end_date = end_date

    def card_info(self):
        return f"Card {self._id} owner: {self.name}, end {self.end_date}, cvv {self._cvv}"

    def _private_info(self):
        return f"id {self._id}, cvv {self._cvv}"

    def see_private_info(self):
        print(self._private_info())


card_1 = BankCard('4200 3800 5000 4000', 200)
card_2 = BankCard('4200 5800 3000 2000', 250)

card_2.see_private_info()
