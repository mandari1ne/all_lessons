import random
import string

def check_func(structure_):
    if isinstance(structure_, tuple):
        dict_ = {ch: len(ch) for ch in structure_}
        print('Длина слов: ', dict_)
    elif isinstance(structure_, list):
        tmp1 = [ch for ch in structure_ if ch.isalpha()]
        tmp2 = [ch for ch in structure_ if ch.isnumeric()]
        print('Кол-во букв: ', len(tmp1))
        print('Кол-во чисел: ', len(tmp2))
    elif isinstance(structure_, int):
        tmp = [ch for ch in str(structure_) if int(ch) % 2 != 0]
        print('Кол-во нечетных цифры: ', len(tmp))
    else:
        tmp = [ch for ch in structure_ if ch.isalpha()]
        print('Кол-во букв: ', len(tmp))
def gen_structure(s):
    if s == 1:
        words = []
        for i in range(20):
            word = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 15)))
            #words.append(word)
        print(words)
        tuple_ = tuple(random.choice(words) for _ in range(random.randint(3, 5)))
        print('Кортеж: ', tuple_)
        check_func(tuple_)
    elif s == 2:
        list_ = [random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 15))]
        print('Список: ', list_)
        check_func(list_)
    elif s == 3:
        num = random.randint(1, 10000)
        print('Число: ', num)
        check_func(num)
    else:
        str_ = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 50)))
        print('Строка: ', str_)
        check_func(str_)

structure = random.randint(1, 4)
gen_structure(structure)

## ДОПЫ

# def reverse_str(s):
#     if s != '':
#         return s[len(s) - 1] + reverse_str(s[:len(s) - 1])
#     else:
#         return ''
#
#
# all_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
# str_ = ''.join(random.choice(all_symbols) for _ in range(random.randint(3, 10)))
# print(str_)
# print('Строка в обратном порядке: ', reverse_str(str_))


# def reverse_list(l):
#     if l != []:
#         return [l[len(l) - 1]] + reverse_list(l[:len(l) - 1])
#     else:
#         return []
#
#
# list_ = [random.randint(1, 50) for _ in range(random.randint(3, 15))]
# print(list_)
# print('Список в обратном порядке: ', reverse_list(list_))


# def sum_num(n):
#     if n != 0:
#         return n % 10 + sum_num(n // 10)
#     else:
#         return 0
#
#
# num = random.randint(1, 10000)
# print(f'Сумма цифр числа {num}: ', sum_num(num))
