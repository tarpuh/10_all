L = list(map(str, input().split()))
print(list(filter(lambda x: len(x) % 2 == 0, L)))
print([elem for elem in L if len(elem) % 2 == 0])
