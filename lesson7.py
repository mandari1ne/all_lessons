product = {'Honor X9B': [1000, 5],
           'Honor 200Lite': [1389.99, 7],
           'Honor 8X': [559, 13],
           'Samsung Galaxy S23': [1799, 8],
           'Samsung Galaxy A55': [1569.67, 10],
           'Apple iPhone 15 Pro': [4399, 11]
           }

while True:
    product_keys = product.keys()

    print('Меню:')
    print('[1] Посмотреть товары')
    print('[2] Осуществить покупку')
    print('[3] Выход из программы')
    n = int(input('Ваш выбор: '))

    if n == 1:
        n1 = int(input('\n[1] - Посмотреть все товары \n[2] - Посмотреть определенный товар \nВаш выбор: '))

        if n1 == 1:
            for k in product_keys:
                print(f'{k} - {product[k][0]} - {product[k][1]}')
        elif n1 == 2:
            choice = input('Введите марку товара: ')

            if choice.title() not in product_keys:
                print('Товара с таким название нет')
            else:
                for k in product_keys:
                    if k == choice.title():
                        print(f'{k} - {product[k][0]} - {product[k][1]}')
                        break
        print()

    elif n == 2:
        order = {}
        order_sum = 0
        check_product = 0

        while True:
            choice = input('\nВведите название товара либо 0 для выхода: ').title()

            if choice == '0':
                break
            elif choice.title() not in product_keys:
                print('Товара с таким название нет')
            else:
                check_product = 1
                count_choice = int(input('Введите кол-во товара: '))

                if product[choice][1] < count_choice:
                    new_count_choice = int(input(
                        f'Недостаточное кол-во товара на складе, введите число меньше {count_choice}: '))
                    product[choice][1] -= new_count_choice
                    order_sum += roduct[choice][0]
                elif product[choice][1] > count_choice:
                    product[choice][1] -= count_choice
                    order_sum += product[choice][0]

        if check_product == 1:
            order_keys = order.keys()
            print(f'Ваш заказ на сумму {order_sum}')

            while True:
                choice = int(input('[1] - Подтвердить \n[2] - Отменить \n'))
                if choice == 1:
                    print('Ваш заказ успешно оформлен')
                    break
                elif choice == 2:
                    for k in order_keys:
                        product[k][1] += order[k]
                #print(product)
                break
            else:
                print('Неверный ввод')

        print()

    elif n == 3:
        break
    else:
        print('Неверный выбор')