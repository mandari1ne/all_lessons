class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        while True:
            ch = float(input('Choose one options: [1] a - b; [2] b - a\n'))

            if ch == 1:
                return self.a - self.b
            elif ch == 2:
                return self.b - self.a

    def multipl(self):
        return self.a * self.b

    def divid(self):
        while True:
            ch = int(input('Choose one options: [1] a / b; [2] b / a\n'))

            try:
                if ch == 1:
                    return self.a / self.b
                elif ch == 2:
                    return self.b / self.a
            except ZeroDivisionError:
                print('Error!!!')

calculator = Calculator(5, 0)

print(calculator.divid())
