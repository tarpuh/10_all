def fib(n):
    L = list()
    for i in range(n):
        if len(L) < 2:
            L.append(1)
        else:
            L.append(L[-1] + L[-2])
        yield L[-1]


print(*enumerate(list(fib(int(input()))), start=1))

