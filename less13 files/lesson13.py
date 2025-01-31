import random
import string

words = []
for i in range(20):
    word = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3, 7)))
    words.append(word)

arr = (list(random.choice(words) for _ in range(random.randint(3, 5))) +
       list(random.randint(0, 100) for _ in range(random.randint(3, 5))))
random.shuffle(arr)
print('Ваш массив: ', arr)

str_ = [i for i in arr if isinstance(i, str)]
dig = [i for i in arr if isinstance(i, int)]

str_ = sorted(str_, key=len)
dig = sorted(dig)

with open('hw13.txt', 'w+') as f:
    tmp = ' '.join(str_ + [str(i) for i in dig])
    f.write(tmp)

    f.seek(0)
    print('Содержимое файла: ', *f)
