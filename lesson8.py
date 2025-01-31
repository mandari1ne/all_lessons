print('ЗАДАЧА 1')
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print('sum = ', sum(t))

print('\nЗАДАЧА 2')
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т',
             'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')

temp = []
for i in long_word:
    if i not in temp:
        temp.append(i)
        print(f'В кортеже букв {i} = {long_word.count(i)}')

print('\nЗАДАЧА 3')
week_temp = (26, 29, 34, 32, 28, 26, 23)

sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days

print('Суммарная температура: ', sum_temp)
print('Кол-во дней: ', days)
print('Средняя температура: ', int(mean_temp))
