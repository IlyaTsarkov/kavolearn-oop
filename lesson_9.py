class Group:
    def __init__(self, group_count):
        self.count = group_count

    def __eq__(self, other):
        ex = other.count if isinstance(other, Group) else other
        return self.count == ex

    def __lt__(self, other):
        ex = other.count if isinstance(other, Group) else other
        return self.count < ex

    def __le__(self, other):
        ex = other.count if isinstance(other, Group) else other
        return self.count <= ex


group_1 = Group(50)
group_2 = Group(40)

print(group_1 == group_2)
print(group_1 == 50)
print(group_1 != group_2)
print(group_1 > group_2)
print(group_1 < group_2)
print(group_1 <= group_2)
print(group_1 >= group_2)

