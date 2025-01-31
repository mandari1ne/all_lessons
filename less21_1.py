# import time
#
# def fun1(x):
#     print('Запуск fun1...')
#     print(f'x ** 2 = {x ** 2}')
#     print('fun1 засыпает...')
#     time.sleep(3)
#     print('...fun1 очнулась и завершена')
#
# def fun2(x):
#     print('Запуск fun2...')
#     print(f'x ** 0.5 = {x ** 0.5}')
#     print('fun2 засыпает...')
#     time.sleep(3)
#     print('...fun1 очнулась и завершена')
#
# def main():
#     fun1(4)
#     fun2(4)
#
# print(time.strftime('%X'), ': программа запущена')
#
# main()
#
# print(time.strftime('%X'), ': программа завершена')

# import asyncio
# import time

# async def fun1(x):
#     print(x ** 2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
# async def fun2(x):
#     print(x ** 0.5)
#     await asyncio.sleep(3)
#     print('fun3 завершена')
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
# # print(time.strftime('%X'))
# # if __name__ == '__main__': # можно и чисто раном
# #     asyncio.run(main())
# # print(time.strftime('%X'))
#
# # ЦИКЛ СОБЫТИЙ
# print(time.strftime('%X'))
#
# loop = asyncio.get_event_loop()
# task1 = loop.create_task(fun1(4))
# task2 = loop.create_task(fun2(4))
# loop.run_until_complete(asyncio.wait([task1, task2]))
#
# print(time.strftime('%X'))

# async def get_conn(host, port):
#     class Conn:
#         async def put_data(self):
#             print('Отправка данных...')
#             await asyncio.sleep(2)
#             print('Данные отправлены.')
#
#         async def get_data(self):
#             print('Получение данных...')
#             await asyncio.sleep(2)
#             print('Данные получены.')
#
#         async def close(self):
#             print('Завершение соединения...')
#             await asyncio.sleep(2)
#             print('Соединение завершено.')
#
#     print('Установление соединения...')
#     await asyncio.sleep(2)
#     print('Соединение установлено.')
#     return Conn()
#
# class Connection():
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#
#     async def __aenter__(self):
#         self.conn = await get_conn(self.host, self.port)
#         return self.conn
#
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.conn.close()
#
# async def main():
#     async with Connection('localhost', 9001) as conn:
#         send_task = asyncio.create_task(conn.put_data())
#         receive_task = asyncio.create_task(conn.get_data())
#
#         await send_task
#         await receive_task
#
# asyncio.run(main())

# import time
# from aiohttp import ClientSession
#
# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
#
#         async with session.get(url, params=params) as response:
#             weather_json = await response.json()
#             print(f'{city}: {weather_json["weather"][0]["main"]}')
#
# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))
#
#     for task in tasks:
#         await task
#
# cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#           'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York',]
#
# print(time.strftime('%X'))
#
# asyncio.run(main(cities))
#
# print(time.strftime('%X'))

# import asyncio
# import time
# from aiohttp import ClientSession
#
# async def fetch_url_data(session, url):
#     try:
#         async with session.get(url, timeout=60) as response:
#             resp = await response.read()
#     except Exception as e:
#         print(e)
#     else:
#         return resp
#
# async def fetch_async(loop, r):
#     url = 'https://www.uefa.com/uefaeuro-2020'
#     tasks = []
#     async with ClientSession() as session:
#         for i in range(r):
#             task = asyncio.ensure_future(fetch_url_data(session, url))
#             tasks.append(task)
#         responses = await asyncio.gather(*tasks)
#
#     return responses
#
# if __name__ == '__main__':
#     for ntimes in [1, 10, 50, 100, 500]:
#         start_time = time.time()
#         loop = asyncio.get_event_loop()
#         future = asyncio.ensure_future(fetch_async(loop, ntimes))
#         # будет выполняться до тех пор, пока не завершится или не возникнет ошибка
#         loop.run_until_complete(future)
#         responses = future.result()
#         print(f'Получено {ntimes} результатов запроса за {time.time() - start_time} секунд')

# import threading
# import time
# import random
#
# def worker(number):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print('I am Worker {}, I slept for {} seconds'.format(number, sleep))
#
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()
#
# print("All Threads are queued, let's see when they finish!")

# from threading import Thread, Lock
# from time import sleep, time, strftime
#
# lock = Lock()
# stop_thread = False
#
# def infinit_worker():
#     print('Start infinit_worker()')
#
#     while True:
#         print('--> thread work')
#         lock.acquire()
#
#         if stop_thread:
#             break
#
#         lock.release()
#         sleep(0.1)
#
#     print('Stop infinit_worker()')
#
# th = Thread(target=infinit_worker)
# th.start()
# sleep(2)
#
# lock.acquire()
# stop_thread = True
# lock.release()

# ПОТОКИ ДЕМОНЫ
# from threading import Thread
# from time import sleep
#
# def func():
#     for i in range(5):
#         print(f'from child thread {i}')
#         sleep(0.5)
#
# th = Thread(target=func, daemon=True)
# th.start()
# print('App stop')

import multiprocessing

def cube(n):
    print('The Cube is: {}'.format(n * n * n))

def square(n):
    print('The Square is: {}'.format(n * n))

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=cube, args=(5, ))
    process2 = multiprocessing.Process(target=square, args=(5, ))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Both processes are finished')
