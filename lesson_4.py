class Table:
    __shared_attrs = {
        'width': 1000,
        'height': 500,
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs

