import sqlite3
import random

# conn = sqlite3.connect('name.db')
# cursor = conn.cursor()
# cursor.execute('''DROP TABLE IF EXISTS tab_1''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
#
# cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world')''')
# conn.commit()
#
# d = 'red'
# f = 'black'
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
# cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (d, f))
# conn.commit()
#
# # for i in range(5):
# #     a = input('Enter first value: ')
# #     b = input('Enter second value: ')
# #
# #     cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (a, b))
# #     conn.commit()
#
# cursor.execute('SELECT * FROM tab_1')
# conn.commit()
# print(cursor.fetchall())
#
# cursor.execute('''SELECT * FROM tab_1 WHERE col_1='hello' ''')
# conn.commit()
# print(cursor.fetchall())
#
# # отсортированно
# cursor.execute('''SELECT * FROM tab_1 ORDER BY col_2 ''')
# conn.commit()
# print(cursor.fetchall())
#
# # где значение начинается с определенного символа
# cursor.execute('''SELECT * FROM tab_1 WHERE col_1 LIKE 'h%' ''')
# conn.commit()
# print(cursor.fetchall())

# conn = sqlite3.connect('task1.db')
# cursor = conn.cursor()
# cursor.execute('''DROP TABLE IF EXISTS tab_1''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INTEGER)''')
#
# for i in range(5):
#     s1 = 'col_1_value' + str(i + 1)
#     s2 = 'col_2_value' + str(i + 1)
#     n = int(input('Enter your number: '))
#
#     cursor.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES (?, ?, ?)''', (s1, s2, n))
#     conn.commit()
#
# cursor.execute('SELECT * FROM tab_1')
# res = cursor.fetchall()
# for i in res:
#     print(i)

# cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
# conn.commit()
#
# cursor.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')
# conn.commit()
#
# cursor.execute('''SELECT * FROM tab_1''')
# print(cursor.fetchall())

# conn = sqlite3.connect('task2.db')
# cursor = conn.cursor()
# cursor.execute('''DROP TABLE IF EXISTS tab_1''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
#
# for i in range(5):
#     n1 = random.randint(0, 9)
#     n2 = random.randint(0, 9)
#
#     cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES(?, ?)''', (n1, n2))
#     conn.commit()
#
# cursor.execute('''SELECT * FROM tab_1''')
# res = cursor.fetchall()
#
# for i in res:
#     print(i)
#
# # если через генераторы, то 2 списка
# sum_ = 0
# for row in res:
#     sum_ = sum_ + row[1] + row[2]
#
# aver = sum_ / (len(res) * 2)
# print('\nСреднее арифмитическое: ', aver)
#
# if aver > len(res):
#     cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
#     conn.commit()
#
# cursor.execute('''SELECT * FROM tab_1''')
# print('\n', cursor.fetchall())
#
# t = 2
# cursor.execute('''UPDATE tab_1 SET col_1 = 100 WHERE id = ?''', (t,))
# conn.commit()
#
# cursor.execute('''SELECT * FROM tab_1''')
# print('\n', cursor.fetchall())

# conn = sqlite3.connect('task3.db')
# cursor = conn.cursor()
# cursor.execute('''DROP TABLE IF EXISTS tab_1''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
#
# for i in range(5):
#     n1 = random.randint(0, 9)
#     n2 = random.randint(0, 9)
#
#     cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES(?, ?)''', (n1, n2))
#     conn.commit()
#
# r = random.randint(1, 5)
# print(r)
#
# cursor.execute('''SELECT * FROM tab_1''')
# res = cursor.fetchall()
# print(res)
#
# if res[r - 1][1] % 2 == 0 and res[r - 1][2] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_1 WHERE id = ?''', (r,))
#     conn.commit()
#
#     print('\nNew data1')
#     cursor.execute('''SELECT * FROM tab_1''')
#     res = cursor.fetchall()
#     print(res)
# elif res[r - 1][1] % 2 != 0 and res[r - 1][2] % 2 != 0:
#     cursor.execute('''UPDATE tab_1 SET col_1 = 2, col_2 = 2 WHERE id = ?''', (r,))
#     conn.commit()
#
#     print('\nNew data2')
#     cursor.execute('''SELECT * FROM tab_1''')
#     res = cursor.fetchall()
#     print(res)
# else:
#     print('Values in your table do not fit the condition')

