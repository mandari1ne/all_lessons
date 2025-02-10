class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        if a == int and b == int:
            return a + b
        else:
            raise ValueError

    def minus(self, a, b):
        return a - b

    def multipl(self, a, b):
        return a * b

    def divid(self, a, b):
        return a / b
