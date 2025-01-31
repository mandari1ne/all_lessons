def give_sum(a, b):
    return a + b

def give_min(a, b):
    return a - b

def give_mult(a, b):
    return a * b

def give_div(a, b):
    return a / b

def calculate(a, b, oper):
    if oper == '+':
        return give_sum(a, b)
    elif oper == '-':
        return give_min(a, b)
    elif oper == '*':
        return give_mult(a, b)
    elif oper == '/':
        if b == 0:
            return 'Ошибка, деление на 0!'
        else:
            return give_div(a, b)
    else:
        return 'Ошибка!'

while True:
    num1 = float(input('Введите первое число: '))
    op = input('Введите оператор: ')
    num2 = float(input('Введите второе число: '))

    print(calculate(num1, num2, op))

    check = input('Желаете продолжить (1 - да; 0 - нет): ')

    if check == '0':
        break

#############################
print('\nДОП 1')
def char_frequency(s):
    dict_ = {}

    for c in s:
        dict_[c] = s.count(c)

    return dict_

str_ = input('Введите вашу строку: ')

print('Получившийся словарь: ', char_frequency(str_))

print('\nДОП 2')

def sort_by_key(l, s):
    return sorted(l, key=lambda v: v[s])

list_ = [
    {'table': 3, 'chair': 6},
    {'table': 9, 'chair': 2},
    {'table': 1, 'chair': 1}
]
print(list_)
str_ = input(f'ВВедите название ключа {list(list_[0].keys())}, по которму хотите отсортировать: ')
print('Отсортированный словарь: ', sort_by_key(list_, str_))
