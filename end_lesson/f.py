from string import Template

x = 1
print(f'Строка {x} конец строки')
print('Строка %d конец строки' % x)

template = Template('Строка $number конец строки')
print(template.substitute(number=x))



print('Строка ' + str(x) + 'конец строки')
