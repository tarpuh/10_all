def kelemsubsets(L, m):
    k = len(L)
    M = list()
    A = list()
    a = 1
    while a != 2 ** k:
        M = list()
        for i in range(0, len(bin(a)) - 1):
            if bin(a)[-i] == '1':
                M.append(L[i - 1])
        if len(M) == m:
            A.append(M)
        a += 1

    return A

