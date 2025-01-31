while True:
    try:
        num = input('Введите 2 числа: ').split(' ')
        num = [float(i) for i in num]

        try:
            if len(num) > 2:
                raise IndexError

            print(f'{num[0]} / {num[1]} = {round(num[0] / num[1], 2)}')

        except ZeroDivisionError:
            print('Ошибка! Деление на 0!', end='\n' * 2)
        except IndexError:
            print('Ошибка ввода! Введено не 2 числа', end='\n' * 2)
        else:
            break
    except ValueError:
        print('Ошибка ввода!', end='\n' * 2)
