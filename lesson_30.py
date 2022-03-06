dm = 10
km = 0.001


def how_many_cm(m, cm=100):
    return f"{m * cm} centimetres"


def how_many_other(m, measure_of_length):
    if measure_of_length == 'dm':
        return f"{m * dm} decimetres"
    elif measure_of_length == 'km':
        return f"{m * km} kilometers"
    else:
        return f"Выберете дециметры или километры"


def main():
    print(how_many_cm(50))

    print(how_many_other(100, 'dm'))
    print(how_many_other(100, 'km'))

    print(__name__)


if __name__ == '__main__':
    main()