# conn = sqlite3.connect('task4.db')
# cursor = conn.cursor()
#
# cursor.execute('''DROP TABLE IF EXISTS tab_1''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
#
# cols = [1, 2, 3, 4, 5]
# cursor.executemany('''INSERT INTO tab_1 (col_1)  VALUES(?)''', [(x,) for x in cols])
# # cursor.executemany('''INSERT INTO tab_1 (col_1)  VALUES(?), (?), (?), (?), (?)''', (cols,))
# conn.commit()
#
# # for i in range(5):
# #     cursor.execute('''INSERT INTO tab_1 (col_1) VALUES(?);''',  (i + 1,))
# #     conn.commit()
#
# cursor.execute('''SELECT * FROM tab_1''')
# res = cursor.fetchall()
# print(res)
#
# class Task4:
#     def func(self, *args):
#         if len(args) == 1:
#             cursor.execute('''INSERT INTO tab_1 (col_1) VALUES(3)''')
#             conn.commit()
#         elif len(args) == 2 and args[0] is not None and args[1] is not None:
#             if isinstance(args[0], int):
#                 cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
#                 conn.commit()
#         elif len(args) == 3 and args[0] is None and args[1] is None and isinstance(args[2], int):
#             cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id=3''')
#             conn.commit()
#
# task4 = Task4()
# task4.func(7)
# task4.func(2, 6)
# task4.func(None, None, 3)
#
# cursor.execute('''SELECT * FROM tab_1''')
# print(cursor.fetchall())

# conn = sqlite3.connect('task5.db')
# cursor = conn.cursor()
# cursor.execute('''DROP TABLE IF EXISTS tab_1''')
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
#
# for i in range(3):
#     str1 = 'string1_' + str(i)
#     str2 = 'string2_' + str(i)
#     cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES(?, ?)''', (str1, str2))
#     conn.commit()
#
# cursor.execute('''SELECT * FROM tab_1''')
# print('Table after insert 3 records\n', cursor.fetchall(), end='\n' * 2)
#
# cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# print('Table after deletion 2nd record\n', cursor.fetchall(), end='\n' * 2)
#
# cursor.execute('''UPDATE tab_1 SET col_1='hello world', col_2='hello world' WHERE id=3''')
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# res = cursor.fetchall()
# print('Table after update 3rd record\n', res, end='\n' * 2)
#
# with open('task5.txt', 'w') as f:
#     for row in res:
#         f.write('%s - %s - %s\n' % (row[0], row[1], row[2]))
#
#     print('Information is written into file')

conn = sqlite3.connect('task6.db')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS tab_1''')
cursor.execute('''DROP TABLE IF EXISTS tab_2''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

list_ = [12, 56, 'jhd', 45, 'ajg12', 'lwjs', 89, 67, 'skhfb', 45, 'ehkdvs', 'adfsf']
for i in list_:
    if isinstance(i, str):
        cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (i,))
        conn.commit()

        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (len(i),))
        conn.commit()

    elif isinstance(i, int):
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', ('нечтное',))
            conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
res1 = cursor.fetchall()

cursor.execute('''SELECT * FROM tab_2''')
res2 = cursor.fetchall()

if len(res2) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
    conn.commit()
elif len(res2) < 5:
    cursor.execute('''UPDATE tab_1 SET col_1='hello' ''')
    conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
print('First table\n', cursor.fetchall(), end='\n\n')

cursor.execute('''SELECT * FROM tab_2''')
print('Second table\n', cursor.fetchall(), end='\n\n')
