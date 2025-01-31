# 2 игрока, игра в кости, бросает 1й, 2й выбирает выпадет больше или меньше,
# затем бросате, угадал - выиграл, иначе проиграл

from random import randint

res1_1 = randint(1, 6)
res1_2 = randint(1, 6)

print('1й игрок сделал свой ход')

choice = input('Выбирает 2й игрок (1 - больше, 2 - меньше): ')

res2_1 = randint(1, 6)
res2_2 = randint(1, 6)

print(f'Результат 1го игрока: {res1_1} + {res1_2}')
print(f'Результат 2го игрока: {res2_1} + {res2_2}')

if res1_1 + res1_2 > res2_1 + res2_2 and choice == '2':
    print('Выиграл  2й игрок')
elif res1_1 + res1_2 > res2_1 + res2_2 and choice == '1':
    print('Выиграл  1й игрок')
elif res1_1 + res1_2 < res2_1 + res2_2 and choice == '2':
    print('Выиграл  1й игрок')
elif res1_1 + res1_2 < res2_1 + res2_2 and choice == '1':
    print('Выиграл  2й игрок')
elif res1_1 + res1_2 == res2_1 + res2_2:
    print('Ничья')
