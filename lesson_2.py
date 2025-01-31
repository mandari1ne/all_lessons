from random import randint

a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
print(f"a = {a}, b = {b}, c = {c}")

print("Perimetr: ", a + b + c)
print("Square: ", a * b / 2, "\n")

num = randint(100, 999)
print("num = ", num)

sum = num // 100 + num % 100 // 10 + num % 10
print("sum = ", sum, "\n")

apple_ann = 2
apple_pol = 5

print(f"Ann has {apple_ann} apples, Pol has {apple_pol} apples", "\n")

cube = randint(1, 10)
print("cube = ", cube)

print("Volume = ", cube ** 3)
print("Side surface area = ", 4 * a ** 2, "\n")

print(20 / (2 - 1), " days")
