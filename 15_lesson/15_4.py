from random import randint

a = int(input())
b = int(input())
L = [randint(a, b) for i in range(5)]
print(list(filter(lambda x: x > 0, L)))
print(list(map(lambda x: x**2 - 15, L)))
