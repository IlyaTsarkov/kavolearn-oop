while True:
    try:
        a, b = map(int, input('Введите два числа: ').split())
        action = input('Что сделать с числами, разделить или умножить? ')
        if action.lower() == 'разделить':
            print(a / b)
        elif action.lower() == 'умножить':
            print(a * b)
        else:
            print('Напишите разделить или умножить')
    except Exception as e:
        print(e)



