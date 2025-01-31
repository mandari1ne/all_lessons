#d = dict(short='dict', long='dictionary')
#d_2 = dict([(1, 1), (2, 4)])
#print(d, '\n', d_2)
#dict.fromkeys(...)
# word[key] = value

person = {'name': 'Марина', 'age': 19, 'city': 'Minsk'}
print(person['age'])

cars = {'BMW': ['X5 M', 'X6 M', 'X3 M50'], 'Tesla': ['Roadster', 'Cybertruck', 'Model Y']}
print(cars['BMW'][0], cars['BMW'][2], cars['Tesla'][0], cars['Tesla'][2])

dict_ = {1: 1, 2: 2, 3: 3, 4: 4}
keys = dict_.values()
p = 1
for i in keys:
    p *= i
print(p)

list1 = [1, 2, 3, 4]
list2 = ['один', 'два', 'три', 'четыре']
dict_ = dict(zip(list1, list2))
print(dict_)

s = 'pythonist'
dict_ = {lett: s.count(lett) for lett in s}
print(dict_)

###############
print('\n#################')
d = {'apple': 'яблко', 'table': 'стол', 'animal': 'животное'}
l1 = []
l2 = []

count = int(input('Сколько слов будете вводить: '))
for i in range(count):
    w = input('Введите слово на английском: ').lower()
    l1.append(w)

for i in l1:
    if i in d:
        l2.append(d[i])
    else:
        l2.append('Неизвестно')
print(l2)

print('\n#################')
d = {'Москва': 11920000, 'Санкт-Петербург': 5384000, 'Новосибирск': 1613000}
d_keys = list(d.keys())

d_values = list(d.values())
d_values.sort(reverse=True)
#print(d_keys)

new_d = {}
for k in d_keys:
    for v in d_values:
        if v == d[k]:
            new_d[k] = d[k]
            print('(', k, ': ', d[k], ')')

print(new_d)
