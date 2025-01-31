# class Phone:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     @classmethod
#     def toy_phone(cls, color):
#         toy_phone = cls.model_hash(color, 'ToyPhone', None)
#         return toy_phone
#
#     def check_sim(self, mobile_oper):
#         if self.model == 'I785' and mobile_oper == 'MTS':
#             print('Your mobile operator is MTS')
#
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
#
# Phone.model_hash('I785')
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')
# Phone.toy_phone('red', 'I785')

# class Human:
#     default_name = 'Albert'
#     default_age = 18
#
#     def __init__(self, name = default_name, age = default_age):
#         self.name = name
#         self.age = age
#         self.__money = 909
#         self.__house = 'deteched'
#
#     def info(self):
#         print(f'Name: {self.name}, age: {self.age}, money: {self.__money}, house: {self.__house}')
#
#     @staticmethod
#     def default_info():
#         print(f'Default name: {Human.default_name}, default age: {Human.default_age}')
#
#     def earn_money(self):
#         amount = int(input('Enter amount of money: '))
#         self.__money += amount
#
# Human.default_info()
# human = Human('Alfons', 24)
# human.earn_money()
# human.info()

# class Phone:
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         self.is_on = True
#
#     def call(self):
#         if self.is_on:
#             print('Making call....')
#
# class MobilePhone(Phone):
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     def charge(self, num):
#         self.battery = num
#
# mobile_phone = MobilePhone()
# print(mobile_phone)

class Human:
    default_name = 'Albert'
    default_age = 18

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 909
        self.__house = 'deteched'

    def info(self):
        print(f'Name: {self.name}, age: {self.age}, money: {self.__money}, house: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}, default age: {Human.default_age}')

    def earn_money(self):
        amount = int(input('Enter amount of money: '))
        self.__money += amount

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, buying_house, sale):
        if self.__money >= buying_house.final_price(sale):
            self.__make_deal(buying_house, buying_house.price(sale))
        else:
            print('Not enough money')

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        return self._price * sale + self._price

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)

house1 = House(789, 3400)
smh = SmallHouse(678)
human = Human('Alfonse', 24)
human.info()
human.buy_house(house1, 5)
