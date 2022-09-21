def split_expression(s, sign):
    schet = 0
    L = [False, None, None, None]
    kol = -1
    for i in s[::-1]:
        kol -= 1
        if i == ')':
            schet += 1
        elif i == '(':
            schet -= 1
        elif schet == 0 and i in sign and kol != -len(s) - 1 and s[kol] != 'e':
            L[0] = True
            L[1] = i
            L[2] = s[:kol + 1]
            L[3] = s[kol + 2:]
            break
    return L


def calc_expression(a):
    return expr(a)


def expr(a):
    L = split_expression(a, '+-')
    if L[0]:
        if L[1] == '+':
            return expr(L[2]) + item(L[3])
        else:
            return expr(L[2]) - item(L[3])
    else:
        return item(a)


def item(a):
    L = split_expression(a, '*/')
    if L[0]:
        if L[1] == '*':
            return item(L[2]) * factor(L[3])
        else:
            return item(L[2]) / factor(L[3])
    else:
        return factor(a)


def factor(a):
    if a[0] == '-':
        return float(factor(a[1:]) * -1)
    elif a[0] == '+':
        return float(factor(a[1:]) * 1)
    elif a[0] == '(':
        return expr(a[1:-1])
    else:
        return float(a)

