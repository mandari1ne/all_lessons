from random import randint

n1 = randint(1, 10)
n2 = randint(1, 2)

check_n1 = int(input('Угадайте число: '))
check_n2 = int(input('Угадайте цвет ([1] - красный, [2] - черный): '))

is_n1 = check_n1 == n1
is_n2 = check_n2 == n2

if is_n1 and is_n2:
    print('Вы угадали')
else:
    if n2 == 1:
        print(f'Правильная комбинация: {n1} и [{n2} - красный]')
    else:
        print(f'Правильная комбинация: {n1} и [{n2} - черный]')
