import numpy as np

n = int(input())
L = []
for _ in range(n):
    L.append(input())
L = np.array([L])
values, counts = np.unique(L, return_counts=True)
a = [[values[i], counts[i]] for i in range(len(values))]
a = sorted(a, key=lambda x: x[1])
for i in range(0, 10):
    print(a[-1 - i][0], a[-1 - i][1])


