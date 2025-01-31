from random import randint
#
# t1 = tuple(randint(0, 5) for i in range(10))
# t2 = tuple(randint(-5, 0) for i in range(10))
# t3 = t1 + t2
#
# print(t1)
# print(t2)
# print(t3)
# print(f'Кол-во нулей: {t3.count(0)}')

# #t = ('awake', 'tuple', 'pilot')
# t = tuple(str(randint(0, 5)) for i in range(10))
#
# print(', '.join(t))

# a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
#
# if sum(a) > sum(b):
#     print('Сумма больше в кортеже а')
# elif sum(a) < sum(b):
#     print('Сумма больше в кортеже b')
# else:
#     print('Суммы равны')
#
# print('Номер минимального в кортеже а: ', a.index(min(a)) + 1)
# print('Номер минимального в кортеже b: ', b.index(min(b)) + 1)

#l = list(randint(0, 10) for i in range(10))
#print(l)

#if len(l) == len(set(l)):
#    print('Дубликатов нет')
#else:
#    print('Дубликаты есть')

s1 = set(randint(0, 10) for i in range(10))
s2 = frozenset(randint(0, 10) for i in range(10))

print('Множество: ', s1)
print('Неизменяемое множество: ', s2)

print('Объединение: ', s1.union(s2))
print('Пересечение: ', s1 & s2)
