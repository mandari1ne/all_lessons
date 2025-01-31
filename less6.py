arr = [1, 8, 9, 4, 7, 2, 1]

count_ch = 0
count_nch = 0
p = 1

for i in arr:
    if i % 2 == 0:
        count_ch += 1
    else:
        count_nch += 1
    p *= i

if count_ch > count_nch:
    print('Сумма элементов массива: ', sum(arr))
elif count_ch < count_nch:
    print('Произведение 1, 3, 6 элементов: ', arr[1] * arr[3] * arr[6])
else:
    print('Кол-во четных равно колву нечетных')

print('Произведение всех элементов массива: ', p)

print('\nТаблица умножения')
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()
