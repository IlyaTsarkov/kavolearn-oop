class Number:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, x):
        self.x = x

    def into(self):
        return f"{self.x}"


ex_1 = Number(10)
ex_2 = Number(30)
ex_3 = Number(50)
print(ex_1, ex_1.into())
print(ex_2, ex_2.into())
print(ex_3, ex_3.into())

