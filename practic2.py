import random, calendar, string

# Задача 1
# def bmi(h, w):
#     return w / (h ** 2)
#
# def check_bmi(b):
#     if b < 18.5:
#         print('У вас недостаточная масса тела, ИДМ = ', round(b, 2))
#     elif b >= 18.5 and b <= 24.9:
#         print('У вас нормальная масса тела, ИДМ = ', round(b, 2))
#     elif b >= 25.0 and b <= 29.9:
#         print('У вас избыточная масса тела, ИДМ = ', round(b, 2))
#     elif b >= 30 and b <= 34.9:
#         print('У вас ожирение I, ИДМ = ', round(b, 2))
#     elif b >= 35 and b <= 39.9:
#         print('У вас ожирение II, ИДМ = ', round(b, 2))
#     else:
#         print('У вас ожирение III, ИДМ = ', round(b, 2))
#
#
# height = float(input('Введите ваш рост в см: '))
# weight = float(input('Введите ваш вес: '))
#
# check_bmi(bmi(height / 100, weight))

#Задача 2
# def check_fig(aa):
#     if a == 3:
#         return 'треуголник'
#     elif a == 4:
#         return 'четырехуголник'
#     elif a == 5:
#         return 'пятиуголник'
#     elif a == 6:
#         return 'шестиуголник'
#     elif a == 7:
#         return 'семиуголник'
#     elif a == 8:
#         return 'восьмиуголник'
#     elif a == 9:
#         return 'девятиуголник'
#     elif a == 10:
#         return 'десятиуголник'
#     else:
#         return 'неверный ввод!'
#
# a = int(input('Введите кол-во сторон у фигуры: '))
# print('Это ', check_fig(a))

#Задача 3
# def next_date(d, m, y):
#     if ((d < 0 or y < 0) or (d > 28 and m == '02' or m == 'февраля' or m == 'февраль' and not calendar.isleap(y)) or
#             (d > 29 and m == '02' or m == 'февраля' or m == 'февраль' and calendar.isleap(y)) or
#             (d > 30 and (m == '04' or m == 'апреля' or m == 'апрель' or m == '06' or m == 'июня' or m == 'июнь' or
#              m == '09' or m == 'сентября' or m == 'сентябрь' or m == '11' or m == 'ноября' or m == 'ноябрь')) or
#             (d > 31 and (m == '01' or m == 'января' or m == 'январь' or m == '05' or m == 'марта' or m == 'март' or
#             m == '05' or m == 'мая' or m == 'май' or m == '07' or m == 'июля' or m == 'июль' or
#                          m == '08' or m == 'августа' or m == 'август' or m == '10' or m == 'октября' or m == 'октябрь' or
#             m == '12' or m == 'декабря' or m == 'декабря'))):
#         print('Неверный ввод!')
#         #return
#     ###################################
#     elif d == 30 and (m == '04' or m == 'апреля' or m == 'апрель'):
#         if m == 'апреля' or m == 'апрель':
#             print(f'1 мая {year} года')
#         else:
#             print(f'1.05.{year}')
#     elif d == 30 and (m == '06' or m == 'июня' or m == 'июнь'):
#         if m == 'июня' or m == 'июнь':
#             print(f'1 июля {year} года')
#         else:
#             print(f'1.06.{year}')
#     elif d == 30 and (m == '09' or m == 'сентября' or m == 'сентябрь'):
#         if m == 'сентября' or m == 'сентябрь':
#             print(f'1 октября {year} года')
#         else:
#             print(f'1.10.{year}')
#     elif d == 30 and (m == '11' or m == 'ноября' or m == 'ноябрь'):
#         if m == 'ноября' or m == 'ноябрь':
#             print(f'1 декабря {year} года')
#         else:
#             print(f'1.12.{year}')
#     #######################
#     elif d == 31 and (m == '01' or m == 'января' or m == 'январь'):
#         if m == 'января' or m == 'январь':
#             print(f'1 февраля {year} года')
#         else:
#             print(f'1.02.{year}')
#     elif d == 31 and (m == '05' or m == 'марта' or m == 'март'):
#         if m == 'марта' or m == 'март':
#             print(f'1 апреля {year} года')
#         else:
#             print(f'1.04.{year}')
#     elif d == 31 and (m == '05' or m == 'мая' or m == 'май'):
#         if m == 'мая' or m == 'май':
#             print(f'1 июня {year} года')
#         else:
#             print(f'1.06.{year}')
#     elif d == 31 and (m == '07' or m == 'июля' or m == 'июль'):
#         if m == 'июля' or m == 'июль':
#             print(f'1 августа {year} года')
#         else:
#             print(f'1.08.{year}')
#     elif d == 31 and (m == '08' or m == 'августа' or m == 'август'):
#         if m == 'августа' or m == 'август':
#             print(f'1 сентября {year} года')
#         else:
#             print(f'1.09.{year}')
#     elif d == 31 and (m == '10' or m == 'октября' or m == 'октябрь'):
#         if m == 'октября' or m == 'октябрь':
#             print(f'1 ноября {year} года')
#         else:
#             print(f'1.11.{year}')
#     elif d == 31 and (m == '12' or m == 'декабря' or m == 'декабря'):
#         if m == 'декабря' or m == 'декабря':
#             print(f'1 января {year + 1} года')
#         else:
#             print(f'1.01.{year + 1}')
#     ####################################
#     elif d == 29 and (m == '02' or m == 'февраля' or m == 'февраль'):
#         if m == 'февраля' or m == 'февраль':
#             print(f'1 марта {year} года')
#         else:
#             print(f'1.03.{year}')
#     elif d == 28 and (m == '02' or m == 'февраля' or m == 'февраль') and calendar.isleap(y):
#         if m == 'февраля' or m == 'февраль':
#             print(f'29 февраля {year} года')
#         else:
#             print(f'29.02{year}')
#     elif d == 28 and (m == '02' or m == 'февраля' or m == 'февраль') and not calendar.isleap(y):
#         if m == 'февраля' or m == 'февраль':
#             print(f'1 марта {year} года')
#         else:
#             print(f'1.03.{year}')
#     ###################################
#     else:
#         if not m.isnumeric():
#             new_m = m[:-1] + 'я'
#             print(f'{d + 1} {new_m} {y}')
#         else:
#             print(f'{d + 1}.{m}.{y}')
#
# day = int(input('Введите день: '))
# month = input('Введите месяц: ').lower()
# year = int(input('Введите год: '))
#
# next_date(day, month, year)

