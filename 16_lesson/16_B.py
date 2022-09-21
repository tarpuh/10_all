class Error(RuntimeError):
    pass


class Queue:
    def __init__(self):
        self.L = list()

    def is_empty(self):
        return len(self.L) == 0

    def push(self, item):
        self.L.append(item)

    def pop(self):
        try:
            return self.L.pop(0)
        except IndexError:
            raise Error

    def peek(self):
        try:
            return self.L[0]
        except IndexError:
            raise Error

    def size(self):
        return len(self.L)

    def full(self):
        return tuple(self.L)