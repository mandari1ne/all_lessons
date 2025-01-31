import os

# path1 = input('Введите название входного файла: ')
# path2 = input('Введите название выходного файла: ')
#
# listdir_ = os.listdir()
#
# if path1 not in listdir_:
#     print('Файл не найден')
# else:
#     with open(path1, 'r') as f1:
#         with open(path2, 'w') as f2:
#             file1 = f1.read().split(' ')
#             print('Содержимое входного файла: ', file1)
#
#             file2 = []
#             for i in file1:
#                 if i not in file2:
#                     file2.append(i)
#
#             file2 = ' '.join(file2)
#             f2.write(file2)
#             print('Содержимое выходного файла: ', file2)

# path = input('Введите название файла: ')
# listdir_ = os.listdir()
#
# if path not in listdir_:
#     print('Файл не найден')
# else:
#     with open(path, 'r+') as f:
#         file = f.read().split(' ')
#         print('Содержимое файла: ', ' '.join(file))
#
#         while True:
#             word = input('Введите слово, которое хитите заменить: ')
#
#             if word not in file:
#                 print('Такого слова нет: ')
#             else:
#                 break
#
#         new_word = input('Введите слово, на которое хотите заменить: ')
#
#         for i in range(len(file)):
#             if file[i] == word:
#                 file[i] = new_word
#         f.seek(0)
#         f.truncate()
#         f.write(' '.join(file))
#
#         f.seek(0)
#         print('Обновленный файл: ', f.read())

# path = input('Введите название файла: ')
# listdir_ = os.listdir()
#
# if path not in listdir_:
#     print('Файл не найден')
# else:
#     with open(path, 'r') as f:
#         print('Содержимое файла:')
#         print(f.read(), end='\n' * 2)
#         f.seek(0)
#         file = f.read().replace('\n', '').replace(' ', '')
#
#         tmp = []
#         for i in file:
#             if i not in tmp:
#                 tmp.append(i)
#                 print(f'Символ {i} встречается в файле {file.count(i)}')

path = input('Введите название файла: ')
listdir_ = os.listdir()

if path not in listdir_:
    print('Файл не найден')
else:
    with open(path, 'r+') as f:
        print('Содержимое файла:')
        print(f.read(), end='\n' * 2)
        f.seek(0)
        file = f.read().split(' ')

        new_path = input('Введите новое имя файла: ')
        with open(new_path, 'w+') as f2:
            file = sorted(file, key=str.lower)
            f2.write(' '.join(file))

            f2.seek(0)
            print('Содержимое нового файла: ', f2.read())
