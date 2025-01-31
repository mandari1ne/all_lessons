# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f'Вызвана функция {func.__name__} с аргументами {args, kwargs} '
#               f'и возвращаемым значением {func(*args, **kwargs)}')
#
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @debug
# def func1(a, b):
#     return a + b
#
# @debug
# def func2(s, g):
#     return s, g
#
# @debug
# def func3():
#     return 'Good job!!!'
#
# func1(2, 3)
# func2('Hello!', g='trulala')
# func3()

# Задание1
# Описание: Создайте декоратор timeout, который будет ограничивать время выполнения функции.
# Если функция не завершает выполнение в заданное время, она должна выбрасывать исключение TimeoutError.
# Требования:
# - Декоратор должен принимать время в секундах как аргумент.
# - Используйте модуль threading для реализации ограничения времени.

# import threading
# import time
#
# def timeout(func):
#     def wrapper(time_):
#         t = threading.Thread(target=func, args=(time_,))
#
#         t.start()
#         t.join(timeout=time_ + 1)
#
#         if t.is_alive():
#             raise TimeoutError
#         else:
#             print('Все гуд!')
#
#     return wrapper
#
# @timeout
# def func1(time1):
#     print('Первая функция запущена')
#     time.sleep(time1)
#
# @timeout
# def func2(time2):
#     print('Вторая функция запущена')
#     time.sleep(time2 + 5)
#
# try:
#     func1(2)
# except TimeoutError:
#     print('Ошибка времени выполнения!')
#
# try:
#     func2(2)
# except TimeoutError:
#     print('Ошибка времени выполнения!')

# Задача2
# Описание: Напишите декоратор requires_permission,
# которые будет проверять, есть ли у пользователя необходимые права доступа для выполнения функции.
# Если прав недостаточно, функция должна возвращать сообщение об ошибке.
# Требования:
# - Декоратор должен принимать строку с названием необходимого разрешения.
# - Используйте переменную user_permission для имитации прав доступа пользователя

def requires_permission(user_permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_permission:
                func(*args, **kwargs)
            else:
                print('You are not allowed to do that.')

        return wrapper
    return decorator

class User:
    def __init__(self, name, user_permission):
        self.name = name
        self.user_permission = user_permission

    def important_func(self):
        @requires_permission(self.user_permission)
        def func():
            print('trulala')

        func()

user1 = User('Albert', True)
user1.important_func()

user2 = User('Adolf', False)
user2.important_func()
