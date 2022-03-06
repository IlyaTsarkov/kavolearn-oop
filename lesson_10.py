class Group:
    def __init__(self, group_count):
        self.count = group_count

    def __eq__(self, other):
        return self.count == other.count

    def __hash__(self):
        return hash(self.count)


class ForHash:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))


group_1 = Group(50)
group_2 = Group(50)

print(group_1 == group_2)

print(hash(group_1))
print(hash(group_2))

ex_1 = ForHash(5, 10)
ex_2 = ForHash(5, 10)

print(ex_1 == ex_2)

print(hash(ex_1))
print(hash(ex_2))

