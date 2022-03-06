print(10 + 30)
try:
    print(1 * 'b')
    try:
        lst = [1, 2, 3, 4]
        print(lst[5])
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
else:
    print('Вызов блока else')
finally:
    print('Вызов блока finally')
print('a' + 'b')

