class Error(RuntimeError):
    pass


class Stack:
    def __init__(self):
        self.L = list()

    def is_empty(self):
        return len(self.L) == 0

    def push(self, item):
        self.L.append(item)

    def pop(self):
        try:
            return self.L.pop()
        except IndexError:
            raise Error

    def peek(self):
        try:
            return self.L[-1]
        except IndexError:
            raise Error

    def size(self):
        return len(self.L)

    def full(self):
        return tuple(self.L)


def calc_pref(a):
    y1 = 0
    y2 = 0
    for el in a:
        if el == ')':
            y1 += 1
        elif el == '(':
            y2 += 1
    if y1 != y2:
        try:
            [].pop()
        except IndexError:
            raise Error
    kolodec = Stack()
    for elem in a[::-1]:
        if elem in '1234567890':
            kolodec.push(float(elem))
        elif elem == '*':
            a = kolodec.pop()
            b = kolodec.pop()
            kolodec.push(a * b)
        elif elem == '/':
            a = kolodec.pop()
            b = kolodec.pop()
            kolodec.push(a / b)
        elif elem == '+':
            a = kolodec.pop()
            b = kolodec.pop()
            kolodec.push(a + b)
        elif elem == '-':
            a = kolodec.pop()
            b = kolodec.pop()
            kolodec.push(a - b)
    if len(kolodec.full()) != 1:
        try:
            [].pop()
        except IndexError:
            raise Error
    L = list(kolodec.full())
    return float(L[0])

