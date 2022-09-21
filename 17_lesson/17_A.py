def split_expression(s, sign):
    schet = 0
    L = [False, None, None, None]
    kol = -1
    for i in s[::-1]:
        kol -= 1
        if i == ')':
            schet += 1
        if i == '(':
            schet -= 1
        if schet == 0 and i in sign and kol != -len(s) - 1 and s[kol] != 'e':
            L[0] = True
            L[1] = i
            L[2] = s[:kol + 1]
            L[3] = s[kol + 2:]
    return L

