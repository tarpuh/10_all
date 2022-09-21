# 1
class LeftParagraph:
    def __init__(self, n):
        self.num = n
        self.l = ['']

    def add_word(self, word):
        if len(self.l[-1]) + len(word) > self.num:
            self.l.append(word + ' ')
        else:
            self.l[-1] += (word + ' ')

    def end(self):
        for elem in self.l:
            print(''.join(elem)[:-1])


class RightParagraph:
    def __init__(self, n):
        self.num = n
        self.l = ['']

    def add_word(self, word):
        if len(self.l[-1]) + len(word) > self.num:
            self.l.append(word + ' ')
        else:
            self.l[-1] += (word + ' ')

    def end(self):
        for elem in self.l:
            print((''.join(elem)[:-1]).rjust(self.num))


# 2
class Rectangle:
    def __init__(self, x1, y1, w, h):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + w
        self.y2 = y1 + h
        self.list_of_x = list()
        self.list_of_y = list()

    def intersection(self, rect):
        self.list_of_x = sorted([self.x1, self.x2, rect.x1, rect.x2])
        self.list_of_y = sorted([self.y1, self.y2, rect.y1, rect.y2])
        if self.x1 >= rect.x2 or rect.x1 >= self.x2 or self.y1 >= rect.y2 or rect.y1 >= self.y2:
            return None
        else:
            return Rectangle(self.list_of_x[1], self.list_of_y[1], self.list_of_x[2] - self.list_of_x[1],
                             self.list_of_y[2] - self.list_of_y[1])

    def get_x(self):
        return self.x1

    def get_y(self):
        return self.y1

    def get_w(self):
        return self.x2 - self.x1

    def get_h(self):
        return self.y2 - self.y1


# 3
class Table:
    def __init__(self, row, col):
        self.rows = row
        self.col = col
        self.tab = list()
        for _ in range(row):
            self.row = list()
            for _ in range(col):
                self.row.append(0)
            self.tab.append(self.row)

    def get_value(self, row, col):
        if 0 <= row < len(self.tab) and 0 <= col < len(self.tab[0]):
            return self.tab[row][col]
        else:
            return None

    def set_value(self, row, col, amount):
        self.tab[row][col] = amount

    def n_rows(self):
        return len(self.tab)

    def n_cols(self):
        return len(self.tab[0])

    def delete_row(self, n):
        self.tab.pop(n)

    def delete_col(self, n):
        for elem in self.tab:
            elem.pop(n)

    def add_row(self, n):
        self.row = list()
        for _ in range(self.col):
            self.row.append(0)
        x = self.tab[:n]
        x.append(self.row)
        x += self.tab[n:]
        self.tab = x

    def add_col(self, n):
        for i in range(len(self.tab)):
            x = self.tab[i][:n]
            x.append(0)
            x += self.tab[i][n:]
            self.tab[i] = x


# 4
class Person:
    def __init__(self, name, otch, fam, direct, ):
        self.name = name
        self.otch = otch
        self.fam = fam
        self.direct = direct

    def get_phone(self, ):
        return self.direct.get('private', None)

    def get_name(self):
        return '{} {} {}'.format(self.fam, self.name, self.otch)

    def get_work_phone(self):
        return self.direct.get('work', None)

    def get_sms_text(self):
        return 'Уважаемый {} {}! Примите участие внашем беспроигрышном конкурсе для физических лиц.'.format(self.name,
                                                                                                            self.otch)


class Company:
    def __init__(self, name, type, direction, *pers):
        self.name = name
        self.type = type
        self.direction = direction
        self.pers = pers

    def get_phone(self):
        phone = self.direction.get('contact', None)
        if not phone:
            for elem in self.pers:
                phone = elem.direct.get('work', None)
                if phone:
                    return phone
        if not phone:
            return None
        return phone

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return 'Для компании {} есть суперпредложение! Примите участие в нашем беспроигрышном конкурсе для {}.'.format(
            self.name, self.type)


def send_sms(*pers):
    for elem in pers:
        if elem.get_phone():
            print('Отправлено СМС на номер {} с текстом: {}'.format(elem.get_phone(), elem.get_sms_text()))
        else:
            print('Не удалось отправить сообщение абоненту: {}'.format(elem.get_name()))


# 5
class ReversedList:
    def __init__(self, L):
        self.spis = L[::-1]

    def __len__(self):
        return len(self.spis)

    def __getitem__(self, item):
        return self.spis[item]


# 6
class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * (x ** 2) + self.b * x + self.c


# 7
class SparseArray:

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, 0)

    def __setitem__(self, key, value):
        self.data[key] = value


# 8
class Queue:
    def __init__(self, *que):
        self.que = list()
        for elem in que:
            self.que.append(str(elem))

    def append(self, *values):
        for elem in values:
            self.que.append(str(elem))

    def copy(self):
        return Queue(*self.que)

    def pop(self):
        return self.que.pop(0)

    def extend(self, que_2):
        for elem in que_2.que:
            self.que.append(str(elem))

    def next(self):
        return Queue(*self.que[1::])

    def __add__(self, other):
        a = self.que[::]
        for elem in other.que:
            a.append(str(elem))
        return Queue(*a)

    def __iadd__(self, other):
        for elem in other.que:
            self.que.append(str(elem))
        return Queue(*self.que)

    def __eq__(self, other):
        return self.que == other.que

    def __rshift__(self, n):
        if n <= len(self.que):
            return Queue(*self.que[n::])
        else:
            return None

    def __str__(self):
        a = '[' + '->'.join(self.que) + ']'
        return a

    def __next__(self):
        return Queue(*self.que[1::])
