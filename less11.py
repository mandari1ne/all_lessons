import random
from math import pi


#
# def num_digit(n):
#     if n != 0:
#         return 1 + num_digit(n // 10)
#     else:
#         return 0
#
# num = random.randint(1, 10000)
# print(f'Разряд числа {num}: ', num_digit(num))

# def circle_square():
#     r = random.randint(1, 50)
#     print('Радиус круга', r)
#
#     return round(pi * (r ** 2), 2)
#
#
# def rectangle_square():
#     a = random.randint(1, 50)
#     b = random.randint(1, 50)
#     print('Стороны прямоугоника: ', a, b)
#
#     return a * b
#
#
# def triangle_square():
#     a = random.randint(1, 50)
#     h = random.randint(1, 15)
#     print('Высота треугольника: ', h)
#     print('Сторона треугольника: ', a)
#
#     return 0.5 * a * h
#
#
# def square(n):
#     if n == 1:
#         return circle_square()
#     elif n == 2:
#         return rectangle_square()
#     elif n == 3:
#         return triangle_square()
#     else:
#         return 'Ошибка'
#
#
# while True:
#     print('\nВыберте фигуру, площадь которой хотите найти')
#     fig = int(input('1 - круг, 2 - прямоугольник, 3 - треугольник: '))
#
#     print(square(fig))
#
#     check = int(input('Желаете продолжить (1 - да, 2 - нет): '))
#     if check == 2:
#         break

# def for_arr(b, f):
#     arr = [random.randint(b, f) for i in range(10)]
#
#     print('Получившийся массив: ', arr)
#
#
# beg = int(input('Введите начало диапазона: '))
# fin = int(input('Введите конец диапазона: '))
# for_arr(beg, fin)

# def date(sec):
#     days = sec // 86400
#     hours = sec % 86400 // 3600
#     minutes = sec % 3600 // 60
#     seconds = sec % 60
#
#     print(f'{days}:{hours}:{minutes}:{seconds}')
#
# seconds = int(input('Введите кол-во секунд: '))
# date(seconds)

def count_letters(s):
    vowels = 'уеыаоэяиюeyuioa'
    consonants = 'йцкнгшщзхфвпрлдчсмтбqwrtpsdfghjklzxcvbnm'

    сount_vow = 0
    count_cons = 0
    for c in s:
        if c in vowels:
            сount_vow += 1
        elif c in consonants:
            count_cons += 1

    print(f'гласных - {сount_vow}, согласных - {count_cons}')


str_ = input('Введите вашу строку: ').lower()
count_letters(str_)
