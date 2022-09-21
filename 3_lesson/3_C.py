a = set(map(str, input().split()))
b = set(map(str, input().split()))
c = a - b
d = b - a
li = list(c | d)
li.sort()
for elem in li:
    print(elem)

