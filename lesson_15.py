class Languages:
    def __init__(self, *args):
        self.l_list = list(args)
        self.index = 0

    def __next__(self):
        item = self.l_list[self.index]
        self.index += 1
        return item


ex_l = Languages('Python', 'Java', 'C++', 'JavaScript', 'PHP', 'Ruby')
print(ex_l.__next__())
print(ex_l.__next__())
print(ex_l.__next__())
print(ex_l.__next__())
print(ex_l.__next__())
print(ex_l.__next__())

