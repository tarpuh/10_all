a = list(map(str, input().split()))
b = set()
i = 0
for elem in a:
    b.add(elem)
    i += 1
    if len(b) != i:
        print('YES')
        i -= 1
    else:
        print('NO')

