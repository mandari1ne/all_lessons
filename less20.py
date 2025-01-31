from datetime import datetime
import time
import random

# def list_gen():
#     start = datetime.now()
#     list_ = [i for i in range(100 ** 3)]
#     print(datetime.now() - start)
#
# def list_loop():
#     start = datetime.now()
#     list_ = []
#     for i in range(100 ** 3):
#         list_.append(i)
#     print(datetime.now() - start)
#
# list_gen()
# list_loop()

# from datetime import datetime
# import time
#
# def count_the_time(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         print(datetime.now() - start)
#
#     return wrapper
#
# @count_the_time
# def list_gen():
#     list_ = [i for i in range(100 ** 3)]
#
# @count_the_time
# def list_loop():
#     list_ = []
#     for i in range(100 ** 3):
#         list_.append(i)
#
# list_gen()
# list_loop()

# def decorator(func):
#     def wrapper():
#         print('функция-оболочка')
#         func()
#
#     return wrapper
#
# def basic():
#     print('основная функция')
#
# wrapped = decorator(basic)
# print('старт программы')
# basic()
# wrapped()
# print('конец программы')

# def decorator(func):
#     print('декоратор')
#
#     def wrapper():
#         print('-- до функции', func.__name__)
#         func()
#         print('-- после функции', func.__name__)
#
#     return wrapper
#
# @decorator
# def wrapped():
#     print('--- обернутая функция')
#
# print('- старт программы...')
# wrapped()
# print('- конец программы')

#ЗАДАЧА 1
# def decorator(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         func()
#         count += 1
#         print(f'{count} раз/раза', end='\n\n')
#
#     return wrapper
#
# # def decorator(func):
# #     def wrapper():
# #         wrapper.count += 1
# #         return func()
# #
# #     wrapper.count = 0
# #     return wrapper
#
# @decorator
# def hello():
#     print('Hello World!')
#
# @decorator
# def foo():
#     print('cap')
#
# hello()
# hello()
# foo()
# hello()


#ТАЙМЕРЫ
# def elapsed(func):
#     def wrapper(a, b, delay=0):
#         start = datetime.now()
#         func(a, b, delay)
#         end = datetime.now()
#         elapsed = (end - start).total_seconds() * 1000
#         print(f'>> функция {func.__name__} время выполнения (ms): {elapsed}')
#
#     return wrapper
#
# @elapsed
# def add_with_delay(a, b, delay=0):
#     print('сложить', a, b, delay)
#     time.sleep(delay)
#     return a + b
#
# print('старт программы')
# add_with_delay(10, 20)
# add_with_delay(10, 20, 1)
# print('конец программы')


# app = {}
#
# def callback(route):
#     def wrapper(func):
#         app[route] = func
#
#         def wrapped():
#             ret = func()
#             return ret
#
#         return wrapped
#
#     return wrapper
#
# @callback('/')
# def index():
#     print('index')
#
#     return 'OK'
#
# print('> start')
# route = app['/']
#
# if route:
#     resp = route()
#     print('response:', resp)
#
# print('> end')


# Напишите декоратор retry, который будет повторять выполнение функции определенное количество раз
# в случае возникновения исключения.
# Декоратор должен принимать два аргумента:
# max_retries — максимальное количество попыток выполнения функции.
# delay — время ожидания перед повторной попыткой (в секундах).
# Если функция завершится успешно, возвращайте результат.
# Если после всех попыток функция все еще вызывает исключение, выбрасывайте это исключение.

def retry(func):
    count = 1
    def wrapper(max_retries, delay):
        nonlocal count

        if count <= max_retries:
            try:
                return func(max_retries, delay)
            except ZeroDivisionError:
                print('ZeroDivisionError')
                count += 1
                time.sleep(delay)
                return wrapper(max_retries, delay)
        else:
            raise 'ZeroDivisionError'

    return wrapper

@retry
def foo(max_retries, delay):
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    print(a, b)

    return f'{a} / {b} = {a / b}'

try:
    print(foo(5, 1))
except BaseException:
    print('ZeroDivisionError')
