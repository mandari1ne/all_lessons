print('ПЕРВАЯ ЗАДАЧА')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if (num1 >= 0 and num2 >= 0) or (num1 == 0 and num2 == 0):
    print(f'Отрицательных чисел между {num1} и {num2} нет')
else:
    if num1 < num2:
        i = num1 + 1
        while i < num2 and i < 0:
            print(i)
            i += 1
    else:
        i = num2 + 1
        while i < num1 and i < 0:
            print(i)
            i += 1

print('\nВТОРАЯ ЗАДАЧА')
check = 1

while check:
    n1 = float(input('Введите первое число: '))
    n2 = float(input('Введите второе число: '))
    o = input('Введите операцию: ')

    if o == '/' and n2 == 0:
        print('Ошибка, деление на 0')
    else:
        if o == '+':
            print(f'{n1} + {n2} = {n1 + n2}')
        elif o == '-':
            print(f'{n1} - {n2} = {n1 - n2}')
        elif o == '*':
            print(f'{n1} * {n2} = {n1 * n2}')
        else:
            print(f'{n1} / {n2} = {n1 / n2}')

    ch = int(input('[1] - Желаете продолжить, [0] - Завершить: '))

    if ch == 0:
        check = 0
