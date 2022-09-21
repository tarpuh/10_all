a = list(map(str, input().lower().split()))
b = list(map(str, input().lower().split()))
M = list()
for elem in a:
    if elem in b:
        M.append(elem)
M.sort()
for e in M:
    print(e.lower())

