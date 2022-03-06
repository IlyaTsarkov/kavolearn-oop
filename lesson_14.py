class Languages:
    def __init__(self, *args):
        self.l_list = list(args)

    def __getitem__(self, item):
        return self.l_list[item]

    def __setitem__(self, key, value):
        self.l_list[key] = value

    def __delitem__(self, key):
        del self.l_list[key]


ex_l = Languages('Python', 'Java', 'C++', 'JavaScript', 'PHP')
print(ex_l[2])
ex_l[2] = 'C#'
print(ex_l[2])
del ex_l[2]
print(ex_l[2])

