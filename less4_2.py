your_date = input('Введите дату вашего рождения: ').lower()

if '.' in your_date:
    date = your_date.split('.')
else:
    date = your_date.split()

date[0] = int(date[0])

if ((date[1] == '03' or date[1] == 'марта') and date[0] >= 21 and date[0] <= 31 or
        (date[1] == '04' or date[1] == 'апреля') and date[0] >= 1 and date[0] <= 20):
    print('Ваш знак зодиака - Овен')
elif ((date[1] == '04' or date[1] == 'апреля') and date[0] >= 21 and date[0] <= 30 or
      (date[1] == '05' or date[1] == 'мая') and date[0] >= 1 and date[0] <= 20):
    print('Ваш знак зодиака - Телец')
elif ((date[1] == '05' or date[1] == 'мая') and date[0] >= 21 and date[0] <= 31 or
      (date[1] == '06' or date[1] == 'июня') and date[0] >= 1 and date[0] <= 20):
    print('Ваш знак зодиака - Близнецы')
elif ((date[1] == '06' or date[1] == 'июня') and date[0] >= 21 and date[0] <= 30 or
      (date[1] == '07' or date[1] == 'июля') and date[0] >= 1 and date[0] <= 22):
    print('Ваш знак зодиака - Рак')
elif ((date[1] == '07' or date[1] == 'июля') and date[0] >= 23 and date[0] <= 31 or
      (date[1] == '08' or date[1] == 'августа') and date[0] >= 1 and date[0] <= 22):
    print('Ваш знак зодиака - Лев')
elif ((date[1] == '08' or date[1] == 'августа') and date[0] >= 23 and date[0] <= 31 or
      (date[1] == '09' or date[1] == 'сентября') and date[0] >= 1 and date[0] <= 22):
    print('Ваш знак зодиака - Дева')
elif ((date[1] == '09' or date[1] == 'сентября') and date[0] >= 23 and date[0] <= 30 or
      (date[1] == '10' or date[1] == 'октября') and date[0] >= 1 and date[0] <= 22):
    print('Ваш знак зодиака - Весы')
elif ((date[1] == '10' or date[1] == 'октября') and date[0] >= 23 and date[0] <= 31 or
      (date[1] == '11' or date[1] == 'ноября') and date[0] >= 1 and date[0] <= 22):
    print('Ваш знак зодиака - Скорпион')
elif ((date[1] == '11' or date[1] == 'ноября') and date[0] >= 23 and date[0] <= 30 or
      (date[1] == '12' or date[1] == 'декабря') and date[0] >= 1 and date[0] <= 21):
    print('Ваш знак зодиака - Стрелец')
elif ((date[1] == '12' or date[1] == 'декабря') and date[0] >= 22 and date[0] <= 31 or
      (date[1] == '01' or date[1] == 'января') and date[0] >= 1 and date[0] <= 19):
    print('Ваш знак зодиака - Козерог')
elif ((date[1] == '01' or date[1] == 'января') and date[0] >= 20 and date[0] <= 31 or
      (date[1] == '02' or date[1] == 'февраля') and date[0] >= 1 and date[0] <= 19):
    print('Ваш знак зодиака - Володей')
elif ((date[1] == '02' or date[1] == 'февраля') and date[0] >= 20 and date[0] <= 29 or
      (date[1] == '03' or date[1] == 'марта') and date[0] >= 1 and date[0] <= 20):
    print('Ваш знак зодиака - Рыбы')
else:
    print('Неверный ввод')
