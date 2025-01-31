# iter_obj = iter([1, 2, 3, 4, 5])
#
# while True:
#     try:
#         i = next(iter_obj)
#         print(i)
#     except StopIteration:
#         break

# class IterationExample:
#     def __iter__(self):
#         self.x = 0
#
#         return self
#
#     def __next__(self):
#         y = self.x
#         self.x += 1
#
#         return y
#
# class_instance = IterationExample()
# elements = iter(class_instance)

# class StoppingIteration:
#     def __iter__(self):
#         self.x = 1
#
#         return self
#
#     def __next__(self):
#         if self.x <= 5:
#             y = self.x
#             self.x += 1
#
#             return y
#         else:
#             raise StopIteration
#
# class_instance = StoppingIteration()
# elements = iter(class_instance)
#
# for i in elements:
#     print(i)

# elements = [2, 4, 6, 8, 10]
#
# def square_all(numbers):
#     for n in numbers:
#         yield n ** 2
#
# squares = square_all(elements)
# print(next(squares))
# squares1 = (n ** 2 for n in elements)
# print(next(squares1))

# def gen_fib(num):
#     tmp1 = 1
#     tmp2 = 0
#
#     for i in range(num):
#         yield tmp1
#         tmp1 = tmp1 + tmp2
#         tmp2 = tmp1 - tmp2
#
# fib = list(gen_fib(8))
# print(fib)

# def gen_fib(num):
#     tmp1 = 1
#     tmp2 = 1
#
#     for i in range(num):
#         yield tmp1
#         tmp, tmp1, tmp2 = tmp1, tmp2, tmp1 + tmp2
#
# fib = list(gen_fib(8))
# print(fib)

# def gen_fib(num):
#     tmp1 = 0
#     tmp2 = 1
#
#     for i in range(num):
#         yield tmp2
#         tmp1, tmp2 = tmp2, tmp1 + tmp2
#
# fib = list(gen_fib(8))
# print(fib)

# 1
# Чтение файла построчно:
# Напишите программу,
# которая открывает текстовый файл и выводит на экран каждую строку, пронумеровав её.
# Например: "1: Первая строка".

# with open('1.txt', 'r') as file:
#     info = iter(file.read().split('\n'))
#
#     i = 1
#     for line in info:
#         print(f'Строка {i}: {line}')
#         i += 1

# 2
# Запись в файл:
# Создайте программу, которая запрашивает у пользователя
# несколько строк текста и записывает их в файл.
# Программа должна завершаться, когда пользователь введёт пустую строку.

# def gen_info():
#     while True:
#         s1 = input('Введите строку: ')
#
#         if s1 == '':
#             break
#
#         yield s1
#
# strs = list(gen_info())
# print(strs)
#
# with open('2.txt', 'w') as file:
#     info = '\n'.join(strs)
#     file.write(info)
#     print('Записалось!')

# 3
# Копирование файла:
# Реализуйте функцию, которая копирует содержимое одного текстового файла в другой.
# Используйте итераторы для чтения и записи данных.

# def copy_func():
#     with open('1.txt', 'r') as file:
#         info = iter(file.read().split('\n'))
#
#         with open('3.txt', 'w') as file1:
#             for line in info:
#                 file1.write(line + '\n')
#
#         print('Все гуд!')
#
# copy_func()

# 4
# Подсчет слов:
# Напишите программу, которая открывает текстовый файл
# и подсчитывает количество слов в нём.
# Используйте итераторы для обработки строк.

# def count_str():
#     count = 0
#
#     with open('1.txt', 'r') as file:
#         info = iter(file.read().split('\n'))
#
#         for i in info:
#             count += 1
#
#     return count
#
# print('Кол-во строк в файле: ', count_str())

# 5
# Фильтрация строк:
# Создайте программу, которая читает файл и выводит только те строки,
# которые содержат определённое слово (например, "Python").
# Слово должно запрашиваться у пользователя.

# def read_file():
#     with open('5.txt', 'r') as file:
#         info = iter(file.read().split('\n'))
#
#         return info
#
# def filter_str():
#     word = input('\nВведите слово: ')
#     info = read_file()
#
#     check = 0
#     for i in info:
#         if word in i:
#             print(i)
#             check = 1
#
#     if check == 0:
#         print('В файле такого слова нет')
#
# file_info = read_file()
# print('Содержимое файла')
# for i in file_info:
#     print(i)
#
# filter_str()

# 6
# Объединение файлов:
# Напишите программу, которая объединяет содержимое нескольких текстовых файлов в один.
# Пусть имена файлов будут переданы в качестве аргументов командной стоки.

# def read_file(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line
#
# def get_filenames():
#     while True:
#         name = input('Введите имя файла либо ничего, если ввод окончен: ')
#
#         if name == '':
#             break
#
#         yield name
#
# def copy_files():
#     names = list(get_filenames())
#
#     if names != []:
#         new_file = input('\nВведите имя нового файла: ')
#
#         try:
#             with open(new_file, 'w') as file1:
#                 for name in names:
#                     file_info = iter(read_file(name))
#
#                     for line in file_info:
#                         file1.write(line)
#                     file1.write('\n')
#
#                 print('Все гуд!')
#         except FileNotFoundError:
#             print('Файл не найден!!!')
#     else:
#         print('\nНичего не введено!')
#
# copy_files()

# 7
# Итератор для чтения файла:
# Создайте свой собственный итератор, который будет читать файл построчно.
# Итератор должен возвращать строки по одной при каждом вызове next().

# def read_file():
#     with open('1.txt', 'r') as file:
#         info = iter(file.read().split('\n'))
#
#         return info
#
# file_info = read_file()
# try:
#     while True:
#         print(next(file_info))
# except StopIteration:
#     pass

# 8
# Поиск максимального числа:
# Напишите программу, которая считывает числовые данные из файла
# (по одному числу на строку) и находит максимальное число,
# используя итераторы.

# def max_found():
#     with open('8.txt', 'r') as file:
#         nums = iter(int(n) for n in file)
#
#         return max(nums)
#
# print(max_found())

# 9
# Удаление пустых строк:
# Реализуйте программу, которая читает текстовый файл и записывает его в новый файл,
# удаляя все пустые строки.

# def read_file():
#     with open('9.txt', 'r') as file:
#         for line in file:
#             line = line.strip()
#             yield line
#
# def write_file():
#     with open('9_1.txt', 'w') as file:
#         info = iter(read_file())
#
#         for line in info:
#             if line != '':
#                 file.write(line + '\n')
#
#         print('Все гуд!')
#
# write_file()

# 10
# Сортировка строк:
# Напишите программу, которая читает строки из файла,
# сортирует их в алфавитном порядке и записывает отсортированные строки в новый файл.

def read_file():
    with open('1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            yield line

def write_new_file():
    with open('10.txt', 'w') as file:
        info_unsort = iter(read_file())
        info = sorted(info_unsort)

        for line in info:
            file.write(line + '\n')

        print('Все гуд!')

write_new_file()
