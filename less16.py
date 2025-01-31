# class Human:
#     legs = 2 #статическое св-во класса (статический атрибут класса)
#     eyes = 2
#
#     def __init__(self, name, surname, eyes_color):
#         self.name = name
#         self.surname = surname
#         self.eyes_color = eyes_color
#
#     def talking(self):
#         print(self.name, 'что-то сказал')
#
#     def do_jump(self):
#         print(self.name, 'прыгнул')
#
# human1 = Human('Richard', 'Olegovich', 'blue')
# human2 = Human('Kate', 'Olegovich', 'red')
# human3 = Human('Ivan', 'Ivanovich', 'green')

# class Car:
#
#     #Статические поля (переменные класса)
#     default_color = 'Grey'
#     default_weight = 5000
#
#     def __init__(self, color, model):
#         #Динамические поля класса
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass

# 1
# from random import randint
#
# class Example:
#     num1 = 1
#     num2 = 3
#
#     def def1(self):
#         str_ = 'Hello World'
#         print(str_)
#
#     def sum_(self):
#         return self.num1 + self.num2
#
#     def def3(self):
#         n1 = randint(1, 20)
#         n2 = randint(1, 5)
#
#         print(f'{n1}^{n2} = {n1 ** n2}')
#
#
# example = Example()
#
# example.def1()
# print(example.sum_())
# example.def3()

#2
# class Calculator:
#     n1 = 0
#     op = ''
#     n2 = 0
#
#     def set_data(self):
#         self.n1 = float(input('Enter first number: '))
#         self.op = input('Enter operation: ')
#         self.n2 = float(input('Enter second number: '))
#
#     def plus(self):
#         return self.n1 + self.n2
#
#     def minus(self):
#         return self.n1 - self.n2
#
#     def multipl(self):
#         return self.n1 * self.n2
#
#     def divid(self):
#         return self.n1 / self.n2
#
# calculator = Calculator()
#
# while True:
#     calculator.set_data()
#
#     if calculator.op == '+':
#         print(calculator.plus())
#     elif calculator.op == '-':
#         print(calculator.minus())
#     elif calculator.op == '*':
#         print(calculator.multipl())
#     elif calculator.op == '/':
#         print(calculator.divid())
#     else:
#         print('Error!')

class Homework:
    def len_tmp(self, tmp):
        return len(str(tmp))

    def str_or_num(self, tmp):
        if isinstance(tmp, str):
            glas = 'eyuioa'
            sogl = 'qwrtpsdfghjklzxcvbnm'

            list_glas = [c for c in tmp if c in glas]
            list_sogl = [c for c in tmp if c in sogl]

            if len(list_glas) * len(list_sogl) <= self.len_tmp(tmp):
                print('Vowel letters in the string: ', ''.join(list_glas))
            else:
                print('Consonant letters in the string: ', ''.join(list_sogl))
        else:
            even_nums = sum(int(i) for i in str(tmp) if int(i) % 2 == 0)
            print('Even numbers * len number = ', even_nums * self.len_tmp(tmp))

homework = Homework()
homework.str_or_num('string is the best word in the world')
homework.str_or_num(124827)
