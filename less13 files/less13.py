# path = 'D:\COURSES\less13 files\example.txt'
# f = open(path, 'r')
#
# with open(path) as f:
#     print(*f)

#print(f.read(7)) #читает 7 символов

# print(f.readline())
# print(f.readline())

#print(f.readlines())

# f = open(path, 'w')
# f.write('Hello \nWorld!')
# f.close()

#import os

#os.rename('example.txt', '11.txt')
#print(os.getcwd())

# os.chdir('folder') #изменение папки на folder
# os.chdir('..') #поднятие на папку выше
# os.makedirs('nested1/nested2/nested3') #создание вложенных папок

# with open('1.txt') as f:
#     tmp_f = f.read().split(' ')
#     print(tmp_f)
#     tmp_n = [int(i) for i in tmp_f if i.isdigit()]
#     print(sum(tmp_n))

# with open('2.txt') as f:
#     tmp_f = f.readlines()
#     new_tmp = [i.replace('\n', '') for i in tmp_f]
#     num = [int(i) for i in new_tmp if i.isnumeric()]
#     str_ = [i for i in new_tmp if not i.isnumeric()]
#     print(sorted(num) + sorted(str_, key=len))
#     #print(sorted(num) + sorted(str_, key=lambda x: (len(x), x)))

# with open('3.txt', 'w') as f:
#     while True:
#         str_ = input('Enter your string: ')
#
#         if str_ == '':
#             break
#         f.write(str_ + '\n')

# with open('4.txt') as f:
#     #tmp_f = f.readlines()
#     tmp_f = f.read().split('\n')
#     print(tmp_f)
#     print('Кол-во строк в файле: ', len(tmp_f))
#
#     #dict_ = {i.replace('\n', ''): len(i) - 1 for i in tmp_f}
#     dict_ = {i: len(i) for i in tmp_f}
#     print('Слова в файле и их длина: ', dict_)
