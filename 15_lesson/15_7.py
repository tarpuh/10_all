def checking_star(s):
    if s[0] == '*':
        return s[1:]
    else:
        return s


L = list(map(checking_star, (filter(lambda x: x[0] != 'V' and x[0] != 'v', input().split('; ')))))
for i in L:
    print(i)
