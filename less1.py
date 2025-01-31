x = 10
y = 5

sum_result = x + y
print("sum_result =", sum_result, "\n")

name = input("Enter your name: ")
print("Your name:", name, "\n")

age = input("Enter your age: ")
age_int = int(age)

print("Your age:", age_int)
print("Type age_int:", type(age_int), "\n")

message = f"Привет, меня зовут {name} и мне {age_int} лет"
print(message, "\n")

print("Address sum_result:", id(sum_result), "\n")

mult_result = x * y
print("mult_result = ", mult_result, "\n")

greeting = "Hello, World!"
print(greeting)
