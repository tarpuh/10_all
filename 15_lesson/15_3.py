print(sorted(input().split(), key=lambda x: sum(list(map(int, list(x))))))
