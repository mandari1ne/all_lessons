print('ЗАДАЧА 1')
n = int(input('Введите число: '))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f'Сумма чисел от 1 до {n}: ', sum)

print('\nЗАДАЧА 2')
n = int(input('Введите число: '))

factor = 1
i = 1
while i <= n:
    factor *= i
    i += 1

print(f'факториал {n}: ', factor)

print('\nЗАДАЧА 3')
n = int(input('Введите число: '))

while n > 0:
    print(n, end=' ')
    n -= 1

print('\n\nЗАДАЧА 4')
n = int(input('Введите число: '))

if n == 1:
    print('Число не является ни составным, ни простым')
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

print('\nЗАДАЧА 5')
n = int(input("Введите количество чисел Фибоначчи для вывода: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1

print('\n\nЗАДАЧА 6')
n = int(input('Введите число: '))

sum = 0
while n > 0:
    n1 = n % 10
    sum += n1
    n = n // 10

print('Сумма цифр числа: ', sum)

print('\nЗАДАЧА 7')
s = input('Введите строку: ')

print('Строка в обратном порядке: ', s[::-1])

print('\nЗАДАЧА 8')
n = int(input('Введите число: '))

if n == 0:
    print('Одна цифра')
else:
    count = 0
    while n > 0:
        count += 1
        n = n // 10

    print('Цифр в числе: ', count)

print('\nЗАДАЧА 9')
s = input('Введите строку: ')
s = s.replace(' ', '').lower()
is_palindrome = s == s[::-1]

if is_palindrome:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")

print('\nЗАДАЧА 10')
count = int(input('Сколько чисел хотите ввести: '))
n = int(input('Введите число: '))
max = n

i = 2
while i <= count:
    n = int(input('Введите число: '))
    if n > max:
        max = n
    i += 1

print('Макисмальное число: ', max)

print('\nЗАДАЧА 11')
count = int(input('Сколько чисел хотите ввести: '))
n = int(input('Введите число: '))
min = n

i = 2
while i <= count:
    n = int(input('Введите число: '))
    if n < min:
        min = n
    i += 1

print('Минимальнок число: ', min)

print('\nЗАДАЧА 12')
n = int(input('Введите число: '))
nn = n

sum = 0
while n != 0:
    if n % 2 == 0:
        sum += n
    n -= 1

print(f'Сумма четных чисел от 1 до {nn}: ', sum)

print('\nЗАДАЧА 13')
n = int(input('Введите число: '))
nn = n

sum = 0
while n != 0:
    if n % 2 != 0:
        sum += n
    n -= 1

print(f'Сумма нечетных чисел от 1 до {nn}: ', sum)

print('\nЗАДАЧА 14')
n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))

if n1 % n2 == 0:
    print(f'{n1} делится на {n2} без остатка')
else:
    print(f'{n1} не делится на {n2} без остатка')

print('\nЗАДАЧА 15')
n = int(input('Введите первое число: '))

divid = 1
count = 1

while divid <= n:
    if n % divid == 0:
        print(divid, end=' ')
        count += 1
    divid += 1
