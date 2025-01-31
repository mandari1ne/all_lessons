# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 0
#
# print(k)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Такого ключа нет')
#
# my_list = [1, 2, 3, 4, 5]
#
# try:
#     my_list[6]
# except IndexError:
#     print('Этого идекса нет в списке')

# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = my_dict['a']
# except (IndexError, KeyError):
#     print('Произошла ошибка IndexError или KeyError')
# else:
#     print('Ошибок не произошло!') #сработает, когда нету ошибок
# finally:
#     print('Оператор finally выполнен!') #сработает всегда

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# try:
#     divid = num1 / num2
# except ZeroDivisionError:
#     print('Ошибка, деление на 0!')
# else:
#     print(round(divid ** 2, 2))
# finally:
#     print('Конец!')

import random

#1
# while True:
#     try:
#         n = input('Введите число: ')
#         n = int(n)
#     except ValueError:
#         print('Ошбика, введите число', end='\n' * 2)
#     else:
#         print(f'Все прошло успешно, {n} = {type(n)}')
#         break

#2
# def check_list(l, i):
#     try:
#         return l[i]
#     except IndexError:
#         return 'Такого индекса нет'
#
# list_ = [random.randint(1, 50) for _ in range(random.randint(3, 10))]
# print('Список: ', list_)
# index_ = int(input('Введите индекс: '))
#
# print(check_list(list_, index_))

#3
# try:
#     with open('adn.txt', 'r') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('Такого файла не существует')

#4
# def is_adult(a):
#     if a < 18:
#         return False
#     else:
#         return True
#
# while True:
#     try:
#         age = int(input('Введите ваш возраст: '))
#
#         if is_adult(age):
#             print('Вы можете голосовать')
#         else:
#             print('Вам не можете голосовать')
#     except ValueError:
#         print('Некорректный ввод', end='\n' * 2)
#     else:
#         break

#5
# with open('less14.txt', 'r') as f:
#     file = f.read().split(' ')
#     print('Данные в файле: ', file)
#
#     s = 0
#     for i in file:
#         try:
#             s += int(i)
#         except ValueError:
#             print(f'Элемент файла {i} является строкой')
#     print('Сумма чисел в файле: ', s)

#6
# n = random.randint(-20, 10)
# print('Число: ', n)
#
# try:
#     if n < 0:
#         raise ValueError
#
#     print(f'Корень числа {n}: ', n ** 0.5)
# except ValueError:
#     print(f'Число {n} отрицательное')

#7
# def check_dict(d, k):
#     return d[k]
#
# dict_ = {i: i ** 2 for i in range(5)}
# print(dict_)
# key = random.randint(0, 10)
# print('Ключ: ', key)
#
# try:
#     print(f'Значение по ключу {key}: ', check_dict(dict_, key))
# except KeyError:
#     print('Такого ключа в словаре нет')

#8
# def is_divid(n1, n2):
#     if n1 % n2 == 0:
#         return True
#     else:
#         return False
#
# num1 = random.randint(0, 20)
# print(num1)
# num2 = 0
# print(num2)
#
# try:
#     if is_divid(num1, num2):
#         print(f'Число {num1} делиться на число {num2}')
#     else:
#         print(f'Число {num1} не делиться на число {num2}')
# except ZeroDivisionError:
#     print('Ошибка, деление на 0!')

#9
# def is_email(e):
#     if e.endswith('@gmail.com') or e.endswith('@mail.ru') or e.endswith('@yandex.by'):
#         return True
#     else:
#         raise TypeError
#
# email_ = input('Введите вашу почту: ')
#
# try:
#     if is_email(email_):
#         print('Корректно')
#
# except TypeError:
#     print('Некорректный ввод')

#10
# list_ = ['jfk', 89, 'jhf', 'wkfk', 10]
#
# try:
#     print('Сумма элементов списка: ', sum(list_))
# except TypeError:
#     print('Некорректные данные в списке')

#11
# def inter_set(s1, s2):
#     return s1 & s2
#
# set1 = {random.randint(0, 10) for _ in range(10)}
# print(set1)
#
# set2 = [random.randint(0, 10) for _ in range(10)]
# print(set2)
#
# try:
#     print(inter_set(set1, set2))
# except TypeError:
#     print('В функцию переданы не множества')

#12
# with open('less14.txt', 'r') as f:
#     try:
#         f.write('qqq')
#     except Exception:
#         print('Файл открыт не в том режиме')

#13
# def change_val(v, c):
#     if c == 0:
#         raise ValueError
#
#     return v * c
#
# val = round(random.uniform(5, 50), 2)
# print('Валюта: ', val)
# course = 0
# print('Курс: ', course)
#
# try:
#     print('По курсу: ', change_val(val, course))
# except ValueError:
#     print('Курс не может быть 0')

#14
# a = 1
# b = 'nd'
#
# try:
#     print(f'Тип переменной {a}: ', type(a))
#     print(f'Тип переменной {b}: ', type(b))
#     print(f'Тип переменной {c}: ', type(c))
# except NameError:
#     print('Тип переменной не определен')

#15
# def sort_list(l):
#     print(sorted(l))
#
# list_ = [1, 7, 9, 'wg', 0]
#
# try:
#     sort_list(list_)
# except TypeError:
#     print('В списке не только числа')

#16
# n = input('Введите значение: ')
#
# try:
#     print(f'Квадрат числа: ', int(n) ** 2)
# except ValueError:
#     print('Введенное зачение числом не является')

#17
# def check_tuple(t, i):
#     return t[i]
#
# tuple_ = tuple(random.randint(1, 50) for _ in range(10))
# print('Кортеж: ', tuple_)
# index_ = random.randint(5, 50)
# print('Индекс: ', index_)
#
# try:
#     print(f'Число по индексу {index_}: ', check_tuple(tuple_, index_))
# except IndexError:
#     print('Такого индекса в кортеже нет')

#18
try:
    import jash
except ModuleNotFoundError:
    print('Данной библиотеки не существует')
