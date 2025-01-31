a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

res1 = a > b
res2 = a == b

if res1:
    print('Первое число больше')
elif res2:
    print('Числа равны')
else:
    print('Второе число больше')

a1 = int(input('\nВведите первую сторону треугольника: '))
a2 = int(input('Введите вторую сторону треугольника: '))
a3 = int(input('Введите третью сторону треугольника: '))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Треугольник существует')
else:
    print('Треугольник не существует')

num1 = float(input('\nВведите первое число: '))
oper = input('Введите операцию: ')
num2 = float(input('Введите второе число: '))

if oper == '+':
    print('num1 + num2 = ', num1 + num2)
elif oper == '-':
    print('num1 - num2 = ', num1 - num2)
elif oper == '*':
    print('num1 * num2 = ', num1 * num2)
else:
    print('num1 / num2 = ', num1 // num2)

s = input('\nВведите строку: ')

is_mister = s == 'Mister'

if is_mister:
    print('Строка является словом Mister')
else:
    print('Строка не является словом Mister')

armor_color = input('\nВведите цвет доспехов (red, yellow, black): ')
shield_color = input('Введите цвет щита (red, yellow, black): ')

if armor_color != 'red' and shield_color == 'black':
    print(True)
else:
    print(False)
