p = 1
for i in range(1, 31, 2):
    p *= i

print('Произведение  нечетных чисел от 1 до 30: ', p)

arr = []
for i in range(5, 101, 5):
    arr.append(i)

print('\nЧисла от 1 до 100, кратные 5: ', arr)

print('\nЧетные числа от 1 до 71')
for i in range(2, 71, 2):
    print(i, end=' ')

arr = [1, 1, 4, 6, 2, 1, 4, 4, 7]
new_arr = []
print('\n\nИсходный массив: ', arr)

for i in range(len(arr)):
    if arr[i] not in new_arr:
        count = 0

        for j in range(len(arr)):
            if arr[j] == arr[i]:
                count += 1

        if count > 2:
            new_arr.append(arr[i])

print('Новый массив: ', new_arr)
