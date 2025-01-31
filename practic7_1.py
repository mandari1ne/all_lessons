import random
from math import pi

#################
print('ЗАДАЧА 1')
a = int(input('Введите первый катет: '))
b = int(input('Введите второй катет: '))

print('Длина гипотезы: ', (a ** 2 + b ** 2) ** (1 / 2))

#################
print('\nЗАДАЧА 2')
n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))

if n1 < n2 and n2 < n3:
    print(f'{n2} среднее число')
elif n2 < n1 and n1 < n3:
    print(f'{n1} среднее число')
else:
    print(f"{n3} среднее число")

#################
print('\nЗАДАЧА 3')
n1 = random.choice(range(1, 100, 2))
n2 = random.choice(range(2, 101, 2))

print(f'Случайные числа {n1}, {n2}')

if n1 % 2 != 0:
    print(f'{n1} нечетное число')
else:
    print(f'{n2} нечетное число')

#################
print('\nЗАДАЧА 4')
n = int(input('Введите число: '))
new_n = 0

while n > 9:
    new_n = (new_n + n % 10) * 10
    n = n // 10

print('Число в обратном порядке: ', new_n + n)

#################
print('\nЗАДАЧА 5')
while True:
    print('Выберите фигуру:')
    choice = int(input('[1] - Прямоугольник \n[2] - Треугольник \n[3] - Круг \n[0] - Выход \n'))

    if choice == 0:
        break
    elif choice == 1:
        a = int(input('Введите ширину прямоугольника: '))
        b = int(input('Введите длину прямоугольника: '))

        print('Площадь прямоуголька: ', a * b)
    elif choice == 2:
        a = int(input('Введите сторону треугольника, к которой проведена высота: '))
        h = int(input('Введите высоту треугольника: '))

        print('Площадь треугольника: ', a * h / 2)
    elif choice == 3:
        r = int(input('Введите радиус круга: '))

        print('Площадь круга: ', round(pi * r ** 2, 2))
    else:
        print('Неверный вывод')

#################
print('\nЗАДАЧА 6')
a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))

if a < b + c and b < a + c and c < a + b:
    print('Треугольник существует')
else:
    print('Треугольник не существует')

#################
print('\nЗАДАЧА 7')
x = int(input('Введите х координату точки: '))
y = int(input('Введите y координату точки: '))
r = int(input('Введите радиус круга: '))

if (x ** 2 + y ** 2) ** (1 / 2) < r:
    print('Точка принадлежит кругу')
else:
    print('Точка не принадлежит кругу')

#################
print('\nЗАДАЧА 8')
s = input('Введите вашу строку: ')
words = s.split()

print('Слов в строке: ', len(words))

#################
print('\nЗАДАЧА 9')
s = input('Введите вашу строку: ')
new_s = ''

for ch in s:
    if not ch.istitle():
        new_s += ch

print('Новая строка: ', new_s)

#################
print('\nЗАДАЧА 10')
for i in range(101):
    if i % 7 != 0:
        print(i, end=' ')
    if i % 30 == 0:
        print() #чисто ради вывода

#################
print('\n\nЗАДАЧА 11')
s = 0
for i in range(1, 101):
    s += i
print('Сумма чисел от 1 до 100: ', s)

#################
print('\nЗАДАЧА 12')
n = int(input('Введите число: '))

factor = 1
i = 1
while i <= n:
    factor *= i
    i += 1

print(f'факториал {n}: ', factor)

################# ВАЖНОООООООО
print('\nЗАДАЧА 13')
n = int(input('Введите число: '))
i = 1
row = 1

while i <= n:
    s_n = ' '.join(str(x) for x in range(i, min(i + row, n + 1)))
    print(s_n)

    i += row
    row += 1

#################
print('\nЗАДАЧА 14')
list1 = []
len_l1 = int(input('Сколько чисел в первом списке: '))
for i in range(len_l1):
    i = int(input('Введите число: '))
    list1.append(i)

list2 = []
len_l2 = int(input('Сколько чисел во втором списке: '))
for i in range(len_l2):
    i = int(input('Введите число: '))
    list2.append(i)

list3 = []
for i in list1:
    if i not in list2:
        if i not in list3:
            list3.append(i)
print('Пересечение 2х списков: ', list3)
