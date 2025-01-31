import random


# def give_sum(a, b):
#     '''
#     :param a: Integer
#     :param b: Integer
#     :return: None
#
#     нахождение суммы
#     '''
#     # print(a + b)
#     return a + b
#
#
# def give_minus(a, b):
#     '''
#     :param a: Integer
#     :param b: Integer
#     :return: None
#
#     нахождение разности
#     '''
#     # print(a - b)
#     return a - b
#
#
# def give_multiplicat(a, b):
#     '''
#     :param a: Integer
#     :param b: Integer
#     :return: None
#
#     нахождение произведения
#     '''
#     # print(a * b)
#     return a * b
#
#
# def give_division(a, b):
#     '''
#     :param a: Integer
#     :param b: Integer
#     :return: None
#
#     нахождение деления
#     '''
#     # print(a / b)
#     return a / b
#
#
# # num1 = random.randint(1, 100)
# # num2 = random.randint(1, 100)
# # print(num1, num2)
#
# while True:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     o = input('Введите оператор (+ - / *): ')
#
#     if o == '+':
#         print(give_sum(num1, num2))
#     elif o == '-':
#         print(give_minus(num1, num2))
#     elif o == '/':
#         if num2 == 0:
#             print('Ошибка, деление на 0')
#         else:
#             print(give_division(num1, num2))
#     elif o == '*':
#         print(give_multiplicat(num1, num2))
#     else:
#         print('Неверный ввод')
#
#     ch = input('Желаете продолжить (да/нет): ').lower()
#
#     if ch == 'нет':
#         break

def sum_arr(arr):
    print('Массив: ', arr)
    print('Сумма чисел в массиве: ', sum(arr))


def is_year_leap(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


def square(aa):
    return (4 * aa, aa ** 2, round(aa * (2 ** 0.5), 2))


def season(m):
    if m == 12 or m == 1 or m == 2:
        return 'Зима'
    elif m == 3 or m == 4 or m == 5:
        return 'Весна'
    elif m == 6 or m == 7 or m == 8:
        return 'Лето'
    elif m == 9 or m == 10 or m == 11:
        return 'Осень'
    else:
        return 'Нет такого месяца!'


def if_prime(n):
    if n == 0:
        return False
    else:
        divid = 2
        ch = 0

        while divid <= n // 2:
            if n % divid == 0:
                return False
                ch = 1
                break
            divid += 1

        if ch == 0:
            return True


def aver_arr(arr):
    return sum(arr) / len(arr)


sum_arr([random.randint(1, 50) for i in range(10)])

year = int(input('\nВведите номер года: '))

if is_year_leap(year):
    print('Год високосный')
else:
    print('Год невисокосный')

a = int(input('\nВведите сторону квадрата: '))
print(square(a))

month = int(input('\nВведите номер месяца: '))
print(season(month))

num = random.randint(1, 1000)
print('\n', num)

if num == 1:
    print('Число ни простое, ни сотавное')
elif if_prime(num):
    print('Число простое')
else:
    print('Число сотавное')

array_ = [random.randint(1, 50) for i in range(10)]
print('\n', array_)
print('Среднее арифметическое: ', aver_arr(array_))
