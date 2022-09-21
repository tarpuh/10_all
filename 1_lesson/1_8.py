L = list(map(int, input().split()))
id = 0
x = 2
kol = 0
y = -1
maximum = 0
for elem in L:
    x = elem

    if elem == x:
        if y == -1:
            y = id - 1
        kol += 1
    else:
        kol = 0
        y = -1
    id += 1