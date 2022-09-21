def minimum(L, a):
    for i in range(len(L)):
        if min(L) > a:
            return min(L)
        else:
            L.remove(min(L))


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


def permutations(L):
    L = list(L)
    L.sort()
    M = list()
    M.append(L[::])
    k = 0
    while k != fac(len(L)) - 1:
        for i in range(-1, -len(L), -1):
            if L[i - 1] <= L[i]:
                id = L.index(minimum(L[i:], L[i - 1]))
                L[i - 1], L[id] = L[id], L[i - 1]
                L[i:] = sorted(L[i:])
                break
        M.append(L[::])
        k += 1

    return M



