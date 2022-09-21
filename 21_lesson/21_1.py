from random import randint

n = int(input())
a = int(input())
b = int(input())
L = list()
for _ in range(n):
    L.append(randint(a, b))
print(*L)
A = filter(lambda x: x > 0, L)
print(*A)
B = list(map(lambda x: x * x - 15, L))
print(*B)
