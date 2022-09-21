from random import shuffle

n = int(input())
L = list()
A = list()
for _ in range(n):
    a = input()
    L.append(a)
    A.append(a)
while True:
    shuffle(A)
    f = 0
    for j in range(n):
        if L[j] == A[j]:
            f = 1
    if f == 0:
        print(*[L[i] + '-' + A[i] for i in range(n)])
        break
