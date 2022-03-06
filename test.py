class Descriptor:
    @classmethod
    def is_true(cls, other):
        if type(other) != (int, float):
            return f"не подходит"

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.is_true(value)
        instance.__dict__[self.name] = value


class Group:
    count_1 = Descriptor()
    count_2 = Descriptor()
    count_3 = Descriptor()
    count_4 = Descriptor()
    count_5 = Descriptor()

    def __init__(self, group_count_1, group_count_2, group_count_3,
                 group_count_4, group_count_5):
        self.count_1 = group_count_1
        self.count_2 = group_count_2
        self.count_3 = group_count_3
        self.count_4 = group_count_4
        self.count_5 = group_count_5


group_1 = Group(10, 20, 30, 40, 50)
print(group_1.__dict__)
group_1.count_1 = 30
print(group_1.__dict__)
print(group_1.count_1)