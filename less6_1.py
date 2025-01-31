print('ЗАДАЧА 1')

s = 0
for i in range(1, 101):
    s += i

print('Сумма чисел от 1 до 100: ', s)

###########
print('\nЗАДАЧА 2')

for i in range(1, 11):
    print(f'{i}^2 = {i * i};', end=' ')

###########
print('\n\nЗАДАЧА 3')

arr = []
for i in range(2, 51, 2):
    arr.append(i)

print('Четные числа от 1 до 50: ', arr)

###########
print('\nЗАДАЧА 4')

for i in range(10, 0, -1):
    print(i, end=' ')

###########
print('\n\nЗАДАЧА 5')

n = int(input('Введите ваше число: '))
factor = 1

for i in range(1, n + 1):
    factor *= i

print(f'Факториал {n}: ', factor)

###########
print('\nЗАДАЧА 6')

n = int(input('Введете число либо 0, чтобы завершить программу: '))
s = n

if n:
    while n:
        n = int(input('Введете число либо 0, чтобы завершить программу: '))
        s += n

    print('Сумма введенных чисел: ', s)
else:
    print('Вы завершили программу')

###########
print('\nЗАДАЧА 7')
n = int(input('Введите число: '))

if n == 1:
    print('Число не является ни составным, ни простым')
elif n == 0:
    print('Число составное')
else:
    divid = 2
    ch = 0

    while divid <= n // 2:
        if n % divid == 0:
            print('Число составное')
            ch = 1
            break
        divid += 1

    if ch == 0:
        print('Число простое')

###########
print('\nЗАДАЧА 8')

a, b = 0, 1

print('Последовательность чисел Фибоначчи до 100')
while b <= 100:
    print(b, end=' ')
    a, b = b, a + b

###########
print('\n\nЗАДАЧА 9')

from random import randint

n = randint(1, 100)
n1 = 0

print('Попробуйте угадать число')
while n != n1:
    n1 = int(input('Введите число: '))

    if n > n1:
        print('Загаданное число больше')
    elif n < n1:
        print('Загаданное число меньше')
    else:
        print('Вы угадали')

###########
print('\nЗАДАЧА 10')

s = input('Введите строку: ').lower()

letters = 'уеёыаоэяиюeyuioa'
count = 0
i = 0

while i < len(s):
    if s[i] in letters:
        count += 1
    i += 1

print('Кол-во гласных в строке: ', count)