#Задача 4
# def coutn_tov(c):
#     return round(10.95 + (c - 1) * 2.95, 2)
#
# colvo = int(input('Введите кол-во позиций в заказе: '))
# print('Сумма вашей доставки: ', coutn_tov(colvo))

#Задача 5
# def new_fraction(n, d):
#     n1 = n
#     d1 = d
#     while n1 != d1:
#         if n1 > d1: #неправильная дробь
#             n1 -= d1
#         else:
#             d1 -= n1
#     return n // n1, d // d1
#
# numer = int(input('Введите числитель: '))
# denom = int(input('Введите знаменатель: '))
#
# tmp = new_fraction(numer, denom)
# print(f'Новая дробь: {tmp[0]}/{tmp[1]}')

#Задача 6
# def for_list(l):
#     print('Перевернутый список: ', l[::-1])
#     tmp1 = [n for n in l if str(n).isnumeric()]
#     tmp2 = [n for n in l if str(n).isalpha()]
#     print('Список в порядке убывания: ', sorted(tmp1, reverse=True) + sorted(tmp2, reverse=True))
#     print('Список в порядке возрастания: ', sorted(tmp1) + sorted(tmp2))
#     print('От 2 до 7 элемента: ', l[2:8])
#     l.pop(5)
#     print('Без 5 элемента: ', l)
#     new_list = list(set(l))
#     print('Список без дубликатов: ', new_list)
#
# words = []
# for i in range(20):
#     word = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 5)))
#     words.append(word)
# list_ = [random.choice(words + [random.randint(0, 9) for _ in range(10)]) for _ in range(random.randint(10, 15))]
# print(list_)
# for_list(list_)

#Задача 7
# def countRange(l, minim, maxim):
#     tmp = [i for i in l if i >= minim and i < maxim]
#     return len(tmp)
#
# list1 = [
#     random.randint(0, 50) if random.choice([True, False]) else round(random.uniform(0, 50), 2)
#     for _ in range(10)
# ]
# min1 = random.randint(0, 25)
# max1 = random.randint(25, 50)
#
# print('Список1: ', list1)
# print('Первая нижняя граница: ', min1)
# print('Первая верняя граница: ', max1)
# print('Результат: ', countRange(list1, min1, max1), end='\n' * 2)
#
# list2 = [
#     random.randint(0, 50) if random.choice([True, False]) else round(random.uniform(0, 50), 2)
#     for _ in range(10)
# ]
# min2 = random.randint(0, 12)
# max2 = random.randint(13, 50)
#
# print('Список2: ', list2)
# print('Первая нижняя граница: ', min2)
# print('Первая верняя граница: ', max2)
# print('Результат: ', countRange(list2, min2, max2), end='\n' * 2)
#
# list3 = [
#     random.randint(0, 50) if random.choice([True, False]) else round(random.uniform(0, 50), 2)
#     for _ in range(10)
# ]
# min3 = random.randint(0, 2)
# max3 = random.randint(5, 10)
#
# print('Список1: ', list3)
# print('Первая нижняя граница: ', min3)
# print('Первая верняя граница: ', max3)
# print('Результат: ', countRange(list3, min3, max3))

# Задача 8
# def check_list(l):
#     count = 0
#     for i in l:
#         if isinstance(i, list):
#             count += 1
#             count += check_list(i)
#     return count
#
# list_ = [[1, [2, [4, 8]]], [3], 6]
# print(list_)
# print('Кол-во подписчиков: ', check_list(list_))

#Задача 9
# def check_words(w1, w2):
#     return w1 == w2[::-1]
#
# word1 = input('Введите первое слово: ').lower()
# word2 = input('Введите второе слово: ').lower()
# print('Слова анаграммы' if check_words(word1, word2) else 'Слова не анаграммы')

#Задача 10
def conver_str(s, d):
    num_str = ''

    for i in s:
        num_str += d[i] + ' '

    return num_str

dict_ = {'.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
         'a': '2', 'b': '22', 'c': '222',
         'd': '3', 'e': '33', 'f': '333',
         'g': '4', 'h': '44', 'i': '444',
         'j': '5', 'k': '55', 'l': '555',
         'm': '6', 'n': '66', 'o': '666',
         'p': '7', 'q': '77', 'r': '777', 's': '7777',
         't': '8', 'u': '88', 'v': '888',
         'w': '9', 'x': '99', 'y': '999', 'z': '9999',
         ' ': '0'}

str_ = input('Enter your string in english: ').lower()
print(conver_str(str_, dict_))
