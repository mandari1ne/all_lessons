import json

product = []
while True:
    try:
        check = input('\nЖелаете добавить покупику? Если нет, введите [стоп]: ')

        if check == 'стоп':
            break
        elif check != 'да' and check != 'стоп':
            raise ValueError

        name_prod = input('Введите название покупки: ')
        cost_prod = float(input('Введите стоимость покупки: '))

        dict_ = {'название': str(name_prod), 'стоимость': str(cost_prod)}
        product.append(dict_)
    except ValueError:
        print('Некорректный ввод!', end='\n' * 2)

with open('product.json', 'w+', encoding='UTF-8') as file:
    json.dump(product, file, ensure_ascii=False)

    file.seek(0)
    data = json.load(file)

    sum_ = 0
    for i in data:
        sum_ += float(i['стоимость'])

    print('\nСтоимость всех покупок за день: ', sum_)
