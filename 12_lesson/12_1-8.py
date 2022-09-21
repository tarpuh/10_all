# 1
class LittleBell():
    def sound(self):
        print('ding')


# 2
class Button():
    def __init__(self):
        self.cliks = 0

    def click(self):
        self.cliks += 1

    def reset(self):
        self.cliks = 0

    def click_count(self):
        return self.cliks


# 3
class Balance():
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, x):
        self.right += x

    def add_left(self, y):
        self.left += y

    def result(self):
        if self.right > self.left:
            return 'R'
        elif self.right < self.left:
            return 'L'
        else:
            return '='


# 4
class OddEvenSeparator():
    def __init__(self):
        self.list_odd = list()
        self.list_even = list()

    def add_number(self, number):
        if number % 2 == 0:
            self.list_even.append(number)
        else:
            self.list_odd.append(number)

    def even(self):
        return self.list_even

    def odd(self):
        return self.list_odd


# 5
class BigBell():
    def __init__(self):
        self.a = 0

    def sound(self):
        if self.a % 2 == 0:
            print('ding', end='')
        else:
            print('dong', end='')
        self.a += 1


# 6
class MinMaxWordFinder:
    def __init__(self):
        self.max_lenth = 0
        self.min_lenth = 0
        self.max_words = list()
        self.min_words = list()

    def add_sentence(self, sentence):
        for word in list(map(str, sentence.split())):
            if self.min_lenth == 0:
                self.min_lenth = len(word)
                self.min_words.append(word)
            elif len(word) == self.min_lenth:
                self.min_words.append(word)
            if len(word) > self.max_lenth:
                self.max_lenth = len(word)
                self.max_words = list()
                self.max_words.append(word)
            if len(word) == self.max_lenth and word not in self.max_words:
                self.max_words.append(word)
            if len(word) < self.min_lenth:
                self.min_lenth = len(word)
                self.min_words = list()
                self.min_words.append(word)

    def longest_words(self):
        return sorted(self.max_words)

    def shortest_words(self):
        return sorted(self.min_words)


# 7
class BoundingRectangle:
    def __init__(self):
        self.list_x = list()
        self.list_y = list()

    def add_point(self, x, y):
        self.list_x.append(x)
        self.list_y.append(y)

    def width(self):
        return max(self.list_x) - min(self.list_x)

    def height(self):
        return max(self.list_y) - min(self.list_y)

    def bottom_y(self):
        return min(self.list_y)

    def top_y(self):
        return max(self.list_y)

    def left_x(self):
        return min(self.list_x)

    def right_x(self):
        return max(self.list_x)


# 8
class SeaMap:
    def __init__(self):
        self.ground = list()
        for i in range(10):
            self.ground.append(list('..........'))

    def cell(self, x, y):
        return self.ground[x][y]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.ground[row][col] = '*'
        if result == 'hit':
            self.ground[row][col] = 'X'
        if result == 'sink':
            self.ground[row][col] = 'X'
            SeaMap.sink_procces(self, row, col, 11, 11)

    def sink_procces(self, row, col, exeption_row, exeption_col):
        new_row = row - 1
        new_col = col - 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col + 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_row = row
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col - 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_row = row + 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)
        new_col = col + 1
        SeaMap.cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col)

    def cheking_changing(self, new_row, new_col, exeption_row, exeption_col, row, col):
        if (new_row != exeption_row or new_col != exeption_col) and -1 < new_row < 10 and -1 < new_col < 10:
            if self.ground[new_row][new_col] == 'X':
                SeaMap.sink_procces(self, new_row, new_col, row, col)
            else:
                self.ground[new_row][new_col] = '*'
