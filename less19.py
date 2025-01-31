# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     #создание свойства
#     @property
#     def model(self): #обязательно делать приватным поля
#         return self.__model
#
#     #сеттер для создания свойства
#     @model.setter
#     def model(self, model): #обязательно делать приватным поля
#         if model < 2000:
#             self.__model = model
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#
#     def get_car_model(self):
#         return 'Год выпуска модели ' + str(self.model)
#
# car = Car(2028)
# print(car.get_car_model())

# import string
#
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def print_info(self):
#         print(self.letters)
#
#     def letters_num(self):
#         return len(self.letters)
#
# class EngAlphabet(Alphabet):
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)
#         self.__letters_num = len(self.letters)
#
#     def is_eng_letter(self, letter):
#         return letter in self.letters
#
#     def letters_num(self):
#         return self.__letters_num
#
#     @staticmethod
#     def example():
#         return '''This is the best english text ever.
#             You should learn english. It is very necessary'''
#
# alphabet = Alphabet('Ru', 'облицовка')
# alphabet.print_info()
# print(alphabet.letters_num(), end='\n\n')
#
# eng_alphabet = EngAlphabet()
# print(eng_alphabet.is_eng_letter('К'))
# print(eng_alphabet.letters_num())
# print(EngAlphabet.example())

import random

class Tomato:
    state = ['planted', 'growing', 'ripe']

    def __init__(self, index):
        self._index = index
        self._state = self.state[random.randint(0, len(self.state) - 1)]

    def grow(self):
        if self._state == 'planted':
            self._state = 'growing'
        elif self._state == 'growing':
            self._state = 'ripe'

    def is_ripe(self):
        return self._state == 'ripe'

class TomatoBush:
    def __init__(self, num_of_tomatoes):
        self.num_of_tomatoes = num_of_tomatoes
        self.tomatoes = [Tomato(i) for i in range(num_of_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato._state = 'ripe'

    def all_are_ripe(self):
        count_grow = 0
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                count_grow += 1

        return count_grow == len(self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, tomato_b):
        self.name = name
        self._plant = tomato_b

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все созрело, хорошая работа!')
        else:
            print('Не весь урожай созрел')

    @staticmethod
    def knowledge_base():
        print('Помидорчики зреют, вы хороший садовод')

tomato_bush = TomatoBush(10)
gardener = Gardener('Albert', tomato_bush)
Gardener.knowledge_base()

gardener.harvest()
gardener.work()
gardener.harvest()
