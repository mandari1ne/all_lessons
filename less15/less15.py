import csv

# exampleFile = open('example.csv', encoding='UTF-8')
# exampleReader = csv.reader(exampleFile, delimiter=';')
#
# #exampleData = list(exampleReader)
# #print(exampleData)
#
# for row in exampleReader:
#     string = 'Строка #' + str(exampleReader.line_num) + ' '
#
#     for value in row:
#         string = string + value + ' '
#
#     print(string)
#
# exampleFile.close()

# exampleFile = open('output.csv', 'w', encoding='UTF-8', newline='')
# exampleWriter = csv.writer(exampleFile, delimiter=';')
# exampleDate = [['05.04.2015 13:34', 'Яблоки', '73'],
#                ['05.04.2015 3.41', 'Вишни', '85'],
#                ['06.04.2015 12:46', 'Груши', '14']]
#
# for row in exampleDate:
#     exampleWriter.writerow(row)
#
# exampleFile.close()

import json

# string = '{"id":765,"email":"ivanov@mail.ru","surname":"Иванов","age":45,"admin":false,"friends":[123,456,789]}'
# # data = json.loads(string)
# #
# # print(data["email"])
# # print(data["surname"])
# # print(data["admin"])
# # print(data["friends"])
#
# with open('data.json', encoding='UTF-8') as file:
#     data = json.load(file)
#
# print(data["email"])
# print(data["surname"])
# print(data["admin"])
# print(data["friends"])

# data = {"id": 765, "email": "ivanov@mail.ru", "surname": "Иванов", "age": 45,
#         "admin": False, "friends": [123, 456, 789]}
#
# with open('data.json', 'w', encoding='UTF-8') as file:
#     json.dump(data, file)
#
# with open('data.json', 'w', encoding='UTF-8') as file:
#     json.dump(data, file, ensure_ascii=False)
#
# Задача 1: Чтение CSV-файла
# Напишите программу, которая читает данные из файла employees.csv,
# содержащего информацию о сотрудниках (имя, должность, зарплата).
# Выведите на экран имена всех сотрудников.
#
# emp_file = open('employees.csv', encoding='UTF-8')
# emp_reader = csv.reader(emp_file, delimiter=';')
# emp_data = list(emp_reader)
#
# for e in emp_data:
#     print(e[0], end=' ')
#
# emp_file.close()
#
# Задача 2: Запись данных в CSV-файл
# Создайте программу, которая собирает информацию о трех фильмах (название, режиссер и год выпуска)
# и записывает эти данные в файл movies.csv. Каждая запись должна быть в отдельной строке.
#
# film_file = open('films.csv', 'w', encoding='UTF-8', newline='')
# film_writer = csv.writer(film_file, delimiter=';')
# film_data = [
#     ['Гарри Поттер', 'Крис Коламбус', 2001],
#     ['Перси Джексон', 'Крис Коламбус', 2010],
#     ['Первый Мститель', 'Джо Джонстон', 2011]
# ]
#
# for row in film_data:
#     film_writer.writerow(row)
#
# film_file.close()
#
# Задача 3: Обновление данных в CSV-файле
# Напишите программу, которая читает данные из файла products.csv,
# содержащего информацию о товарах (название, цена и количество).
# Увеличьте цену каждого товара на 15% и сохраните обновленные данные обратно в файл.
#
# products_file = open('products.csv', 'r+', encoding='UTF-8', newline='')
# products_reader = csv.reader(products_file, delimiter=';')
# products_data = list(products_reader)
#
# for row in products_data:
#     row[1] = str(round(0.15 * float(row[1]) + float(row[1]), 2))
#
# products_file.seek(0)
# products_writer = csv.writer(products_file, delimiter=';')
#
# for row in products_data:
#     products_writer.writerow(row)
#
# products_file.close()

#Задача 1: Чтение JSON-файла
#Напишите программу, которая читает данные из файла data.json,
# содержащего информацию о студентах (имя, возраст и оценка).
# Выведите на экран имена всех студентов.

# with open('data1.json', encoding='UTF-8') as file:
#     data = json.load(file)
#
# for i in data:
#     print(data[i]['name'])

#Задача 2: Запись данных в JSON-файл
#Создайте программу, которая собирает информацию о трех книгах (название, автор и год издания)
# и записывает эти данные в файл books.json. Каждая книга должна быть представлена как объект в массиве.

# books = [
#     {"name": "Гарри Поттер", "author": "Джоан Роулинг", "year": 2001},
#     {"name": "Перси Джексон", "author": "Рик Риордан", "year": 2010},
#     {"name": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1928}
# ]
#
# with open('books.json', 'w', encoding='UTF-8') as file:
#     json.dump(books, file, ensure_ascii=False)

#Задача 3: Обновление данных в JSON-файле
#Напишите программу, которая читает данные из файла employees.json,
# содержащего информацию о сотрудниках (имя, должность и зарплата).
# Увеличьте зарплату каждого сотрудника на 10% и сохраните обновленные данные обратно в файл.

with open("employees.json", "r+", encoding="UTF-8") as file:
    data = json.load(file)

    for i in data:
        i["salary"] = round(0.1 * i["salary"] + i["salary"], 2)

    file.seek(0)
    json.dump(data, file, ensure_ascii=False)
    file.truncate()
