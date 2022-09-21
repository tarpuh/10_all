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


def inf_to_pref(a):
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
    vir = Stack()
    zna = Stack()
    for elem in a[::-1]:
        if elem in '1234567890':
            vir.push(elem)
        elif elem in ')*/':
            zna.push(elem)
        elif elem == '(':
            while not zna.is_empty():
                if zna.peek() != ')':
                    vir.push(zna.pop())
                else:
                    zna.pop()
                    break

        elif elem in '+-':
            if not zna.is_empty():
                if zna.peek() in '*/':
                    while not zna.is_empty() and zna.peek() in '/*':
                        vir.push(zna.pop())
                zna.push(elem)
            else:
                zna.push(elem)
    while not zna.is_empty():
        vir.push(zna.pop())
    L = list(vir.full()[::-1])
    return ''.join(L)