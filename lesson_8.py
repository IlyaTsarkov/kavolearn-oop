class Group:
    def __init__(self, group_count):
        self.count = group_count

    def __add__(self, other):
        if isinstance(other, Group):
            return self.count + other.count
        if isinstance(other, (int, float)):
            return self.count + other

    def __mul__(self, other):
        if isinstance(other, Group):
            return self.count * other.count
        if isinstance(other, (int, float)):
            return self.count * other

    def __sub__(self, other):
        if isinstance(other, Group):
            return self.count - other.count
        if isinstance(other, (int, float)):
            return self.count - other

    def __truediv__(self, other):
        if isinstance(other, Group):
            return self.count / other.count
        if isinstance(other, (int, float)):
            return self.count / other


group_1 = Group(50)
group_2 = Group(40)
print(group_1.__add__(group_2))          # == group_1 + group_2
print(group_2.__add__(100))              # == group_2 + 100
print(group_2 + 200)                     # == group_2.__add__(200)
print(group_1.__mul__(group_2))          # == group_1 * group_2
print(group_1.__sub__(group_2))          # == group_1 - group_2
print(group_2.__sub__(group_1))          # == group_2 - group_1
print(group_2.__truediv__(group_1))      # == group_2 / group_1

