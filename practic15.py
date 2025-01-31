import random, string

### 1
# temp_c = float(input('Enter temperature in Celsius: '))
# print('Temperature in Fahrenheit is:', temp_c * 1.8 + 32)
# print('Temperature in Kelvin is:', temp_c + 273.15)

### 2
# def func(s, w1, w2):
#   s = s.replace(w1, w2)
#   return s
#
# str_ = 'wertywercvhtywer'
# print('Your string: ', str_)
# print('Your new string: ', func(str_, 'wer', 'zzzzzzz'))

### 3
# def func(n):
#     list_ = [x for x in range(1, n) if x % 2 == 0]
#     print('Your list: ', list_)
#
# num = random.randint(1, 10)
# print('Count: ', num)
# func(num)

### 4
# str_ = input("Enter your string: ").lower()
# list_str = str_.split(' ')
#
# new_list = sorted(list_str, key=len)
# print('Sorted list of words: ', new_list)

### 5
# def convert_str(s):
#     ss = ''
#     for i in s:
#         if i not in ss:
#             ss += i + str(s.count(i))
#
#     return ss
#
# str_ = 'aaaffjffjkkla'
# print('Your string: ', str_)
# print('Your new string: ', convert_str(str_))

### 6
# def func(l):
#     d = {i: l.count(i) for i in l}
#
#     return d
#
# list_ = ['blabla', 'red', 'purple', 'red', 'bad', 'blabla', 'red', 'red', 'red']
# print('Your list:', list_)
# print('Your dict: ', func(list_))

### 7
# def func(l1, l2):
#     new_l = [x for x in l1 if x in l2]
#     for i in new_l:
#         if new_l.count(i) > 1:
#             new_l.remove(i)
#     return new_l
#
# list1 = [1, 4, 5, 1, 7, 9, 0, 4, 5]
# print('Your first list:', list1)
# list2 = [1, 0, 9, 1]
# print('Your second list: ', list2)
# print('Your new list: ', func(list1, list2))

### 8
# def func(l):
#     max_product = max((x * y for x in l for y in l if x != y), default=0)
#     return max_product
#
# l = [4, 4, 2, 4, 1]
# print('Your list: ', l)
# print('Max product: ', func(l))

### 9
# def func(s):
#     list_ = []
#     for i in s:
#         if i == '(':
#             list_.append(i)
#         elif i == ')':
#             if not list_:
#                 return False
#             list_.pop()
#
#     return len(list_) == 0
#
# s1 = '(())()'
# s2 = '(((())('
#
# if func(s1):
#     print('In first string everything is correct')
# else:
#     print('In first string everything is not correct')
#
# if func(s2):
#     print('In second string everything is correct')
# else:
#     print('In second string everything is not correct')

### 10
# def func(l):
#     new_l = []
#     new_l.append(l[-1])
#     return new_l + l[:-1]
#
# list_ = [1, 2, 3, 4, 5]
# print('Your list: ', list_)
# print('Your new list: ', func(list_))

### 11
# len_ = int(input('Enter the length of password: '))
# password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(len_))
# print('Your password: ', password)

### 12
# def func(s):
#     list_s = s.lower().split(' ')
#
#     d = {i: list_s.count(i) for i in list_s}
#
#     return d
#
# str_ = 'blabla Red purple red bad blabla Red red red'
# print('Your string:', str_)
# print('Your dict: ', func(str_))

### 13
# def sort_(l):
#     if l:
#         return [l[-1]] + sort_(l[:-1])
#
#     return []
#
# list_ = [random.randint(1, 100) for i in range(10)]
# print('Your list: ', list_)
# print('Your sorted list: ', sort_(list_))

### 14
# def name_dict(l):
#     d = {i: len(i) for i in l}
#     return d
#
# list_ = ['Marina', 'Yana', 'Vanya', 'Roman', 'Alexandra', 'Evgeny', 'Lev']
# print('List of names: ', list_)
# print('Dict: ', name_dict(list_))

### 15
# def sort_list(l):
#     d = {i: l.count(i) for i in l}
#     list_k = list(d.values())
#     list_k.sort(reverse=True)
#
#     new_d = {}
#     for value in list_k:
#         for key, val in d.items():
#             if val == value and key not in new_d:
#                 new_d[key] = val
#     print(new_d)
#
#     new_list = []
#     keys = list(new_d.keys())
#
#     for i in range(len(new_d)):
#         for j in range(new_d[keys[i]]):
#             new_list.append(keys[i])
#
#     return new_list
#
# list_ = [random.randint(1, 5) for i in range(20)]
# print('Your list: ', list_)
# print('Sorted list: ', sort_list(list_))
