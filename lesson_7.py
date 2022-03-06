class LenWord:
    def __init__(self, word):
        self.word = word

    def __len__(self):
        return len(self.word)


class SegmentLen:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __abs__(self):
        return abs(self.b - self.a)


ex_word = LenWord('slovo')
print(ex_word.__len__())

ex_len = SegmentLen(10, 50)
print(ex_len.__abs__())


