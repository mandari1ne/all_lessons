from random import randint
from itertools import product

print('ЗАДАЧА 1')

list_ = [randint(1, 100) for i in range(10)]

print(list_)
print(set(list_))
print(list(sorted(set(list_))))

print('\nЗАДАЧА 2')

set1 = set(randint(1, 20) for i in range(10))
set2 = set(randint(1, 20) for i in range(10))

print(set1)
print(set2)
print(sorted(list(set1 & set2)))

print('\nЗАДАЧА 3')

list_ = [randint(1, 5) for i in range(10)]
print(list_)

new_list = []
temp_list = []
for i in list_:
    if i not in temp_list:
        temp_list.append(i)
        temp = (i, list_.count(i))
        new_list.append(temp)

print(sorted(new_list, key=lambda i: i[1], reverse=True))

print('\nЗАДАЧА 4')

list_ = [randint(1, 10) for i in range(10)]
print(list_)

num = randint(1, 20)
print(num)

set_ = set()
for i in list_:
    for j in list_:
        if i == j and list_.count(i) != 1:
            if i + j == num and (i, j) not in set_ and (j, i) not in set_:
                set_.add((i, j))
        else:
            if i + j == num and (i, j) not in set_ and (j, i) not in set_:
                set_.add((i, j))

print(set_)

print('\nЗАДАЧА 5')
list_ = ['aaa', 'trtrtr', 'trtrtr', 'rrrr', 'pppppp', 'trtrtr', 'pppppp']
print(list_)

set_ = set()
for i in list_:
    if len(i) < 5:
        list_.remove(i)
    else:
        if i not in set_:
            set_.add(i)

print('Строки с длиной больше 5: ', list_)
print('Уникальные оставшиеся строки: ', set_)

print('\nЗАДАЧА 6')
list1 = [randint(1, 10) for i in range(3)]
list2 = [randint(1, 10) for i in range(3)]
print(list1)
print(list2)

print(list(set(product(list1, list2))))

print('\nЗАДАЧА 7')
list_ = [tuple(randint(1, 100) for i in range(2)) for x in range(5)]
print(list_)

tmp_l = []
for i in list_:
    tmp_l.append(sum(i))

print(tuple(tmp_l))

print('\nЗАДАЧА 8')
list_ = [randint(1, 20) for i in range(10)]
print(list_)

new_list = []
for i in list_:
    if i not in new_list:
        new_list.append(i)

print(new_list)

print('\nЗАДАЧА 9')
list_ = ['aaa', 'trtrtr', 'trtrtr', 'rrrr', 'pppppp', 'trtrtr', 'pppppp']
print(list_)

dict_ = {}
for i in list_:
    dict_[i] = list_.count(i)

print(dict_)

print('\nЗАДАЧА 10')
list_ = ['12', '43 68', '2 3 4', '889', '5 9', '3', '11 1']
print(list_)

s = 0
for i in list_:
    for j in i.split():
        s += int(j)

print(s)
