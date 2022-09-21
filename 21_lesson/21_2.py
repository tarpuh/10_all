from random import randint


def make_bingo():
    F = list()
    L = list()
    for j in range(5):
        A = list()
        for i in range(5):
            if i != 2 or j != 2:
                while True:
                    k = randint(1, 75)
                    if k not in F:
                        A.append(k)
                        F.append(k)
                        break
            else:
                A.append(0)
        A = tuple(A)
        L.append(A)
    return tuple(L)


print(make_bingo())
